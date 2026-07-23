#!/usr/bin/python3.10
import math


def get_player_pos() -> tuple(float, float, float):
    c = input("Enter new coordinates as float in format "
               "'x, y, z': ")  # Obtemos un string
    c = c.split(",")  # el string se vuelve tipo list,
    # con elementos string, con split
    float_c = []
    for i in c:  # float() no sabe convertir una lista es
        # necesario un bucle
        float_c.append(float(i))  # Convertimos cada elemento en
        # float y lo introducimos en la lista
    tupla_c = tuple(float_c)
    print(f"Got a first tuple: {tupla_c}")
    print(f"It includes: X={tupla_c[0]}, Y={tupla_c[1]}, "
          f" Z={tupla_c[2]}")
    center = math.sqrt((tupla_c[0]**2) + (tupla_c[1]**2)
                       + (tupla_c[2]**2))
    print(f"Distance to center: {center}")


def main() -> None:
    print("=== Game Coordinate System ===")
    c1 = input("Enter new coordinates as float in format "
               "'x, y, z': ")  # Obtemos un string
    c1 = c1.split(",")  # el string se vuelve tipo list,
    # con elementos string, con split
    float_c1 = []
    for i in c1:  # float() no sabe convertir una lista es
        # necesario un bucle
        float_c1.append(float(i))  # Convertimos cada elemento en
        # float y lo introducimos en la lista
    tupla_c1 = tuple(float_c1)
    print(f"Got a first tuple: {tupla_c1}")
    print(f"It includes: X={tupla_c1[0]}, Y={tupla_c1[1]}, "
          f" Z={tupla_c1[2]}")
    center = math.sqrt((tupla_c1[0]**2) + (tupla_c1[1]**2)
                       + (tupla_c1[2]**2))
    print(f"Distance to center: {center}")

    c2 = input("Enter new coordinates as float in format "
               "'x, y, z': ")  # Obtemos un string
    c2 = c2.split(",")  # el string se vuelve tipo list,
    # con elementos string, con split
    float_c2 = []
    for i in c2:  # float() no sabe convertir una lista es
        # necesario un bucle
        float_c2.append(float(i))  # Convertimos cada elemento en
        # float y lo introducimos en la lista
    tupla_c2 = tuple(float_c2)
    print(f"Got a second tuple: {tupla_c2}")
    print(f"It includes: X={tupla_c2[0]}, Y={tupla_c2[1]}, "
          f" Z={tupla_c2[2]}")
    center = math.sqrt((tupla_c2[0]**2) + (tupla_c2[1]**2)
                       + (tupla_c2[2]**2))
    print(f"Distance to center: {center}")
    distance = math.sqrt((tupla_c2[0] - tupla_c1[0])**2
                         + (tupla_c2[1] - tupla_c1[1])**2
                         + (tupla_c2[2] - tupla_c1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    main()
