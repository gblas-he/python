#!/usr/bin/python3.10

def main() -> None:
    print("=== Player Score Analytics ===")
    coordinate = input("Enter new coordinates as float in format 'x, y, z': ") 
    coordinate = coordinate.split(",")
    coordinate = float(coordinate)
    print(coordinate)


if __name__ == "__main__":
    main()