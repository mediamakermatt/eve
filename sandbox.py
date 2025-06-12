from helpers.get_price_data_by_region import get_price_summary_by_region

# Now you can call it
summary = get_price_summary_by_region("Tritanium", "The Forge", top_n=5)
print(summary)