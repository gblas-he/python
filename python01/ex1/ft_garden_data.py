#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age} days old")


def main() -> None:
    f1 = Plant("rose", 25, 30)
    f2 = Plant("sunflower", 80, 45)
    f3 = Plant("cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    f1.show()
    f2.show()
    f3.show()


if __name__ == "__main__":
    main()
