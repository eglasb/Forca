from letterstate import LetterState
import random


class SecretWord:
    def __init__(self) -> None:
        self.available_words: tuple[str, ...] = ("oi", "tchau") #, "novamente", "espirro")
        self.chosen_word_by_letter_and_state: list[list]
        self.chosen_words: list[str] = []
        self.discovered: bool = False

    def __str__(self) -> str:
        word_print: str = ""
        for letter_state in self.chosen_word_by_letter_and_state:
            if letter_state[1] == LetterState.REVEALED:
                word_print += letter_state[0]
            else:
                word_print += "_"
        return f"Palavra secreta: {word_print}"

    def reset_state(self):
        self.discovered = False

    def choose_secret_word(self):
        print("Sorteando palavra! **BZZZZ BZZZZ BZZZZ**")
        while True:
            word = (random.choice(self.available_words)).upper()
            if word not in self.chosen_words:
                self.chosen_words.append(word)
                print(f"chosen_words: {self.chosen_words}")
                break
        self.chosen_word_by_letter_and_state = [
            [letter, LetterState.HIDDEN] for letter in self.chosen_words[-1]
        ]

    def update_state(self, chosen_letter: str) -> bool:
        player_discovered_letter = False
        for letter in self.chosen_word_by_letter_and_state:
            if chosen_letter == letter[0]:
                letter[1] = LetterState.REVEALED
                player_discovered_letter = True
        self.discovered = all(
            letter[1] == LetterState.REVEALED
            for letter in self.chosen_word_by_letter_and_state
        )
        return player_discovered_letter  # True if player discovered a letter

    def check_if_discovered(self):
        pass
