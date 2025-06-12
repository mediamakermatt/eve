import requests
import json
import os

ESI_BASE = "https://esi.evetech.net/latest"
HEADERS = {"User-Agent": "EVE-Market-Helper"}

# Load static item data
ITEM_DATA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "item_setup", "fetch_item_data.json"))
with open(ITEM_DATA_FILE, encoding="utf-8") as f:
    ITEM_DATA = json.load(f)
NAME_TO_TYPE_ID = {item["typeName"].lower(): item["typeID"] for item in ITEM_DATA}

# Hardcoded region mapping (expand as needed)
REGION_NAME_TO_ID = {
    "the forge": 10000002,
    "domain": 10000043,
    "heimatar": 10000030,
    "metropolis": 10000042,
    "essence": 10000064,
    "sinq laison": 10000032,
    "derelik": 10000001
}

def resolve_type_id(item):
    if isinstance(item, int):
        return item
    return NAME_TO_TYPE_ID.get(item.lower())

def resolve_region_id(region):
    if isinstance(region, int):
        return region
    return REGION_NAME_TO_ID.get(region.lower())

def get_price_summary_by_region(item, region, top_n: int = 5):
    type_id = resolve_type_id(item)
    region_id = resolve_region_id(region)

    if type_id is None:
        raise ValueError(f"❌ Unknown item: {item}")
    if region_id is None:
        raise ValueError(f"❌ Unknown region: {region}")

    def fetch_orders(order_type):
        url = f"{ESI_BASE}/markets/{region_id}/orders/"
        params = {
            "order_type": order_type,
            "type_id": type_id,
            "page": 1
        }
        all_orders = []
        while True:
            resp = requests.get(url, headers=HEADERS, params=params)
            if resp.status_code != 200:
                break
            data = resp.json()
            if not data:
                break
            all_orders.extend(data)
            if 'x-pages' in resp.headers:
                if params["page"] >= int(resp.headers['x-pages']):
                    break
            params["page"] += 1
        return all_orders

    sell_orders = fetch_orders("sell")
    buy_orders = fetch_orders("buy")

    cheapest_sells = sorted(sell_orders, key=lambda x: x["price"])[:top_n]
    highest_buys = sorted(buy_orders, key=lambda x: x["price"], reverse=True)[:top_n]

    sell_avg = round(sum(o["price"] for o in cheapest_sells) / len(cheapest_sells), 2) if cheapest_sells else None
    buy_avg = round(sum(o["price"] for o in highest_buys) / len(highest_buys), 2) if highest_buys else None
    midpoint = round((sell_avg + buy_avg) / 2, 2) if sell_avg and buy_avg else None

    return {
        "type_id": type_id,
        "region_id": region_id,
        "sell_avg": sell_avg,
        "buy_avg": buy_avg,
        "midpoint": midpoint,
        "top_sell_orders": cheapest_sells,
        "top_buy_orders": highest_buys
    }

##########

# type_id = 34  # Tritanium
# region_id = 10000002  # The Forge

# use this in other places
# from helpers.get_price_data_by_region import get_price_summary_by_region

# n=5 is top 5 sell and top 5 buy orders so we can get an average
# summary = get_price_summary_by_region(type_id, region_id, top_n=5)
# summary = get_price_summary_by_region("Tritanium", "The Forge", top_n=5)

# print("📈 Market Summary:")
# print(summary)