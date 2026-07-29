#!/usr/bin/python3.10
import random


def gen_player_achievements(ach: list) -> set:
    num_ach = random.randint(1, len(ach))
    achievements = random.sample(ach, k=num_ach)
    return set(achievements)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    
    ACHIEVEMENT_POOL = ['Crafting Genius', 'Strategist', 'World Savior',
                        'Speed Runner', 'Survivor', 'Master Explorer',
                        'Treasure Hunter', 'Unstoppable', 'First Steps',
                        'Collector Supreme', 'Untouchable', 'Sharp Mind',
                        'Boss Slayer']
    
    p1 = gen_player_achievements(ACHIEVEMENT_POOL)
    p2 = gen_player_achievements(ACHIEVEMENT_POOL)
    p3 = gen_player_achievements(ACHIEVEMENT_POOL)
    p4 = gen_player_achievements(ACHIEVEMENT_POOL)
    ach_set = set(ACHIEVEMENT_POOL)

    print(f"Player Alice: {p1}")
    print(f"Player Bob: {p2}")
    print(f"Player Charlie: {p3}")
    print(f"Player Dylan: {p4}\n")
    print(f"All distinct achievements: {p1.union(p2, p3, p4)}\n")
    print(f"Common achievements: {p1.intersection(p2, p3, p4)}\n")
    print(f"Only Alice has: {p1.difference(p2, p3, p4)}")
    print(f"Only Bob has: {p2.difference(p1, p3, p4)}")
    print(f"Only Charlie has: {p3.difference(p1, p2, p4)}")
    print(f"Only Dylan has: {p4.difference(p1, p2, p3)}\n")
    print(f"Alice is missing: {ach_set.difference(p1)}")
    print(f"Bob is missing: {ach_set.difference(p2)}")
    print(f"Charlie is missing: {ach_set.difference(p3)}")
    print(f"Dylan is missing: {ach_set.difference(p4)}")


if __name__ == "__main__":
    main()
