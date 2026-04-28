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

    def grow(self) -> None:
        self._height += 2.1

    def age(self) -> None:
        self._ages += 1


class Flower(Plant):
    def __init__(self, name: str, height: int, ages: int, color: str):
        super().__init__(name, height, ages)
        self.color = color
        self.is_bloomed = False

    def bloom(self) -> None:
        self.is_bloomed = True

    def show(self):
        print(super().show())
        print(f"Color: {self.color}")
        if self.is_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self):
        print(super().show())
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self):
        super().grow()
        self.nutritional_value += 1

    def age(self):
        super().age()
        self.nutritional_value += 1

    def show(self):
        print(super().show())
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("oak", 200, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("tomato", 5, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()


if __name__ == "__main__":
    main()
