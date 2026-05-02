#!/usr/bin/python3.10

def garden_operation(operation_number) -> None:
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        (5/0)
    elif (operation_number == 2):
        open('/non/existent/file')
    elif (operation_number == 3):
        print("hello" + 4)
    else:
        return


def test_error_types() -> None:
    for num in range(5):
        print(f"Testing operation {num}...")
        try:
            garden_operation(num)
        except ValueError as v:
            print(f"Caught ValueError: {v}")
        except ZeroDivisionError as z:
            print(f"Caught ZeroDivisionError: {z}")
        except FileNotFoundError as f:
            print(f"Caught FileNotFoundError: {f}")
        except TypeError as t:
            print(f"Caught TypeError: {t}")
    print("Operation completed successfully")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
