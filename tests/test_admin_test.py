from __future__ import annotations

import unittest

from logos_engine.admin_test import build_admin_preview
from logos_engine.wf_0001_issue import validate_wf_0001_issue_body


class AdminTestPreviewTests(unittest.TestCase):
    def test_admin_preview_preserves_raw_meaning_and_blocks_yaml(self) -> None:
        preview = build_admin_preview(
            {
                "raw_meaning": (
                    "Если человек получает безопасное пространство, он перестаёт "
                    "быть в режиме защиты и у него появляются силы действовать спокойнее."
                ),
                "audience_context": "первый личный тест",
                "language": "ru",
                "scope": "universal",
                "desired_change": (
                    "От безопасности как слабости к безопасности как возвращению ресурса."
                ),
                "risk_notes": "Может прозвучать как долг или сделка.",
                "source": "local admin personal test",
            }
        )
        data = preview.to_dict()

        self.assertIn("безопасное пространство", data["raw_meaning"])
        self.assertIn("Система предлагает читать это так", data["new_frame"])
        self.assertIn("безопасность", data["new_frame"])
        self.assertIn("Безопасность без давления", data["meaning_atom_draft"])
        self.assertNotEqual(data["new_frame"], "От безопасности как слабости к безопасности как возвращению ресурса.")
        self.assertEqual(data["wf_0001_payload"]["confirm_intake"], "CREATE_WF_0001_HUMAN_TRUTH_ISSUE")
        self.assertTrue(data["wf_0001_issue"]["review_ready"])
        self.assertFalse(data["wf_0001_issue"]["yaml_promotion_ready"])
        self.assertFalse(data["wf_0002"]["ready"])
        self.assertIn("stable HT-####", data["wf_0002"]["blocked_reason"])
        self.assertTrue(data["safety"]["no_yaml_writeback"])
        self.assertTrue(data["safety"]["no_github_issue_created"])

    def test_admin_preview_issue_body_is_wf_0001_review_ready(self) -> None:
        preview = build_admin_preview(
            {
                "raw_meaning": "Люди лучше доверяют системе, когда источник смысла сохранён.",
                "language": "ru",
                "scope": "universal",
            }
        )

        issue = validate_wf_0001_issue_body(
            preview.wf_0001_issue_body,
            title=preview.wf_0001_issue_title,
        )

        self.assertEqual(issue.logos_id, "HT-0000")
        self.assertEqual(issue.status, "candidate")
        self.assertEqual(issue.scope, "universal")

    def test_admin_preview_rejects_empty_raw_meaning(self) -> None:
        with self.assertRaisesRegex(ValueError, "raw_meaning"):
            build_admin_preview({"raw_meaning": "   "})

    def test_admin_preview_rejects_unknown_language(self) -> None:
        with self.assertRaisesRegex(ValueError, "language"):
            build_admin_preview({"raw_meaning": "test", "language": "de"})

    def test_first_personal_test_stays_in_clarification_mode(self) -> None:
        preview = build_admin_preview(
            {
                "raw_meaning": (
                    "Если мужчина получает от женщины безопасное пространство он там начинает "
                    "отдыхать, привязываться и как следствие появляется больше ресурсов у него "
                    "для захвата более новых территорий с новыми ресурсами которыми он делится "
                    "со своей женщиной."
                ),
                "audience_context": "первый личный тест",
                "language": "ru",
                "scope": "universal",
            }
        )
        data = preview.to_dict()

        self.assertTrue(data["needs_clarification"])
        self.assertEqual(data["draft_status"], "needs_clarification")
        self.assertNotIn("...", data["human_truth_candidate"])
        self.assertIn(
            "для захвата более новых территорий",
            data["human_truth_candidate"],
        )
        self.assertIn("Черновик не собран", data["story_pattern_draft"])
        self.assertTrue(
            any("обязанность женщины" in risk for risk in data["detected_risks"]),
            data["detected_risks"],
        )
        self.assertTrue(
            any("доминирование" in risk for risk in data["detected_risks"]),
            data["detected_risks"],
        )
        self.assertTrue(
            any("отдачу" in question for question in data["next_questions"]),
            data["next_questions"],
        )

    def test_dialogue_answers_are_inputs_not_the_system_solution(self) -> None:
        preview = build_admin_preview(
            {
                "raw_meaning": (
                    "Если мужчина получает от женщины безопасное пространство он там начинает "
                    "отдыхать, привязываться и как следствие появляется больше ресурсов у него."
                ),
                "audience_context": (
                    "женщины должны увидеть через простые смыслы что для комфортной жизни "
                    "с мужчиной ничего сложного делать не надо"
                ),
                "language": "ru",
                "scope": "universal",
                "desired_change": (
                    "От: убрать силу навязанных когинтивных искажений всякими инста коучерами\n"
                    "К: не надо лишний раз компосировать мужику мозги. надо искать другой способ взаимодействия"
                ),
                "risk_notes": "не превращать смысл в обязанность женщины",
            }
        )
        data = preview.to_dict()

        self.assertIn("Система предлагает читать это так", data["new_frame"])
        self.assertNotIn("компосировать", data["new_frame"])
        self.assertNotIn("инста коучерами", data["new_frame"])
        self.assertNotIn("инста коучерами", data["meaning_atom_draft"])
        self.assertEqual(
            data["meaning_atom_draft"],
            "Безопасность без давления возвращает ресурс для спокойного вклада в отношения.",
        )


if __name__ == "__main__":
    unittest.main()
