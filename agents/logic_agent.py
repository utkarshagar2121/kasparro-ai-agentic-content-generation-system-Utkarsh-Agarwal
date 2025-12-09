# agents/logic_agent.py

class LogicAgent:
    """
    This agent produces structured content blocks using the product data.
    These blocks will later be used by template-building agents.
    """

    # Benefit block generator
    def generate_benefits_block(self, product):
        
        benefits = ", ".join(product["benefits"])
        return f"This serum provides the following benefits: {benefits}."

    # Usage instructions block
    def generate_usage_block(self, product):
        return f"How to use: {product['how_to_use']}."

    # Side effects block
    def generate_side_effects_block(self, product):
        return f"Possible side effects include: {product['side_effects']}."

    # Purchase block
    def generate_price_block(self, product):
        return f"The product is priced at {product['price']}."

    # Comparison block (vs fictional Product B)
    def generate_comparison_block(self, product):
        comparison_data = {
            "Product A": product["name"],
            "Product B": "RadiancePro Skin Serum",
            "Difference": "RadiancePro contains Niacinamide instead of Hyaluronic Acid and is more expensive."
        }
        return comparison_data
