import sys
import typing


def transform(content: str) -> str:
    result: str = ""
    for line in content.splitlines():
        result += line + "#\n"
    return result


def read_file(filename: str) -> str | None:
    print(f"Accessing file '{filename}'")
    file: typing.IO[str]
    try:
        file = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return None
    try:
        content: str = file.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error reading file '{filename}': {e}")
        return None
    finally:
        file.close()
    print("---\n")
    print(content, end="")
    if not content.endswith("\n"):
        print()
    print("\n---")
    print(f"File '{filename}' closed.")
    return content


def save_file(filename: str, content: str) -> None:
    print(f"Saving data to '{filename}'")
    file: typing.IO[str]
    try:
        file = open(filename, "w")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        print("Data not saved.")
        return
    try:
        file.write(content)
    except OSError as e:
        print(f"Error writing file '{filename}': {e}")
        print("Data not saved.")
        return
    finally:
        file.close()
    print(f"Data saved in file '{filename}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content: str | None = read_file(sys.argv[1])
    if content is None:
        return
    print("\nTransform data:")
    new_content: str = transform(content)
    print("---\n")
    print(new_content)
    print("---")
    new_name: str = input("Enter new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
    else:
        save_file(new_name, new_content)


if __name__ == "__main__":
    main()