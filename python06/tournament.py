from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)


def run_tournament(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> None:
    entries = [(factory.create_base(), strat) for factory, strat in opponents]
    roster = ", ".join(
        f"({creature.name}+{strat.name})" for creature, strat in entries
    )
    print(f"[ {roster} ]")
    print("*** Tournament ***")
    print(f"{len(entries)} opponents involved")

    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            c1, s1 = entries[i]
            c2, s2 = entries[j]
            print("\n* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")
            try:
                s1.act(c1)
                s2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()
    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()

    print("Tournament 0 (basic)")
    run_tournament(
        [
            (flame_factory, normal_strat),
            (transform_factory, aggressive_strat),
        ]
    )

    print("\nTournament 1 (error)")
    run_tournament(
        [
            (transform_factory, aggressive_strat),
            (flame_factory, aggressive_strat),
        ]
    )


if __name__ == "__main__":
    main()
