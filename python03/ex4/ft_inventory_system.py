#!/usr/bin/python3.10
import sys


def gen_player_achievements(ach: list) -> set:


def main() -> None:
    print("=== Inventory System Analysis ===\n")
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:   # bucle convertir los argumento en int
            try:
                partes = i.split(":")
                if len(partes) != 2:
                    print("Error - ivalid parameter '{i}'")
                    continue
                else:
                    inventory.append(int(i))  # Añadir un elemento a una lista
                # int(i) son cada argumento ya que sys.argv[i] es una lista
            except ValueError:
                print(f"Invalid parameter: '{i}'")


if __name__ == "__main__":
    main()