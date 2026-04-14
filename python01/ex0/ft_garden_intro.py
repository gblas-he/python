#!/usr/bin/python3.10

def ft_garden_intro(name: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name.capitalize()}\nHeight: {height}cm"
          f"\nAge: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro("rose", 25, 30)
