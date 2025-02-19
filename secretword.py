from letterstate import LetterState
import random


class SecretWord:
    def __init__(self) -> None:
        self.available_words: tuple[str, ...] = (
            "cobra",
            "aguia",
            "cavalo",
            "marinho",
            "chimpanze",
            "escorpiao",
            "dromedário",
            "hipopótamo",
            "tartaruga",
            "formiga",
            "crocodilo",
            "pinguim",
            "pulga",
            "gaivota",
            "baleia",
            "barata",
            "girafa",
            "gorila",
            "serpente",
            "mosca",
            "mosquito",
            "zebra",
            "onça",
            "tigre",
            "borboleta",
            "camaleão",
            "capivara",
            "beija",
            "flor",
            "aranha",
            "boto",
            "jiboia",
            "jacare",
            "foca",
            "besouro",
            "sapo",
            "tatu",
            "panda",
            "sardinha",
            "peixe",
            "polvo",
            "rinoceronte",
            "hiena",
            "rouxinol",
            "andorinha",
            "abutre",
            "gaviao",
            "corvo",
            "falcao",
            "condor",
        )  # , "novamente", "espirro")
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
                break
            print(f"ERRO: Acabaram as palavras! Resetando lista de palavras!")
            self.chosen_words = []
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
