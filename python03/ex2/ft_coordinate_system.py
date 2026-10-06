import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw: str = input("Enter new coordinates as floats "
                         "in format 'x,y,z': ")
        parts: list[str] = raw.split(",")
        try:
            x_str, y_str, z_str = parts
        except ValueError:
            print("Invalid syntax")
            continue
        coords: list[float] = []
        valid: bool = True
        for part in (x_str, y_str, z_str):
            try:
                coords.append(float(part))
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                valid = False
                break
        if valid:
            return (coords[0], coords[1], coords[2])


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    center: float = math.sqrt(first[0]**2 + first[1]**2 + first[2]**2)
    print(f"Distance to center: {round(center, 4)}\n")
    print("Get a second set of coordinates")
    second: tuple[float, float, float] = get_player_pos()
    distance: float = math.sqrt((second[0] - first[0])**2
                                + (second[1] - first[1])**2
                                + (second[2] - first[2])**2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(distance, 4)}")


if __name__ == "__main__":
    main()
