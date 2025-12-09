class ParserAgent:


    def parse(self, raw_data):
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
