def ft_garden_summary() -> None:
    """Prompt for garden info and print a simple summary."""
    name = input("Enter garden name: ")
    number = input("Enter number of plants: ")
    print("Garden:", name)
    print("Plants:", number)
    print("Status: Growing well!")
