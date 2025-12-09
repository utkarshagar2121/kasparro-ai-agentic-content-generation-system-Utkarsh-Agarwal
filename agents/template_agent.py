class TemplateAgent:
    def build_faq_page(self, product, questions, logic_blocks):
        faq_page = {
            "title": f"FAQs for {product['name']}",
            "categories": []
        }

        for category, qs in questions.items():
            faq_page["categories"].append({
                "category_name": category,
                "questions": qs
            })

        return faq_page

    def build_product_page(self, product, logic_blocks):
        product_page = {
            "product_name": product["name"],
            "concentration": product["concentration"],
            "skin_type": product["skin_type"],
            "content_blocks": [
                logic_blocks["benefits"],
                logic_blocks["usage"],
                logic_blocks["side_effects"],
                logic_blocks["price"]
            ]
        }

        return product_page

    def build_comparison_page(self, product, logic_blocks):
        comparison_page = {
            "Product_A": product["name"],
            "Product_B": logic_blocks["comparison"]["Product B"],
            "Key_Difference": logic_blocks["comparison"]["Difference"]
        }

        return comparison_page
