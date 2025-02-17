class Player:
    def __init__(self, name) -> None:
        self.name: str = name
        self.lifes: int = 6
        self.letters: tuple = ()
        self.played_letters: list = []
        self.chosen_letter: str = ""

    def __repr__(self) -> str:
        return f"Player: {self.name} has {self.lifes} lifes."
