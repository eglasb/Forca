class HangmanDoll:
    def __init__(self) -> None:
        self.drawings: dict = {
            6: "desenho com 6 vidas",
            5: "desenho com 6 vidas",
            4: "desenho com 6 vidas",
            3: "desenho com 6 vidas",
            2: "desenho com 6 vidas",
            1: "desenho com 6 vidas",
            0: "desenho com 6 vidas",
        }

    def draw_hangman(self, lifes:int):
        print(self.drawings[lifes])
        print(
            """ 
                ___ 
               |   |
                ---
                 |
               -----
              /     \\
            """
        )
