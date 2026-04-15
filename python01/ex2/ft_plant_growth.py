#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, years: int):
        self.name = name
        self.height = height
        self.years = years

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.years} days old")
    
    def growth(self) -> None:
        self.height += 0.8
    
    def age(self) -> None:
        self.years += 1
        

def main() -> None:
    f1 = Plant("rose", 25, 30)
    # f2 = Plant("sunflower", 80, 45)
    # f3 = Plant("cactus", 15, 120)
    # i_height = f1.height

    print("=== Garden Plant Growth ===")
    for n in range(7):
        print(f"=== Day{n} ===")
        f1.show()
        f1.growth()
        f1.age()
    # f_height -= i_height
    # print(f"Growth this week: {f_height}cm")


if __name__ == "__main__":
    main()
