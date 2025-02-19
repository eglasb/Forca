import unicodedata


def get_clean_answer(
    text: str, possible_choices: tuple[str, ...], upper: bool = True
) -> str:
    while True:
        answer = input(text).strip()
        answer_upper = answer.upper()
        if answer not in possible_choices and answer_upper not in possible_choices:
            print(f'Entrada inválida "{answer}"!')
        else:
            break
    if upper == True:
        return answer.upper()
    return answer


def read_words_file(filepath="lista_palavras.txt") -> tuple[str, ...]:
    with open(filepath, encoding="utf-8") as file:
        return tuple(line.strip().strip(",") for line in file if line.strip())


def remove_accents(letter: str) -> str:
    return "".join(
        character
        for character in unicodedata.normalize("NFD", letter)
        if unicodedata.category(character) != "Mn"
    )
