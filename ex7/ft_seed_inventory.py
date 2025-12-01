def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
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
