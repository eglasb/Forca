import random
from hangmandoll import HangmanDoll
from player import Player
from letterstate import LetterState


class Game:
    def __init__(self, available_words: tuple[str, ...]) -> None:
        self.player: Player
        self.hangman_doll: HangmanDoll = HangmanDoll()
        self.available_words = available_words
        self.played_words: list[str] = []
        self.chosen_word_by_letter_and_state:list
        self.victories: int = 0

    # Só para testes
    def testa_player(self) -> None:
        print(self.player)

    # Pega nome e cria Player,
    # sorteia palavra e chama next_turn() até zerar as vidas
    def begin_game(self) -> None:
        print("Olá! vamos jogar FORCA?")
        self.player = Player(self.get_name())
        self.chosen_word_by_letter_and_state = self.get_random_word()
        print(f"Ok {self.player.name}, vamos começar!!")
        while self.player.lifes > 0:  # incluir OR palavra descoberta
            self.next_turn(self.player, self.hangman_doll)
            self.player.lifes = 0  # para evitar loop infinito por enquanto

    def next_turn(self, player: "Player", hangman_doll: "HangmanDoll"):
        hangman_doll.draw_hangman(player.lifes)
        self.print_secret_word()
        print(player.choose_letter())

    def get_name(self) -> str:
        return input("Qual o seu nome? ")

    def get_random_word(self) -> list[list]:
        print("Sorteando palavra! **BZZZZ BZZZZ BZZZZ**")
        random_word = random.choice(self.available_words)
        letters_and_state: list[list] = [
            [letter, LetterState.HIDDEN] for letter in random_word
        ]
        return letters_and_state

    def print_secret_word(self) -> None:
        word_print:str = ""
        print(self.chosen_word_by_letter_and_state)  # só de teste
        for letter_state in self.chosen_word_by_letter_and_state:
            if letter_state[1] == LetterState.REVEALED:
                word_print += letter_state[0]
            else:
                word_print += "_"
        print(word_print)
