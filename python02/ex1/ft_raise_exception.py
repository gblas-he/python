#!/usr/bin/python3.10

def input_temperature(tem_str: str) -> int:
    tem_num = int(tem_str)
    if (tem_num <= 0):
        raise Exception(f"Caught input_temperature error: {tem_num}°C "
                        f"is too cold for plants (min {tem_num}°C)")
    elif (tem_num >= 40):
        raise Exception(f"Caught input_temperature error: {tem_num}°C "
                        f"is too hot for plants (min {tem_num}°C)")



    if (tem_num >= 0 and tem_num <= 40):
        return tem_num
    raise Exception(f"Caught input_temperature error: {tem_num}°C is too cold "
                    f"for plants (min {tem_num}°C)")


def test_temperature() -> None:
    test_values = ['25', 'abc', '100', '50']
    for value in test_values:
        try:
            tem = input_temperature(value)
            print(f"Input data is '{value}'")
            print(f"Temperature is now {tem}ºC")
        except ValueError as v:
            print(f"Input data is '{value}'")
            print(f"Caught input_temperature error: {v}")
        except Exception as e:
            print(f"{e}")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
