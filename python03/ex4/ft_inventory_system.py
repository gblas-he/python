#!/usr/bin/python3.10
import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        try:
            parts: list[str] = arg.split(":")
            if len(parts) != 2 or parts[0] == "":
                print(f"Error - invalid parameter '{arg}'")
                continue
            elif parts[0] in inventory:
                print(f"Redundant item '{parts[0]}' - discarding")
                continue
            else:
                inventory[parts[0]] = int(parts[1])
        except ValueError as e:
            print(f"Quantity error for '{parts[0]}': {e}")
    print(f"Got inventory: {inventory}")
    items: list[str] = list(inventory.keys())
    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    print(f"Item list: {items}")
    for item, value in inventory.items():
        if total > 0:
            percent: float = round((value / total) * 100, 1)
        else:
            percent = 0.0
        print(f"Item {item} represents {percent}%")
    most: str = max(inventory, key=inventory.get)
    least: str = min(inventory, key=inventory.get)
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({"magic_item": 1})
    print(f"Update inventory: {inventory}")


if __name__ == "__main__":
    main()
