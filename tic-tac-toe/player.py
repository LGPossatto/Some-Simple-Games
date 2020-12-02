class Player():

    def __init__(self, name:str) -> None:
        self.__name: str = name.upper()
        self.__times_won: int = 0
    
    @property
    def name(self) -> str:
        return self.__name

    @property
    def times_won(self) -> str:
        return self.__times_won
        
    
    def plus_win(self) -> None:
        self.__times_won += 1
