#!/usr/bin/python3.10

def input_temperature(tem_str: str) -> int:
    tem_num = int(tem_str)
    if (tem_num >= 0 and tem_num <= 40):
        try:
            return tem_num
        except Exception as e:
            print(f"Caught input_temperature error: {e}")


def test_temperature() -> None:
    test_values = ['25', 'abc', '100', '50']
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
