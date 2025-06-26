class Animal:
    alive = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def _check_if_alive(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    @staticmethod
    def print_alive() -> None:
        result = []
        for animal in Animal.alive:
            result.append(
                f"{{Name: {animal.name}, Health: {animal.health}, Hidden: {animal.hidden}}}"
            )
        print(result)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victim: Animal) -> None:
        if not isinstance(victim, Herbivore):
            return
        if victim.hidden:
            return
        victim.health -= 50
        victim._check_if_alive()
