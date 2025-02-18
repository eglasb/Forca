from letterstate import LetterState


class SecretWord:
    def __init__(self, secret_word) -> None:
        self.secret_word: str = secret_word.upper()
        self.chosen_word_by_letter_and_state: list[list] = [
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
        return player_discovered_letter

    def check_if_discovered(self):
        pass
