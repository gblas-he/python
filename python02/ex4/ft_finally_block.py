#!/usr/bin/python3.10

class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if (plant_name == plant_name.capitalize()):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as p:
        print(f"Caught PlantError: {p}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    test_plants1 = ['Tomato', 'Lettuce', 'Carrots']
    test_plants2 = ['Tomato', 'lettuce']
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    test_watering_system(test_plants1)
    print("\nTesting invalid plants...")
    test_watering_system(test_plants2)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
