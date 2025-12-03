def ft_water_reminder() -> None:
    """Check if plants need watering and print a reminder."""
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine.")
