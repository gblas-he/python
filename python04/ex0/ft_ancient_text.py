import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    file: typing.IO[str]
    try:
        file = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    try:
        content: str = file.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error reading file '{filename}': {e}")
        return
    finally:
        file.close()
    print("---\n")
    print(content, end="")
    if not content.endswith("\n"):
        print()
    print("\n---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
