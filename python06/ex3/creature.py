from abc import ABC, abstractmethod


class Creature(ABC):
	def __init__(self, name: str, creature_type: str) -> None:
		self.name: str = name
		self.type: str = creature_type

	@abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flamelin(Creature):
	def __init__(self) -> None:
		super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class TransformCapability(ABC):
    def __init__(self) -> None: