#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, ages: int):
        self.name = name.capitalize()
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)
        if ages < 0:
            print(f"{self.name}: Error, age can't be negative")
            self._ages = 0
        else:
            self._ages = ages

    def show(self) -> str:
        return (f"{self.name}: {round(self._height, 1)}cm, "
                f"{self._ages} days old")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._ages

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height updated rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {height}cm")

    def set_age(self, ages):
        if ages < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age updated rejected")
        else:
            self._ages = ages
            print(f"Age updated: {ages} days")

    def growth(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.ages += 1

class Flower(Plant):
    def __init__(self, name: str, height: int, ages: int, color: str):
        super().__init__(name, height, ages)
        self.color = color
    
    def bloom(self):
        


def main() -> None:
    print("=== Garden Security System ===")

    f1 = Plant("rose", 15, 10)
    print("Plant created: " + f1.show())

    f1.set_height(25)
    f1.set_age(30)

    f1.set_height(-25)
    f1.set_age(-30)

    print("Current state: " + f1.show())


if __name__ == "__main__":
    main()
