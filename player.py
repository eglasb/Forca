import random


class Player:
    def __init__(self, name) -> None:
        self.name: str = name
        self.lifes: int = 6
        # fmt: off
        self.letters: tuple = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                                "w", "x", "y", "z",)  # fmt: on
        self.played_letters: list = []
        self.chosen_letter: str = ""

    def __repr__(self) -> str:
        return f"Player: {self.name} has {self.lifes} lifes."

    def choose_letter(self) -> str:
        chosen_letter = input("Escolha uma letra: ").lower()
        while chosen_letter not in self.letters:
            print(f'Erro: entrada inválida "{chosen_letter}". Escolha uma letra: ')
            chosen_letter = input("Escolha uma letra: ").lower()
        return chosen_letter
