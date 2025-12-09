class QuestionAgent:
    def generate_questions(self, product):
        questions = {
            "Informational": [
                f"What is {product['name']}?",
                f"What are the key ingredients in {product['name']}?",
                "What skin types is this serum suitable for?",
                "What are the main benefits of using this serum?"
            ],
            "Usage": [
                "How do I apply this serum?",
                "How many drops should I use per application?",
                "Can I use it at night instead of morning?",
                "Should I apply moisturizer before or after using the serum?"
            ],
            "Safety": [
                "Are there any side effects?",
                "Is this serum safe for sensitive skin?",
                "Can this product cause irritation or redness?",
                "Can it be used daily?"
            ],
            "Purchase": [
                "What is the price of this serum?",
                "Is this product budget-friendly?",
                "Where can I buy it?"
            ],
            "Comparison": [
                "How does this serum compare to other Vitamin C serums?",
                "Is this serum better for oily skin than Product B?"
            ]
        }

        return questions
