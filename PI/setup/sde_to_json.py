import pandas as pd
import os
import json

# Always resolve from this script's location
CSV_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sde_csv"))
print("✅ Resolved CSV_DIR:", CSV_DIR)

# Load required CSV files
inv_types = pd.read_csv(os.path.join(CSV_DIR, "invTypes.csv"))
dgm_type_attributes = pd.read_csv(os.path.join(CSV_DIR, "dgmTypeAttributes.csv"))
dgm_attribute_types = pd.read_csv(os.path.join(CSV_DIR, "dgmAttributeTypes.csv"))
dgm_type_effects = pd.read_csv(os.path.join(CSV_DIR, "dgmTypeEffects.csv"))
dgm_effects = pd.read_csv(os.path.join(CSV_DIR, "dgmEffects.csv"))
inv_groups = pd.read_csv(os.path.join(CSV_DIR, "invGroups.csv"))
inv_categories = pd.read_csv(os.path.join(CSV_DIR, "invCategories.csv"))
inv_market_groups = pd.read_csv(os.path.join(CSV_DIR, "invMarketGroups.csv"), low_memory=False)

# Merge group and category names
inv_types = inv_types.merge(inv_groups[['groupID', 'groupName', 'categoryID']], on='groupID', how='left')
inv_types = inv_types.merge(inv_categories[['categoryID', 'categoryName']], on='categoryID', how='left')
inv_types = inv_types.merge(inv_market_groups[['marketGroupID', 'marketGroupName']], on='marketGroupID', how='left')

# Prepare attribute and effect dictionaries
attr_name_map = dict(zip(dgm_attribute_types['attributeID'], dgm_attribute_types['attributeName']))
effect_name_map = dict(zip(dgm_effects['effectID'], dgm_effects['effectName']))

# Group attributes and effects by typeID
grouped_attrs = dgm_type_attributes.groupby('typeID')
grouped_effects = dgm_type_effects.groupby('typeID')

# Build full item data
all_items = []
for _, row in inv_types.iterrows():
    type_id = row['typeID']
    item_data = {
        "typeID": int(type_id),
        "typeName": row.get("typeName", ""),
        "description": row.get("description", ""),
        "groupID": int(row.get("groupID", 0)),
        "groupName": row.get("groupName", ""),
        "categoryID": int(row.get("categoryID", 0)),
        "categoryName": row.get("categoryName", ""),
        "marketGroupID": int(row.get("marketGroupID", 0)) if not pd.isna(row.get("marketGroupID")) else None,
        "marketGroupName": row.get("marketGroupName", None),
        "mass": row.get("mass", None),
        "volume": row.get("volume", None),
        "capacity": row.get("capacity", None),
        "attributes": {},
        "effects": []
    }

    if type_id in grouped_attrs.groups:
        attrs = grouped_attrs.get_group(type_id)
        for _, attr_row in attrs.iterrows():
            attr_id = attr_row['attributeID']
            attr_name = attr_name_map.get(attr_id, f"attr_{attr_id}")
            value = attr_row.get('valueFloat') or attr_row.get('valueInt')
            item_data["attributes"][attr_name] = value


    if type_id in grouped_effects.groups:
        effects = grouped_effects.get_group(type_id)
        item_data["effects"] = [effect_name_map.get(eid, f"effect_{eid}") for eid in effects['effectID']]

    all_items.append(item_data)

# Save to JSON
output_path = "PI/setup/fetch_item_data.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_items, f, indent=2)