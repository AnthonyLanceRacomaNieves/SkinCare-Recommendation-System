"""Demo script for looking up skincare categories.

This script provides a small command line interface that lets the user type a prefix, see autocomplete suggestions, and view details about a category. It demonstrates a simple use of Python data structures and binary search for efficient prefix matching.
"""

from bisect import bisect_left, bisect_right

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

categories = {
    "moisturizers": {
        "description": "Products that hydrate the skin.",
        "sample_products": [
            "E45 Moisturising Cream 500g",
            "Dermal Therapy Very Dry Skin Cream 125g",
        ],
    },
    "serums": {
        "description": "Concentrated active treatments.",
        "sample_products": [
            "Vinopure Blemish Control Infusion Serum",
            "Boost Lab Vitamin C Brightening Serum",
        ],
    },
    "cleansers": {
        "description": "Formulas that remove dirt and makeup.",
        "sample_products": [
            "Fresh Start Gel Cleanser",
        ],
    },
    "sunscreens": {
        "description": "SPF protection products.",
        "sample_products": [
            "Supreme Screen SPF 50+ Hydrating SKINSCREEN",
        ],
    },
}

# Prepare a sorted list of keys for efficient prefix look‑up
category_names = sorted(categories.keys())

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def autocomplete(prefix: str):
    """Return a list of category names that start with the given prefix (case‑insensitive)."""
    prefix = prefix.lower()
    start = bisect_left(category_names, prefix)
    end = bisect_right(category_names, prefix + "\uffff")  # high Unicode char → end of range
    return category_names[start:end]

def show_category_data(category: str):
    """Pretty‑print information about a category if it exists."""
    data = categories.get(category.lower())
    if not data:
        print(f"No data found for category '{category}'.")
        return

    print(f"\nCategory: {category.title()}")
    print(f"Description: {data['description']}")
    print("Sample products:")
    for product in data["sample_products"]:
        print(f"  – {product}")
    print()

# -----------------------------------------------------------------------------
# CLI entry point
# -----------------------------------------------------------------------------

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
