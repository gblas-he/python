def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    ft_recursive(days)
    print("Harvest Time!")


def ft_recursive(days: int) -> None:
    if days != 0:
        ft_recursive(days - 1)
        print(f"Day {days}")
