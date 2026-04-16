#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, years: int):
        self.name = name
        self.height = float(height)
        self.years = years

    def show(self) -> str:
        return (f"{self.name.capitalize()}: {round(self.height, 1)}cm, "
                f"{self.years} days old")

    def growth(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.years += 1


def main() -> None:
    f1 = Plant("rose", 25, 30)
    f2 = Plant("oak", 200, 365)
    f3 = Plant("cactus", 5, 90)
    f4 = Plant("sunflower", 80, 45)
    f5 = Plant("fern", 15, 120)
    plants = [f1, f2, f3, f4, f5]

    print("=== Plant Factory Output ===")
    for n in plants:
        print("Create: " + n.show())


if __name__ == "__main__":
    main()
