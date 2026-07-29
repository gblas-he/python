#!/usr/bin/python3.10
import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {}
    for i in sys.argv[1:]:   # bucle convertir los argumento en diccionario
        try:
            partes = i.split(":")
            if len(partes) != 2:
                print(f"Error - invalid parameter '{i}'")
                continue
            elif partes[0] in inventory:
                    print(f"Redundant item '{partes[0]}' - discarding")
            else:
                inventory[partes[0]] = int(partes[1])  # Añadir un elemento a un diccionario
        except ValueError as e:
            print(f"Quantity error for '{partes[0]}': {e}")
    print(f"Got inventory: {inventory}")
         


if __name__ == "__main__":
    main()