#!/usr/bin/python3.10

def input_temperature(tem_str: str) -> int:
    return int(tem_str)


def test_temperature() -> None:
    test_values = ['25', 'abc']
    for value in test_values:
        try:
            tem = input_temperature(value)
            print(f"Input data is '{value}'")
            print(f"Temperature is now {tem}ºC")
        except ValueError as e:
            print(f"Input data is '{value}'")
            print(f"Caught input_temperature error: {e}")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
