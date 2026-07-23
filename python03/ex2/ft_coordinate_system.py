#!/usr/bin/python3.10

def main() -> None:
    print("=== Player Score Analytics ===")
    coordinate = input("Enter new coordinates as float in format 'x, y, z': ") # Obtemos un string
    coordinate = coordinate.split(",") # el string se vuelve tipo list, con elementos string, con split
    float_coordinate = []
    for i in coordinate: # float() no sabe convertir una lista es necesario un bucle
        float_coordinate.append(float(i)) # Convertimos cada elemento en float y lo introducimos en la lista
    tupla_coordinate = tuple(float_coordinate)
    print(f"Got a first tuple: {tupla_coordinate}")
    print(f"It includes: X={tupla_coordinate[0]}, Y={tupla_coordinate[1]}, Z={tupla_coordinate[2]}")
    # print(f"Distance to center: {tupla_coordinate}")


if __name__ == "__main__":
    main()