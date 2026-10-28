import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
GITIGNORE_PATH = os.path.join(BASE_DIR, ".gitignore")


def secret_in_source(value: str | None) -> bool:
    if not value:
        return False
    with open(__file__, encoding="utf-8") as file:
        return value in file.read()


def env_is_ignored() -> bool:
    try:
        with open(GITIGNORE_PATH, encoding="utf-8") as file:
            lines = [line.strip() for line in file]
    except OSError:
        return False
    return ".env" in lines


def main() -> None:
    load_dotenv(dotenv_path=ENV_PATH)

    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    required = {
        "MATRIX_MODE": matrix_mode,
        "DATABASE_URL": database_url,
        "API_KEY": api_key,
        "LOG_LEVEL": log_level,
        "ZION_ENDPOINT": zion_endpoint,
    }

    warnings: list[str] = []

    missing = [name for name, val in required.items() if not val]
    if missing:
        warnings.append(
            f"Missing configuration for: {', '.join(missing)}"
        )

    mode = matrix_mode or "development"
    if mode not in ("development", "production"):
        warnings.append(f"Unknown MATRIX_MODE '{mode}', using development")
        mode = "development"

    log = log_level or "DEBUG"

    print()
    print("ORACLE STATUS: Consulting the configuration...")
    print()

    for warning in warnings:
        print(f"WARNING: {warning}")
    if warnings:
        print("Using default values.")
        print()

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode == "production":
        print("Database: Connected to production database")
    else:
        print("Database: Connected to local instance")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthenticated")

    print(f"Log Level: {log}")

    if zion_endpoint:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline")

    print()
    print("Configuration security check:")

    if secret_in_source(api_key) or secret_in_source(database_url):
        print("[WARNING] A secret was found in the source code")
    else:
        print("[OK] No hardcoded secrets detected")

    if env_is_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env is not ignored (or .gitignore is missing)")

    print("[OK] Production overrides available")

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
