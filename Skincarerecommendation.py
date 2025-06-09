# Simple autocomplete and category lookup program

categories = {
    "moisturizers": {
        "description": "Hydrating products that lock in moisture and improve skin barrier function.",
        "sample_products": ["HydraPlus Cream", "AquaBoost Lotion"]
    },
    "cleansers": {
        "description": "Products designed to gently remove dirt, oil, and makeup from the skin.",
        "sample_products": ["PureFoam Cleanser", "GentleWash Gel"]
    },
    "serums": {
        "description": "Concentrated formulas targeting specific skin concerns like dullness or fine lines.",
        "sample_products": ["Brightening Serum", "Age-Defy Concentrate"]
    },
    "sunscreens": {
        "description": "Products that protect skin from harmful UV radiation.",
        "sample_products": ["Daily SPF 50", "UltraShield Sunscreen"]
    },
    "exfoliants": {
        "description": "Chemical or physical treatments that remove dead skin cells.",
        "sample_products": ["SoftScrub Exfoliant", "AHA Renewal Pads"]
    },
    "toners": {
        "description": "Water-based formulas used after cleansing to refine pores and balance skin.",
        "sample_products": ["FreshTone Mist", "Clarifying Toner"]
    },
    "masks": {
        "description": "Treatments left on the skin for a period to deliver intensive benefits.",
        "sample_products": ["Hydrating Sheet Mask", "Clay Detox Mask"]
    },
    "eye creams": {
        "description": "Creams formulated specifically for the delicate eye area.",
        "sample_products": ["Revive Eye Gel", "Anti-Puff Eye Cream"]
    },
    "lip care": {
        "description": "Balms and treatments that nourish and protect lips.",
        "sample_products": ["SmoothLip Balm", "Night Repair Lip Mask"]
    },
    "acne treatments": {
        "description": "Products containing active ingredients to reduce and prevent acne.",
        "sample_products": ["ClearSpot Gel", "BHA Acne Solution"]
    }
}


def autocomplete(prefix):
    """Return list of categories that start with the given prefix (case-insensitive)."""
    prefix = prefix.lower()
    return [name for name in categories.keys() if name.startswith(prefix)]


def show_category_data(category):
    """Display information for the selected category if it exists."""
    data = categories.get(category.lower())
    if not data:
        print(f"No data found for category '{category}'.")
        return
    print(f"\nCategory: {category.title()}")
    print(f"Description: {data['description']}")
    print("Sample products:")
    for product in data["sample_products"]:
        print(f"  - {product}")
    print()


def main():
    print("Welcome to the skincare category lookup!")
    while True:
        prefix = input("\nEnter a search term (or 'quit' to exit): ")
        if prefix.lower() == "quit":
            break
        matches = autocomplete(prefix)
        if not matches:
            print("No categories match your search.")
            continue
        print("Matches: " + ", ".join(matches))
        selected = input("Select a category from the matches: ")
        show_category_data(selected)


if __name__ == "__main__":
    main()
