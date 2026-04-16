#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: float, years: int):
        self.name = name
        self.height = height
        self.years = years

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {round(self.height, 1)}cm, "
              f"{self.years} days old")
    
    def growth(self) -> None:
        self.height += 0.8
    
    def age(self) -> None:
        self.years += 1
        

def main() -> None:
    f1 = Plant("rose", 25.0, 30)
    i_height = f1.height

    print("=== Garden Plant Growth ===")
    f1.show()
    for n in range(1, 8):
        print(f"=== Day {n} ===")
        f1.growth()
        f1.age()
        f1.show()
    print(f"Growth this week: {round(f1.height - i_height, 2)}")


if __name__ == "__main__":
    main()
