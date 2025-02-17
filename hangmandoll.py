class HangmanDoll:
    def __init__(self) -> None:
        self.drawings: dict = {
            6: "desenho com 6 vidas",
            5: "desenho com 5 vidas",
            4: "desenho com 4 vidas",
            3: "desenho com 3 vidas",
            2: "desenho com 2 vidas",
            1: "desenho com 1 vidas",
            0: "desenho com 0 vidas",
        }

    def draw_hangman(self, lifes: int):
        print(self.drawings[lifes])
        print(
            """ 
                ________
                |/     |
                |     ___  
                |    |ó,ò|  
                |    \_-_/  
                |      |    
                |    --|--  
                |      |    
                |     / \  
                |    /   \  
                |  
              __|____________
              |             |
            """
        )
