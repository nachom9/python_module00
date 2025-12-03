def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """Print the inventory status of seeds depending on unit type.

    Args:
        seed_type (str): Type of seed (e.g., Rose, Sunflower).
        quantity (int): Amount of seeds.
        unit (str): Unit type, one of 'packets', 'grams', or 'area'.
    """
    print(seed_type, "seeds:", end=" ")
    print(quantity, end=" ")
    if unit == "packets":
        print("packets available")
    elif unit == "grams":
        print("grams total")
    elif unit == "area":
        print("square meters")
    else:
        print("Unknown unit type")
