class LogicAgent:

    def generate_benefits_block(self, product):
        
        benefits = ", ".join(product["benefits"])
        return f"This serum provides the following benefits: {benefits}."

    def generate_usage_block(self, product):
        return f"How to use: {product['how_to_use']}."

    def generate_side_effects_block(self, product):
        return f"Possible side effects include: {product['side_effects']}."

    def generate_price_block(self, product):
        return f"The product is priced at {product['price']}."

    def generate_comparison_block(self, product):
        comparison_data = {
            "Product A": product["name"],
            "Product B": "RadiancePro Skin Serum",
            "Difference": "RadiancePro contains Niacinamide instead of Hyaluronic Acid and is more expensive."
        }
        return comparison_data
