# agents/parser_agent.py

class ParserAgent:
    """
    This agent is responsible for converting raw product data
    into a structured internal model that will be easier for
    other agents to process.
    """

    def parse(self, raw_data):
        # Convert comma-separated fields into lists
        structured_data = {
            "name": raw_data.get("Product Name", ""),
            "concentration": raw_data.get("Concentration", ""),
            "skin_type": [item.strip() for item in raw_data.get("Skin Type", "").split(",")],
            "key_ingredients": [item.strip() for item in raw_data.get("Key Ingredients", "").split(",")],
            "benefits": [item.strip() for item in raw_data.get("Benefits", "").split(",")],
            "how_to_use": raw_data.get("How to Use", ""),
            "side_effects": raw_data.get("Side Effects", ""),
            "price": raw_data.get("Price", "")
        }

        return structured_data
