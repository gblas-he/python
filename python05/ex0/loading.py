import importlib
import importlib.metadata

REAGENTS: list[tuple[str, str]] = [
    ("pandas", "Data manipulation ready"),
    ("numpy", "Numerical computation ready"),
]


def is_available(name: str) -> bool:
    try:
        importlib.import_module(name)
    except ImportError:
        return False
    return True


def get_version(name: str) -> str:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


def print_install_help(missing: list[str]) -> None:
    names = " ".join(missing)
    print()
    print("Missing reagents! Install them with:")
    print("  pip:    pip install -r ex0/requirements.txt")
    print(f"  Poetry: poetry add {names}")
    print("          (or `poetry install` to use pyproject.toml)")


def print_comparison() -> None:
    print()
    print("pip vs Poetry:")
    print("  requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("  pyproject.toml declares the same constraints, "
          "and Poetry pins the resolved")
    print("  versions in poetry.lock so every install is identical.")


def main() -> None:
    print()
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")

    missing: list[str] = []
    for name, description in REAGENTS:
        if is_available(name):
            print(f"[OK] {name} ({get_version(name)}) - {description}")
        else:
            print(f"[MISSING] {name} - not installed")
            missing.append(name)

    if missing:
        print_install_help(missing)
    print_comparison()

    if not missing:
        print()
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
