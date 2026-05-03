#!/usr/bin/python3.10

class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


def test_garden_error() -> None:
    try:
        print("Testing PlantError...")
        raise PlantError()
    except PlantError as p:
        print(f"Caught PlantError: {p}")
    try:
        print("\nTesting WaterError......")
        raise WaterError()
    except WaterError as w:
        print(f"Caught WaterError: {w}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as g:
        print(f"Caught GardenError: {g}")
    try:
        raise WaterError()
    except GardenError as g:
        print(f"Caught GardenError: {g}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    test_garden_error()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
