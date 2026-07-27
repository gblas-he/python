#!/usr/bin/python3.10
import random


def gen_player_achievements(ach: list) -> set:
    num_ach = random.randint(1, len(ach))
    achievements = random.sample(ach, k = num_ach)
    return set(achievements)



def main() -> None:
    print("=== Achievement Tracker System ===\n")
    ACHIEVEMENT_POOL = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',
                        'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 
                        'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']
    print(f"Player Alice: {gen_player_achievements(ACHIEVEMENT_POOL)}")
    print(f"Player Bob: {gen_player_achievements(ACHIEVEMENT_POOL)}")
    print(f"Player Charlie: {gen_player_achievements(ACHIEVEMENT_POOL)}")
    print(f"Player Dylan: {gen_player_achievements(ACHIEVEMENT_POOL)}")
    print(f"All distinct achievements: ")
    print(f"Common achievements:: ")


if __name__ == "__main__":
    main()