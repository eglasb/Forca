import random
from hangmandoll import HangmanDoll
from player import Player
from letterstate import LetterState
from secretword import SecretWord


class Game:
    def __init__(self, available_words: tuple[str, ...]) -> None:
        self.player: Player
        self.hangman_doll: HangmanDoll = HangmanDoll()
        self.available_words = available_words
        self.played_words: list[str] = []
        self.victories: int = 0
        self.secret_word: SecretWord

    # Só para testes
    def testa_player(self) -> None:
        print(self.player)

    # Pega nome e cria Player,
    # sorteia palavra e chama next_turn() até zerar as vidas
    def begin_game(self) -> None:
        print("Olá! vamos jogar FORCA?")
        self.player = Player(self.get_name())
        self.secret_word = self.get_secret_word()
        print(f"Ok {self.player.name}, vamos começar!!")
        while (
            self.player.lifes > 0 and self.secret_word.discovered == False
        ):  # talvez trocar para get_secretword.doscovered == False
            self.next_turn(self.player, self.hangman_doll, self.secret_word)
            # self.player.lifes = 0  # para evitar loop infinito por enquanto
        self.end_game()

    def next_turn(
        self, player: "Player", hangman_doll: "HangmanDoll", secret_word: "SecretWord"
    ):
        hangman_doll.draw_hangman(player.lifes)
        print(secret_word)
        secret_word.update_state(player.choose_letter())
        

    def get_name(self) -> str:
        return input("Qual o seu nome? ").strip().title()

    def get_secret_word(self) -> SecretWord:
        print("Sorteando palavra! **BZZZZ BZZZZ BZZZZ**")
        return SecretWord(random.choice(self.available_words))

    def end_game(self):
        pass
