#!/usr/bin/python3.10
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as float in format "
                    "'x, y, z': ")  # Obtemos un string
        c = raw.split(",")
        # el string se vuelve tipo list, con elementos string, con split
        if len(c) != 3:
            print("Invalid syntax")
            continue
        error = False
        float_c = []
        for i in c:
            # float() no sabe convertir una lista es necesario un bucle
            try:
                float_c.append(float(i))
            # Convertimos cada elemento en float y lo introducimos en la lista
            except ValueError as e:
                print(f"Error on parameter '{i}': {e}")
                error = True
        if error:
            continue
        return (float_c[0], float_c[1], float_c[2])


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    tupla_c1 = get_player_pos()
    print(f"Got a first tuple: {tupla_c1}")
    print(f"It includes: X={tupla_c1[0]}, Y={tupla_c1[1]}, "
          f"Z={tupla_c1[2]}")
    center = math.sqrt((tupla_c1[0]**2) + (tupla_c1[1]**2)
                       + (tupla_c1[2]**2))
    print(f"Distance to center: {round(center, 4)}\n")
    print("Get a second set of coordinates")
    tupla_c2 = get_player_pos()
    distance = math.sqrt((tupla_c1[0] - tupla_c2[0])**2
                         + (tupla_c1[1] - tupla_c2[1])**2
                         + (tupla_c1[2] - tupla_c2[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()
