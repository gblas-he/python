import random

ACHIEVEMENT_POOL: list[str] = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer', 'Hidden Path Finder', 'Dragon Tamer', 'Night Owl',
    'Quest Master', 'Lucky Charm', 'Iron Will', 'Silent Shadow',
    'Gold Hoarder', 'Sky Walker', 'Deep Diver', 'Pixel Hunter',
    'Combo King', 'Flawless Victory', 'Fast Learner', 'Team Player',
    'Marathoner', 'Trailblazer',
]


def gen_player_achievements(pool: list[str]) -> set[str]:
    count: int = random.randint(10, 20)
    return set(random.sample(pool, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = gen_player_achievements(ACHIEVEMENT_POOL)
    bob: set[str] = gen_player_achievements(ACHIEVEMENT_POOL)
    charlie: set[str] = gen_player_achievements(ACHIEVEMENT_POOL)
    dylan: set[str] = gen_player_achievements(ACHIEVEMENT_POOL)
    everything: set[str] = set(ACHIEVEMENT_POOL)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    print(f"All distinct achievements: "
          f"{alice.union(bob, charlie, dylan)}\n")
    print(f"Common achievements: "
          f"{alice.intersection(bob, charlie, dylan)}\n")

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}\n")

    print(f"Alice is missing: {everything.difference(alice)}")
    print(f"Bob is missing: {everything.difference(bob)}")
    print(f"Charlie is missing: {everything.difference(charlie)}")
    print(f"Dylan is missing: {everything.difference(dylan)}")


if __name__ == "__main__":
    main()
