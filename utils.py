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
