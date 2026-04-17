#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        if height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)
        if age < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def show(self) -> str:
        return (f"{self.name.capitalize()}: {round(self._height, 1)}cm, "
                f"{self._age} days old")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height):
        if height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height updated rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age):
        if age < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age updated rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")


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
