import random


class Player:
    def __init__(self, name) -> None:
        self.name: str = name
        self.lifes: int = 6
        # fmt: off
        self.letters: tuple = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                                "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                                "W", "X", "Y", "Z")  # fmt: on
        self.played_letters: list = []
        self.chosen_letter: str = ""
        self.alive: bool = True

    def __repr__(self) -> str:
        return f"Player: {self.name} has {self.lifes} lifes."

    def choose_letter(self) -> str:
        chosen_letter = input("Escolha uma letra: ").upper().strip()
        while True:
            if chosen_letter in self.played_letters:
                print(f'Você já tentou a letra "{chosen_letter}"!')
                chosen_letter = input("Escolha outra letra: ").upper().strip()
            elif chosen_letter not in self.letters:
                print(f'Entrada inválida "{chosen_letter}"!')
                chosen_letter = input("Escolha uma letra: ").upper().strip()
            elif (
                chosen_letter not in self.played_letters
                and chosen_letter in self.letters
            ):
                self.played_letters.append(chosen_letter)
                return chosen_letter

    def loose_life(self):
        self.lifes -= 1
        if self.lifes == 0:
            self.alive = False
