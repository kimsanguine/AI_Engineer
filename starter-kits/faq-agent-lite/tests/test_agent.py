import unittest

from agent import answer_question, format_response


class FaqAgentLiteTest(unittest.TestCase):
    def test_returns_sourced_billing_answer(self):
        match = answer_question("Can I change my billing date?")
        self.assertIsNotNone(match)
        self.assertEqual(match.faq_id, "FAQ-001")
        self.assertEqual(match.category, "billing")

    def test_refuses_unknown_question(self):
        response = format_response("What is the weather in Seoul tomorrow?")
        self.assertIn("I do not know", response)
        self.assertIn("public synthetic FAQ", response)

    def test_security_question_routes_to_privacy_boundary(self):
        match = answer_question("Should I send personal identifiers to the AI assistant?")
        self.assertIsNotNone(match)
        self.assertEqual(match.faq_id, "FAQ-004")


if __name__ == "__main__":
    unittest.main()
