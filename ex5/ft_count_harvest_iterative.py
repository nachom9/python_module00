def ft_count_harvest_iterative() -> None:
    """Count days iteratively until harvest and print each day."""
    days = int(input("Days until harvest: "))
    i = 1
    while i <= days:
        print("Day", i)
        i += 1
    print("Harvest time!")
