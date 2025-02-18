from letterstate import LetterState


class SecretWord:
    def __init__(self, secret_word) -> None:
        self.secret_word: str = secret_word
        self.chosen_word_by_letter_and_state:list[list]= [
            [letter, LetterState.HIDDEN] for letter in self.secret_word
        ]
        self.discovered: bool = False

    def __str__(self) -> str:
        word_print: str = ""
        for letter_state in self.chosen_word_by_letter_and_state:
            if letter_state[1] == LetterState.REVEALED:
                word_print += letter_state[0]
            else:
                word_print += "_"
        return f"Palavra secreta: {word_print}"
