import json
import os


class JSONOutputAgent:

    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_faq_page(self, faq_page, filename="faq.json"):
        self._save_json(faq_page, filename)

    def save_product_page(self, product_page, filename="product_page.json"):
        self._save_json(product_page, filename)

    def save_comparison_page(self, comparison_page, filename="comparison_page.json"):
        self._save_json(comparison_page, filename)

    def _save_json(self, data, filename):
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f" Saved: {filepath}")
