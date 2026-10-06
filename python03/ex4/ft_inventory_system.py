import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts: list[str] = arg.split(":")
        if len(parts) != 2 or parts[0] == "":
            print(f"Error - invalid parameter '{arg}'")
            continue
        if parts[0] in inventory:
            print(f"Redundant item '{parts[0]}' - discarding")
            continue
        try:
            inventory[parts[0]] = int(parts[1])
        except ValueError as e:
            print(f"Quantity error for '{parts[0]}': {e}")
    print(f"Got inventory: {inventory}")
    items: list[str] = list(inventory.keys())
    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    print(f"Item list: {items}")
    for item in inventory.keys():
        value: int = inventory[item]
        if total > 0:
            percent: float = round((value / total) * 100, 1)
        else:
            percent = 0.0
        print(f"Item {item} represents {percent}%")
    if inventory:
        most: str = items[0]
        least: str = items[0]
        for item in items:
            if inventory[item] > inventory[most]:
                most = item
            if inventory[item] < inventory[least]:
                least = item
        print(f"Item most abundant: {most} with quantity {inventory[most]}")
        print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
