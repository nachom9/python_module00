def ft_plant_age() -> None:
    """Check the age of a plant and print if it's ready to harvest."""
    plant_age = int(input("Enter plant age in days: "))
    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
