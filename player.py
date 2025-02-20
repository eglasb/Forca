from utils import remove_accents


class Player:
    # fmt: off
    LETTERS: tuple[str, ...] = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                                "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                                "W", "X", "Y", "Z") 
    # fmt: on
    def __init__(self, name) -> None:
        self.name: str = name
        self.lives: int = 6
        self.played_letters: list[str] = []
        self.chosen_letter: str = ""
        self.alive: bool = True

    def __repr__(self) -> str:
        return f"Player: {self.name} has {self.lives} lifes."

    def choose_letter(self) -> str:
        chosen_letter = remove_accents(input("Escolha uma letra: ").upper().strip())
        while True:
            if chosen_letter in self.played_letters:
                print(f'Você já tentou a letra "{chosen_letter}"!')
                chosen_letter = input("Escolha outra letra: ").upper().strip()
            elif chosen_letter not in Player.LETTERS:
                print(f'Entrada inválida "{chosen_letter}"!')
                chosen_letter = input("Escolha uma letra: ").upper().strip()
            elif (
                chosen_letter not in self.played_letters
                and chosen_letter in Player.LETTERS
            ):
                self.played_letters.append(chosen_letter)
                return chosen_letter

    def lose_life(self):
        self.lives -= 1
        if self.lives == 0:
            self.alive = False

    def reset_state(self):
        self.lives = 6
        self.played_letters = []
        self.chosen_letter = ""
        self.alive = True
