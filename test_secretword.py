import random
from hangmandoll import HangmanDoll
from player import Player
from letterstate import LetterState
from secretword import SecretWord
from utils import get_clean_answer, read_words_file

if __name__ == "__main__":
    secret_word = SecretWord(
        ("MACACO-PREGO", "COBRA", "ÁGUIA", "CAVALO-MARINHO", "CHIMPANZÉ")
    )
    secret_word.choose_secret_word()
    print(f"available_words: {secret_word.available_words}, chosen_words: {secret_word.chosen_words}\n, chosen_word_by_l_s: {secret_word.chosen_word_by_letter_and_state}")
    secret_word.choose_secret_word()
    print(
        f"available_words: {secret_word.available_words}, chosen_words: {secret_word.chosen_words}\n, chosen_word_by_l_s: {secret_word.chosen_word_by_letter_and_state}"
    )
    secret_word.choose_secret_word()
    print(
        f"available_words: {secret_word.available_words}, chosen_words: {secret_word.chosen_words}\n, chosen_word_by_l_s: {secret_word.chosen_word_by_letter_and_state}"
    )
    secret_word.choose_secret_word()
    print(
        f"available_words: {secret_word.available_words}, chosen_words: {secret_word.chosen_words}\n, chosen_word_by_l_s: {secret_word.chosen_word_by_letter_and_state}"
    )
    secret_word.choose_secret_word()
    print(
        f"available_words: {secret_word.available_words}, chosen_words: {secret_word.chosen_words}\n, chosen_word_by_l_s: {secret_word.chosen_word_by_letter_and_state}"
    )
    secret_word.choose_secret_word()
    print(
        f"available_words: {secret_word.available_words}, chosen_words: {secret_word.chosen_words}\n, chosen_word_by_l_s: {secret_word.chosen_word_by_letter_and_state}"
    )
    secret_word.choose_secret_word()
    print(
        f"available_words: {secret_word.available_words}, chosen_words: {secret_word.chosen_words}\n, chosen_word_by_l_s: {secret_word.chosen_word_by_letter_and_state}"
    )
    secret_word.choose_secret_word()
    print(
        f"available_words: {secret_word.available_words}, chosen_words: {secret_word.chosen_words}\n, chosen_word_by_l_s: {secret_word.chosen_word_by_letter_and_state}"
    )
