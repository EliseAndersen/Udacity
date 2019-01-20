import random

moves = ['rock', 'paper', 'scissors']


class Player():

    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, learn_move):
        pass
# Parent Player class


class RandomPlayer(Player):

    def move(self):
        throw = random.choice(moves)
        return (throw)
# This class selects a random move choice


class ReflectPlayer(Player):

    def __init__(self):

        Player.__init__(self)
        self.learn_move = random.choice(moves)

    def move(self):
        if self.learn_move is None:
            throw = moves[0]                      # First move is always rock
        else:
            throw = self.learn_move               # next move is humanplayers
            return (throw)                        # previous move

    def learn(self, learn_move):

        self.learn_move = learn_move
# This Class reflects the human players 1st and 2nd moves


class Cycles(Player):

    def __init__(self):

        Player.__init__(self)
        self.step = 0

    def move(self):
        throw = None
        if self.step == 0:
            throw = moves[0]
            self.step = self.step + 1
        elif self.step == 1:
            throw = moves[1]
            self.step = self.step + 1
        else:
            throw = moves[2]
            self.step = self.step + 1
        return throw
# This Class cycles through the moves list starting at rock


class HumanPlayer(Player):

    def move(self):

        throw = input('rock, paper, scissors? >')

        while throw != 'rock'and throw != 'paper'and throw != 'scissors':
            print('Sorry try again')
            throw = input('rock, paper, scissors? >')
        return (throw)
# This class requests a human player to make a selection
# ask what the human play wanr to play and checks
# if the input is correct

class Game():

    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_game(self):

        print("Rock Paper Scissors, Go!")
        for round in range(3):
            print (f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print('Player01 won!')
        elif self.p1.score < self.p2.score:
            print('Player02 won!')
        else:
            print('The game was a tie!')
        print('The final score: Player01 has ' + str(self.p1.score) + ' while Player02 has ' +
              str(self.p2.score))
# This class starts the game prints information and calls the playround class
# Also prints out the final score

    def play_single(self):
        print("Rock Paper Scissors, Go!")
        print (f"Round 1 of 1:")
        self.play_round()
        if self.p1.score > self.p2.score:
            print('Player01 won!')
        elif self.p1.score < self.p2.score:
            print('Player02 won!')
        else:
            print('The game was a tie!')
        print('The final score: Player01 has ' + str(self.p1.score) + ' while Player02 has ' +
              str(self.p2.score))
# This class will play a single round of RPS
# A copy of play_game w/o for loop

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = Game.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)
# This class calls the play class, sets the move 1 and 2 variables
# then sets the result variable. Plus stores the players move

    def play(self, move1, move2):
            print(f"Player01 played {move1}")
            print(f"Player02 played {move2}")
            
            if beats(move1, move2):
                print ("** YOU WIN ! **")
                self.p1.score += 1
                print(f"Player01 wins this round!")
                print('The score: Player01 has ' + str(self.p1.score) + ' while Player02 has ' + str(self.p2.score) + '\n')
                return 1
                
                
            elif beats(move2, move1):
                print ("** YOU LOSE ! **")
                self.p2.score += 1
                print(f"Player 2 wins this round!")
                print('The score: Player01 has ' + str(self.p1.score) + ' while Player02 has ' + str(self.p2.score) + '\n')
                return 2

            else:
                print ("** It's A TIE **")
                print('The score: Player01 has ' + str(self.p1.score) + ' while Player02 has ' + str(self.p2.score) + '\n')
                return 0   
                
   
# This class calls the beats functions


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))
# I believe beats would be considered a function and not a module because
# it not part of a class...


if __name__ == '__main__':
    answer = [Player(), RandomPlayer(), Cycles(), ReflectPlayer()]
    p2 = input('Select the RPS game you would like to play or just hit any\
 key and enter for random game: [1]Rock, [2]Random,\
[3]Reflective, or [4]Cycles: >')
# answer is a player class list
# p2 is output input from the user

    while p2 != 1 or p2 != 2 or p2 != 3 or p2 != 4:
        p2 = random.choice(answer)
        break
# If the entry is not a specific entry then
# automatically selects a random choice

    if p2 == '1':
        p2 = Player()
    elif p2 == '2':
        p2 = RandomPlayer()
    elif p2 == '3':
        p2 = Cycles()
    elif p2 == '4':
        p2 = ReflectPlayer()
# Set the p2 variable to the correct player class

    rounds = input('Enter for [s]ingle game or [f]ull game: >')
    Game = Game(p2)
    while True:
        if rounds == 's':
            Game.play_single()
            break
        elif rounds == 'f':
            Game.play_game()
            break
        else:
            print('Sorry try again')
            rounds = input('Enter 1 for a single\
             game and 2 for a full game: >')
