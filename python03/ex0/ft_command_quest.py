#!/usr/bin/python3.10

def input_temperature(tem_str: str) -> int:
    return int(tem_str)


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()