import json
import os

ITEMS_JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "item_setup", "fetch_item_data.json"))

with open(ITEMS_JSON_PATH, "r", encoding="utf-8") as f:
    ALL_ITEMS = json.load(f)

# Correctly build name-to-item dictionary
NAME_TO_ITEM = {item["typeName"].strip().lower(): item for item in ALL_ITEMS if "typeName" in item}

def get_item_data(name_or_id):
    if isinstance(name_or_id, set):
        name_or_id = next(iter(name_or_id))

    if isinstance(name_or_id, int):
        for item in ALL_ITEMS:
            if item.get("typeID") == name_or_id:
                return item
        print(f"⚠️ No item found with typeID: {name_or_id}")
        return None

    elif isinstance(name_or_id, str):
        key = name_or_id.strip().lower()
        result = NAME_TO_ITEM.get(key)
        if result is None:
            print(f"❌ Item not found: {name_or_id}")
        return result

    else:
        raise ValueError(f"🚫 Invalid input type for item lookup: {type(name_or_id)}")
