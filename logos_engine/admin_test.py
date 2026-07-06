"""Local admin test helpers for turning raw meaning into review previews."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from textwrap import shorten
from typing import Any

from logos_engine.wf_0001_idea_intake import validate_wf_0001_idea_intake


CONFIRM_INTAKE = "CREATE_WF_0001_HUMAN_TRUTH_ISSUE"
SUPPORTED_LANGUAGES = {"en", "ru", "uk", "mixed"}
SUPPORTED_SCOPES = {"universal", "runtime"}


@dataclass(frozen=True)
class AdminPreview:
    raw_meaning: str
    language: str
    scope: str
    audience_context: str
    source: str
    human_truth_candidate: str
    human_contradiction_candidate: str
    old_frame: str
    new_frame: str
    belief_shift_candidate: str
    meaning_atom_draft: str
    story_pattern_draft: str
    emotional_result_draft: str
    draft_status: str
    needs_clarification: bool
    detected_risks: list[str]
    test_plan: str
    risk_notes: str
    wf_0001_payload: dict[str, Any]
    wf_0001_issue_title: str
    wf_0001_issue_body: str
    wf_0002_blocked_reason: str
    next_questions: list[str]
    safety: dict[str, bool]

    def to_dict(self) -> dict[str, Any]:
        return {
            "raw_meaning": self.raw_meaning,
            "language": self.language,
            "scope": self.scope,
            "audience_context": self.audience_context,
            "source": self.source,
            "human_truth_candidate": self.human_truth_candidate,
            "human_contradiction_candidate": self.human_contradiction_candidate,
            "old_frame": self.old_frame,
            "new_frame": self.new_frame,
            "belief_shift_candidate": self.belief_shift_candidate,
            "meaning_atom_draft": self.meaning_atom_draft,
            "story_pattern_draft": self.story_pattern_draft,
            "emotional_result_draft": self.emotional_result_draft,
            "draft_status": self.draft_status,
            "needs_clarification": self.needs_clarification,
            "detected_risks": self.detected_risks,
            "test_plan": self.test_plan,
            "risk_notes": self.risk_notes,
            "wf_0001_payload": self.wf_0001_payload,
            "wf_0001_issue": {
                "title": self.wf_0001_issue_title,
                "body": self.wf_0001_issue_body,
                "review_ready": True,
                "yaml_promotion_ready": False,
            },
            "wf_0002": {
                "ready": False,
                "blocked_reason": self.wf_0002_blocked_reason,
            },
            "next_questions": self.next_questions,
            "safety": self.safety,
        }


def _clean_text(value: Any, *, default: str = "") -> str:
    if value is None:
        return default
    if not isinstance(value, str):
        raise ValueError("all text fields must be strings")
    return value.strip()


def _short(value: str, width: int = 96) -> str:
    return shorten(" ".join(value.split()), width=width, placeholder="...")


def _first_sentence(value: str) -> str:
    normalized = " ".join(value.split())
    for separator in (".", "!", "?", "\n"):
        if separator in normalized:
            candidate = normalized.split(separator, 1)[0].strip()
            if candidate:
                return candidate
    return normalized


def _candidate_human_truth(raw_meaning: str, supplied: str) -> str:
    if supplied:
        return supplied
    base = _first_sentence(raw_meaning)
    lowered = base.lower()
    if lowered.startswith(("люди", "человек", "people", "a person", "person")):
        return base
    return f"Люди узнают себя в ситуации, где: {base}"


def _detected_risks(raw_meaning: str, risk_notes: str) -> list[str]:
    raw_lower = raw_meaning.lower()
    risks: list[str] = []
    if risk_notes:
        risks.append(risk_notes)
    if "женщин" in raw_lower or "женщиной" in raw_lower or "женщина" in raw_lower:
        risks.append("может звучать как обязанность женщины давать безопасность")
    if "делится" in raw_lower or "отда" in raw_lower or "возвращ" in raw_lower:
        risks.append("может звучать как сделка или обязанная отдача")
    if "захват" in raw_lower or "территор" in raw_lower:
        risks.append("может звучать как доминирование или буквальное расширение власти")
    if "привя" in raw_lower:
        risks.append("может звучать как зависимость вместо свободной привязанности")
    if not risks:
        risks.append("смысл может быть прочитан как давление, долг или манипуляция")

    deduped: list[str] = []
    for risk in risks:
        if risk not in deduped:
            deduped.append(risk)
    return deduped


def _candidate_contradiction(human_truth: str, risks: list[str]) -> str:
    risk = "; ".join(risks)
    return (
        "Человек может узнавать правду в этом наблюдении, "
        f"но одновременно сопротивляться ему, если {risk}."
    )


def _candidate_frames(
    human_truth: str,
    desired_change: str,
    risks: list[str],
) -> tuple[str, str]:
    old_frame = (
        f"Этот смысл можно читать опасно или узко: {'; '.join(risks)}"
    )
    new_frame = (
        desired_change
        if desired_change
        else f"Этот смысл становится полезным, когда он сохраняет человеческую правду: {human_truth}"
    )
    return old_frame, new_frame


def _meaning_atom(human_truth: str, desired_change: str) -> str:
    if desired_change:
        return _first_sentence(desired_change)
    words = _first_sentence(human_truth).split()
    if len(words) <= 14:
        return _first_sentence(human_truth)
    return " ".join(words[:14]).rstrip(".,;:") + "."


def _story_pattern(old_frame: str, new_frame: str) -> str:
    return (
        "Показать знакомую ситуацию, где старое прочтение выглядит естественным; "
        "затем раскрыть скрытое напряжение; затем дать человеку безопасный переход "
        f"к новому прочтению: {new_frame}"
    )


def _incomplete_story_pattern() -> str:
    return (
        "Черновик не собран: сначала нужно уточнить желаемый переход и риск неверного прочтения. "
        "Пока безопаснее работать в режиме вопросов, а не готового Story Pattern."
    )


def _test_plan(audience_context: str) -> str:
    return "\n".join(
        [
            "Purpose: Check whether raw meaning can become a review-ready Human Truth candidate.",
            f"Input: One raw meaning from local admin test for {audience_context}.",
            "Expected output: One structured preview with preserved raw meaning and blocked YAML promotion.",
            "Manual test: Read the preview and answer whether the belief movement is recognizable.",
            "Acceptance criteria: Raw meaning is preserved, risks are visible, no YAML object is written.",
            "Evidence: Local admin preview output and validator result.",
            "Future automation: Create a GitHub review issue only after human confirmation.",
        ]
    )


def _next_questions(raw_meaning: str, desired_change: str, risk_notes: str) -> list[str]:
    questions = [
        "Кто именно должен узнать себя в этом смысле?",
        "Что человек должен перестать считать после этого перехода?",
        "Что человек должен начать считать вместо этого?",
    ]
    if not desired_change:
        questions.append("Какой новый взгляд должен появиться у человека после контакта со смыслом?")
    if not risk_notes:
        questions.append("Где этот смысл может быть прочитан как давление, долг или манипуляция?")
    raw_lower = raw_meaning.lower()
    if "женщин" in raw_lower or "женщиной" in raw_lower or "женщина" in raw_lower:
        questions.append("Как показать безопасность так, чтобы женщина не выглядела обязанной её давать?")
    if "захват" in raw_lower or "территор" in raw_lower:
        questions.append("Как заменить буквальный захват территорий на метафору возможностей без доминирования?")
    if "делится" in raw_lower:
        questions.append("Как показать добровольную отдачу, чтобы она не выглядела оплатой за безопасность?")
    if len(raw_meaning) < 80:
        questions.append("Какой живой пример или сцена показывает этот смысл без объяснения?")
    return questions


def _build_wf_0001_issue_body(
    *,
    scope: str,
    source: str,
    raw_meaning: str,
    human_truth: str,
    risk_notes: str,
    test_plan: str,
) -> str:
    marker = f"local_admin_test:{datetime.now(UTC).isoformat()}"
    meaning_resources = risk_notes or "Needs human review."
    return "\n".join(
        [
            "## LOGOS ID",
            "HT-0000",
            "## Status",
            "candidate",
            "## Scope",
            scope,
            "## Source or context",
            source,
            "## Raw observation",
            raw_meaning,
            "## Human Truth candidate",
            human_truth,
            "## Meaning resources",
            meaning_resources,
            "## Test plan",
            test_plan,
            "## Connected objects",
            "Local Admin Test, WF-0001 preview",
            "## Intake evidence",
            f"Marker: {marker}",
            "Workflow: LOGOS WF-0001 Idea Intake Issue Gate",
            "Generated by local admin test preview, not by YAML promotion.",
            "Safety:",
            "- GitHub Issue creation only after human confirmation",
            "- no YAML object writeback",
            "- no learning or law artifact",
            "- no VPS reboot or service restart",
            "- no secrets in issue body",
        ]
    )


def build_admin_preview(payload: dict[str, Any]) -> AdminPreview:
    """Build a deterministic local admin preview from a raw meaning payload."""

    if not isinstance(payload, dict):
        raise ValueError("payload must be a JSON object")

    raw_meaning = _clean_text(payload.get("raw_meaning"))
    if not raw_meaning:
        raise ValueError("raw_meaning must be non-empty")

    language = _clean_text(payload.get("language"), default="ru")
    if language not in SUPPORTED_LANGUAGES:
        raise ValueError("language must be en, ru, uk or mixed")

    scope = _clean_text(payload.get("scope"), default="universal")
    if scope not in SUPPORTED_SCOPES:
        raise ValueError("scope must be universal or runtime")

    audience_context = _clean_text(
        payload.get("audience_context"),
        default="local admin reviewer",
    )
    source = _clean_text(payload.get("source"), default="local admin test input")
    supplied_human_truth = _clean_text(payload.get("human_truth_candidate"))
    desired_change = _clean_text(payload.get("desired_change"))
    risk_notes = _clean_text(payload.get("risk_notes"))
    needs_clarification = not desired_change or not risk_notes

    human_truth = _candidate_human_truth(raw_meaning, supplied_human_truth)
    detected_risks = _detected_risks(raw_meaning, risk_notes)
    human_contradiction = _candidate_contradiction(human_truth, detected_risks)
    old_frame, new_frame = _candidate_frames(human_truth, desired_change, detected_risks)
    belief_shift = f"{old_frame} -> {new_frame}"
    meaning_atom = _meaning_atom(human_truth, desired_change)
    story_pattern = (
        _incomplete_story_pattern()
        if needs_clarification
        else _story_pattern(old_frame, new_frame)
    )
    emotional_result = "recognition_without_pressure"
    test_plan = _test_plan(audience_context)

    wf_0001_payload = {
        "confirm_intake": CONFIRM_INTAKE,
        "raw_idea": raw_meaning,
        "source": source,
        "language": language,
        "scope": scope,
        "optional_context": audience_context,
        "human_truth_candidate": human_truth,
        "meaning_resources": risk_notes or "Needs review.",
        "test_plan": test_plan,
        "connected_objects": "Local Admin Test",
        "title_suffix": _short(human_truth, 100),
    }
    validate_wf_0001_idea_intake(wf_0001_payload)

    issue_title = f"HT-0000: {_short(human_truth, 100)}"
    issue_body = _build_wf_0001_issue_body(
        scope=scope,
        source=source,
        raw_meaning=raw_meaning,
        human_truth=human_truth,
        risk_notes=risk_notes,
        test_plan=test_plan,
    )

    return AdminPreview(
        raw_meaning=raw_meaning,
        language=language,
        scope=scope,
        audience_context=audience_context,
        source=source,
        human_truth_candidate=human_truth,
        human_contradiction_candidate=human_contradiction,
        old_frame=old_frame,
        new_frame=new_frame,
        belief_shift_candidate=belief_shift,
        meaning_atom_draft=meaning_atom,
        story_pattern_draft=story_pattern,
        emotional_result_draft=emotional_result,
        draft_status="needs_clarification" if needs_clarification else "preview_candidate",
        needs_clarification=needs_clarification,
        detected_risks=detected_risks,
        test_plan=test_plan,
        risk_notes=risk_notes or "Not provided yet.",
        wf_0001_payload=wf_0001_payload,
        wf_0001_issue_title=issue_title,
        wf_0001_issue_body=issue_body,
        wf_0002_blocked_reason=(
            "WF-0002 requires a reviewed stable HT-#### source. "
            "This admin preview still uses HT-0000 and cannot create Belief Shift YAML."
        ),
        next_questions=_next_questions(raw_meaning, desired_change, risk_notes),
        safety={
            "local_preview_only": True,
            "no_yaml_writeback": True,
            "no_github_issue_created": True,
            "no_learning_or_law_created": True,
            "requires_human_review": True,
        },
    )
