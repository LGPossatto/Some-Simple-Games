from time import sleep
from random import random, randint
from datetime import datetime

class reaction_time_game():

    @classmethod
    def game_star(cls):
        
        print('Prepare Yourself!')
        sleep(cls.sleep_time())
        
        time_a = datetime.now()
        input('Press Enter!')
        time_b = datetime.now()
        
        print('Your Time is ', end='')

        time_c = time_b - time_a
        if time_c.seconds < 1:
            print(f'{str(time_c.microseconds)[:-3]} ms')
        elif 10 >= time_c.seconds >= 1 :
            print(f'{time_c.seconds}:{str(time_c.microseconds)[:-3]} ms')
        else:
            print('Too Slow :(')

    @staticmethod
    def sleep_time() -> float:
        return randint(1, 7) + random()


if __name__ == '__main__':
    reaction_time_game.game_star()