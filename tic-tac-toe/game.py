class Game():

    board: list = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

    def __str__(self) -> str:
        return f'{Game.board}'
    
    @classmethod
    def play_move(cls, player: object, play: int) -> bool:
        a, b = str(play)[::]

        if isinstance(cls.board[int(a) - 1][int(b) - 1], str):
            raise Exception

        cls.board[int(a) - 1][int(b) - 1] = (player.name)


    @classmethod
    def verify_game(cls) -> bool:
        for i in range(3):
            if (cls.board[i][0] == cls.board[i][1] == cls.board[i][2] == cls.board[i][0]) or (cls.board[0][i] == cls.board[1][i] == cls.board[2][i] == cls.board[0][i]):
                return True
        
        if (cls.board[0][0] == cls.board[1][1] == cls.board[2][2] == cls.board[0][0]) or (cls.board[0][2] == cls.board[1][1] == cls.board[2][0] == cls.board[0][2]):
            return True
    
        return False

    @classmethod
    def print_board(cls):
        for i in range(3):
            print('|----------------|')
            print(f'|- {cls.board[i][0]:^2} - {cls.board[i][1]:^2} - {cls.board[i][2]:^2} -|')
        print('|----------------|')

    @classmethod
    def reset_game(cls):
        cls.board= [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
