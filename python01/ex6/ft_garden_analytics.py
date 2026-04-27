class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self._height = float(height) if height >= 0 else 0.0
        self._age = age if age >= 0 else 0
        self._stats = self.Stats()

    def grow(self):
        self._stats._grow += 1
        self._height += 2.1

    def age(self):
        self._stats._age += 1
        self._age += 1

    def show(self):
        self._stats._show += 1
        return f"{self.name}: {round(self._height,1)}cm, {self._age} days old"

    def get_stats(self):
        return self._stats.display()

    @staticmethod
    def more_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0, 0)

    class Stats:
        def __init__(self):
            self._grow = 0
            self._age = 0
            self._show = 0

        def display(self):
            return f"Stats: {self._grow} grow, {self._age} age, {self._show} show"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def show(self):
        base = super().show()
        if self._bloomed:
            bloom = f"{self.name} is blooming beautifully!"
        else:
            bloom = f"{self.name} has not bloomed yet"
        return f"{base}\nColor: {self.color}\n{bloom}"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats = self.Stats()

    def produce_shade(self):
        self._stats._shade += 1
        return (f"Tree {self.name} now produces a shade of "
                f"{self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self):
        base = super().show()
        return f"{base}\nTrunk diameter: {self.trunk_diameter}cm"

    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade = 0

        def display(self):
            base = super().display()
            return f"{base}\n{self._shade} shade"


class Seed(Flower):
    def __init__(self, name, height, age, color, seeds):
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def bloom(self):
        super().bloom()
        self._seeds = 42

    def show(self):
        base = super().show()
        return f"{base}\nSeeds: {self._seeds}"


def display_stats(p: Plant):
    print(f"[statistics for {p.name}]")
    print(p.get_stats())


def main():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.more_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.more_year(400)}")

    print("\n=== Flower")
    rose = Flower("rose", 15, 10, "red")
    print(rose.show())
    display_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()

    print(rose.show())
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("oak", 200, 365, 5.0)
    print(oak.show())
    display_stats(oak)

    print("[asking the oak to produce shade]")
    print(oak.produce_shade())
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("sunflower", 80, 45, "yellow", 0)
    print(sunflower.show())

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()

    print(sunflower.show())
    display_stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.anonymous()
    print(anon.show())
    display_stats(anon)


if __name__ == "__main__":
    main()
