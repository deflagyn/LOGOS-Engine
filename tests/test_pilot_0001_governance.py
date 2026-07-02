from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
import json
from pathlib import Path

from logos_engine.validate import validate_repository


ROOT = Path(__file__).resolve().parents[1]


def copy_repo_to_temp(temp_dir: Path) -> Path:
    target = temp_dir / "repo"
    shutil.copytree(
        ROOT,
        target,
        ignore=shutil.ignore_patterns(
            ".git",
            ".secrets",
            ".venv",
            "__pycache__",
            "*.pyc",
        ),
    )
    return target


def issue_messages(root: Path) -> list[str]:
    return [issue.render() for issue in validate_repository(root)]


def load_response_input(repo: Path) -> dict[str, object]:
    fixture = repo / "testing" / "fixtures" / "pilot-0001-response-input.json.example"
    return json.loads(fixture.read_text(encoding="utf-8"))


def write_response_input(repo: Path, data: dict[str, object]) -> Path:
    input_path = repo / "testing" / "fixtures" / "tmp-response-input.json"
    input_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return input_path


def run_response_intake(repo: Path, input_path: Path) -> subprocess.CompletedProcess[str]:
    script = repo / "scripts" / "create_pilot_response.py"
    return subprocess.run(
        [sys.executable, str(script), "--input", str(input_path)],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def run_response_schema_validation(repo: Path, input_path: Path) -> subprocess.CompletedProcess[str]:
    script = repo / "scripts" / "validate_pilot_response_input.py"
    return subprocess.run(
        [sys.executable, str(script), "--input", str(input_path)],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def run_pilot_status(repo: Path) -> dict[str, object]:
    script = repo / "scripts" / "pilot_0001_status.py"
    result = subprocess.run(
        [sys.executable, str(script), "--json"],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stderr)
    return json.loads(result.stdout)


class Pilot0001GovernanceTests(unittest.TestCase):
    def test_response_input_fixture_matches_schema(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp_dir:
            repo = copy_repo_to_temp(Path(raw_temp_dir))
            fixture = repo / "testing" / "fixtures" / "pilot-0001-response-input.json.example"

            result = run_response_schema_validation(repo, fixture)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PILOT-0001 response input schema passed.", result.stdout)

    def test_response_input_schema_rejects_missing_required_answer(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp_dir:
            repo = copy_repo_to_temp(Path(raw_temp_dir))
            data = load_response_input(repo)
            answers = data["answers"]
            assert isinstance(answers, dict)
            del answers["q1_changed_in_hero"]
            input_path = write_response_input(repo, data)

            result = run_response_schema_validation(repo, input_path)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("q1_changed_in_hero", result.stderr)

    def test_learning_requires_three_real_responses(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp_dir:
            repo = copy_repo_to_temp(Path(raw_temp_dir))
            learning_path = repo / "pilots" / "PILOT-0001" / "output" / "learning.md"
            learning_path.write_text("# Fake learning\n", encoding="utf-8")

            messages = issue_messages(repo)

        self.assertTrue(
            any(
                "learning/law artifact requires at least 3 real responses; found 0" in message
                for message in messages
            ),
            messages,
        )

    def test_declared_path_reference_must_exist(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp_dir:
            repo = copy_repo_to_temp(Path(raw_temp_dir))
            fixture_path = (
                repo / "testing" / "fixtures" / "reference-integrity" / "broken-path.yaml"
            )
            fixture_path.write_text(
                "\n".join(
                    [
                        "id: TMP-PATH-REFERENCE-0001",
                        "type: test_fixture",
                        "status: invalid",
                        "source_path: missing/path/does-not-exist.md",
                        "",
                    ]
                ),
                encoding="utf-8",
            )

            messages = issue_messages(repo)

        self.assertTrue(
            any(
                "reference path does not exist: missing/path/does-not-exist.md" in message
                for message in messages
            ),
            messages,
        )

    def test_response_intake_creates_real_response_and_updates_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp_dir:
            repo = copy_repo_to_temp(Path(raw_temp_dir))
            fixture = repo / "testing" / "fixtures" / "pilot-0001-response-input.json.example"
            result = run_response_intake(repo, fixture)

            response_path = (
                repo
                / "pilots"
                / "PILOT-0001"
                / "experiment"
                / "responses"
                / "RESPONSE-PILOT-0001-0001.yaml"
            )
            response_exists = response_path.exists()
            manifest = (repo / "pilots" / "PILOT-0001" / "RUN-MANIFEST.yaml").read_text(
                encoding="utf-8"
            )
            messages = issue_messages(repo)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("created pilots/PILOT-0001/experiment/responses/", result.stdout)
        self.assertTrue(response_exists)
        self.assertIn("real_response_count: 1", manifest)
        self.assertEqual(messages, [])

    def test_response_intake_rejects_personal_data_not_removed(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp_dir:
            repo = copy_repo_to_temp(Path(raw_temp_dir))
            data = load_response_input(repo)
            data["personal_data_removed"] = False
            input_path = write_response_input(repo, data)

            result = run_response_intake(repo, input_path)
            response_files = list(
                (repo / "pilots" / "PILOT-0001" / "experiment" / "responses").glob(
                    "RESPONSE-PILOT-0001-*.yaml"
                )
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("personal_data_removed must be true", result.stderr)
        self.assertEqual(response_files, [])

    def test_response_intake_rejects_simulated_response(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp_dir:
            repo = copy_repo_to_temp(Path(raw_temp_dir))
            data = load_response_input(repo)
            data["simulated_response"] = True
            input_path = write_response_input(repo, data)

            result = run_response_intake(repo, input_path)
            response_files = list(
                (repo / "pilots" / "PILOT-0001" / "experiment" / "responses").glob(
                    "RESPONSE-PILOT-0001-*.yaml"
                )
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("simulated responses must not be written", result.stderr)
        self.assertEqual(response_files, [])

    def test_pilot_status_reports_waiting_for_responses(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp_dir:
            repo = copy_repo_to_temp(Path(raw_temp_dir))
            status = run_pilot_status(repo)

        self.assertEqual(status["response_count"], 0)
        self.assertEqual(status["manifest_response_count"], 0)
        self.assertFalse(status["learning_allowed"])
        self.assertTrue(status["validation_passed"])
        self.assertEqual(status["next_action"], "collect_real_responses")

    def test_respondent_handout_does_not_expose_internal_traceability(self) -> None:
        handout = (
            ROOT / "pilots" / "PILOT-0001" / "experiment" / "RESPONDENT-HANDOUT.md"
        ).read_text(encoding="utf-8")

        forbidden_fragments = [
            "RM-PILOT-0001",
            "ME-PILOT-0001",
            "HT-PILOT-0001",
            "HC-PILOT-0001",
            "BS-PILOT-0001",
            "MA-PILOT-0001",
            "SP-PILOT-0001",
            "## Source Objects",
            "## Belief Movement",
            "## What Was Preserved",
            "## What Was Changed",
        ]
        for fragment in forbidden_fragments:
            self.assertNotIn(fragment, handout)

        self.assertIn("## Draft Scene", handout)
        self.assertIn("## Questions", handout)

    def test_pilot_status_allows_learning_after_three_valid_responses(self) -> None:
        with tempfile.TemporaryDirectory() as raw_temp_dir:
            repo = copy_repo_to_temp(Path(raw_temp_dir))
            fixture = repo / "testing" / "fixtures" / "pilot-0001-response-input.json.example"

            for _ in range(3):
                result = run_response_intake(repo, fixture)
                self.assertEqual(result.returncode, 0, result.stderr)

            status = run_pilot_status(repo)

        self.assertEqual(status["response_count"], 3)
        self.assertEqual(status["manifest_response_count"], 3)
        self.assertTrue(status["learning_allowed"])
        self.assertTrue(status["validation_passed"])
        self.assertEqual(status["next_action"], "draft_learning_candidate_from_real_responses")


if __name__ == "__main__":
    unittest.main()
