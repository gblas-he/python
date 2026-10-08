import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {players}")
    players_capitalized: list[str] = [
        player.capitalize() for player in players
    ]
    print(f"New list with all names capitalized: {players_capitalized}")
    capitalized_only: list[str] = [
        player for player in players if player[0].isupper()
    ]
    print(f"New list of capitalized names only: {capitalized_only}")
    scores: dict[str, int] = {
        player: random.randint(50, 1000) for player in players_capitalized
    }
    print(f"\nScore dict: {scores}")
    avg_score: float = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg_score, 2)}")
    high_scores: dict[str, int] = {
        player: score for player, score in scores.items()
        if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
