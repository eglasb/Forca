from letterstate import LetterState
import random
from utils import remove_accents


class SecretWord:
    def __init__(self, available_words: tuple[str, ...]) -> None:
        self.available_words = available_words
        self.chosen_word_by_letter_and_state: list[list]
        self.chosen_words: list[str] = []
        self.discovered: bool = False

    def __str__(self) -> str:
        word_print: str = ""
        for letter_state in self.chosen_word_by_letter_and_state:
            if letter_state[2] == LetterState.REVEALED:
                word_print += letter_state[0]
            else:
                word_print += "_"
        return f"Palavra secreta: {word_print}"

    def reset_state(self):
        self.discovered = False

    def choose_secret_word(self):
        print("Sorteando palavra! **BZZZZ BZZZZ BZZZZ**")
        if len(self.chosen_words) == len(self.available_words):
            print(f"ERRO: acabaram as palavras. Resetando lista...")
            self.chosen_words = []
        word = random.choice(
            [unused_words for unused_words in self.available_words if unused_words not in self.chosen_words]
        )
        self.chosen_words.append(word)
        self.chosen_word_by_letter_and_state = [
            [letter, remove_accents(letter), LetterState.HIDDEN]
            for letter in self.chosen_words[-1]
        ]
        for letter in self.chosen_word_by_letter_and_state:
            if letter[0] == "-":
                letter[2] = LetterState.REVEALED

    def update_state(self, chosen_letter: str) -> bool:
        player_discovered_letter = False
        for letter in self.chosen_word_by_letter_and_state:
            if chosen_letter == letter[1]:
                letter[2] = LetterState.REVEALED
                player_discovered_letter = True
        self.discovered = all(
            letter[2] == LetterState.REVEALED
            for letter in self.chosen_word_by_letter_and_state
        )
        return player_discovered_letter  # True if player discovered a letter
