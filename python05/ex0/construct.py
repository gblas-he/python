import os
import site
import sys


def is_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if is_venv():
        env_path = sys.prefix
        env_name = os.path.basename(env_path)
        site_packages = site.getsitepackages()[0]

        print()
        print("LABORATORY STATUS: The laboratory is sealed")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print()
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print()
        print("Reagent installation path:")
        print(site_packages)
    else:
        print()
        print("LABORATORY STATUS: You are working in the open")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print()
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate  # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
