from hangmandoll import HangmanDoll
from player import Player
from secretword import SecretWord
from utils import get_clean_answer, read_words_file, clear_screen


class Game:
    def __init__(self) -> None:
        self.player: Player
        self.hangman_doll: HangmanDoll = HangmanDoll()
        self.played_words: list[str] = []
        self.victories: int = 0
        self.games_played: int = 0
        self.secret_word: SecretWord = SecretWord(read_words_file(upper_case=True))

    def begin_game(self) -> None:
        self.games_played += 1
        if self.games_played == 1:
            clear_screen()
            print("Olá! vamos jogar FORCA?")
            self.player = Player(self.get_name())
        else:
            clear_screen()
            print(f"Jogo: {self.games_played}, Vitórias: {self.victories}")
            self.player.reset_state()
            self.secret_word.reset_state()
        self.secret_word.choose_secret_word()
        print(f"Ok {self.player.name}, vamos lá!!")
        while self.player.lifes > 0 and self.secret_word.discovered == False:
            self.next_turn(self.player, self.hangman_doll, self.secret_word)
        self.end_game()

    def next_turn(
        self, player: "Player", hangman_doll: "HangmanDoll", secret_word: "SecretWord"
    ):
        hangman_doll.draw_hangman(player.lifes)
        print(secret_word)
        if player.played_letters != []:
            print(f"Letras já tentadas: ", end="")
            for letter in player.played_letters:
                print(letter, end=" ")
            print("")
        if secret_word.update_state(player.choose_letter()) == False:
            clear_screen()
            print("Você errou e perdeu uma vida!")
            player.lose_life()
        else:
            clear_screen()
            print("Você acertou uma letra!")

    def get_name(self) -> str:
        return input("Qual o seu nome? ").strip().title()

    def end_game(self):
        if self.player.lifes == 0:
            self.hangman_doll.draw_hangman(self.player.lifes)
            print("Você morreu!")
            print(f"A palavra secreta era: {self.secret_word.chosen_words[-1]}!")
        else:
            self.hangman_doll.draw_hangman(7)
            print(f"Palavra secreta descoberta: {self.secret_word.chosen_words[-1]}!")
            print(f"PARABENS!!! Você ganhou {self.player.name}!")
            self.victories += 1
        print(f"{self.player.name}, você gostaria de jogar novamente?")
        answer = get_clean_answer("(S)im ou (N)ão? ", ("S", "N"))
        if answer == "S":
            self.begin_game()
        elif answer == "N":
            parting_text = ""
            if self.games_played == 1:
                parting_text += f"Você jogou {self.games_played} vez e "
            else:
                parting_text += f"Você jogou {self.games_played} vezes e "
            if self.victories == 1:
                parting_text += f"ganhou {self.victories} jogo"
            else:
                parting_text += f"ganhou {self.victories} jogos"
            print(parting_text)
            print(f"Até a próxima, {self.player.name}")
            input("Pressione ENTER para sair...")
