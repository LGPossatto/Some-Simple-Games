from game import Game
from player import Player

def play_game():
    while True:
        for player in players:
            while True:
                try:
                    game.print_board()
                    print(f'Player "{player.name}" move!')
                    player_move = int(input('Select your move: '))
                    
                    print("\033c", end='')

                    game.play_move(player, player_move)
                    break
                
                except:
                    print("\033c", end='')
                    print('Please select a valid number!')
                    continue

            if game.verify_game():
                player.plus_win() 
                print(f'\nPlayer "{player.name}" won!')
                print(f'\nScoreboard\nPlayer "{players[0].name}": {players[0].times_won}\nPlayer "{players[1].name}": {players[1].times_won}\n')
                
                while True:
                    try:
                        play_again = str(input('Play again (y/n)? ')).lower()
                        print("\033c", end='')
                    
                        if play_again == 'y' or play_again == 'n':
                            break

                        raise Exception
                    except:
                        print('Please, only "y" or "n"!')
                        continue

                if play_again == 'y':
                    game.reset_game()
                    play_game()
                
                return None
                                        
                

print("\033c", end='')
players = [Player('x'), Player('o')]
game = Game()
play_game()
print('Thanks for playing!!!')