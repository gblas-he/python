#!/usr/bin/python3.10

def garden_temperature(tem_str: str) -> int:
    tem_num = int(tem_str)
    if (tem_num < 0):
        raise Exception(f"Caught input_temperature error: {tem_num}°C "
                        f"is too cold for plants (min 0°C)")
    elif (tem_num > 40):
        raise Exception(f"Caught input_temperature error: {tem_num}°C "
                        f"is too hot for plants (max 40°C)")
    else:
        return tem_num


def garden_operation(operation_number) -> None:
    if 
    test_values = ['25', 'abc', '100', '-50']
    for value in test_values:
        print(f"Input data is '{value}'")
        try:
            tem = input_temperature(value)
            print(f"Temperature is now {tem}ºC")
        except ValueError as v:
            print(f"Caught input_temperature error: {v}")
        except Exception as e:
            print(f"{e}")
        print()


def main() -> None:
    print("=== Garden Temperature ===\n")
    garden_operation(0)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
