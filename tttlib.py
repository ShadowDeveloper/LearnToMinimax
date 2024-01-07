# This file contains the Board class, which is used to represent the state of the game. The AI is implemented in main.py.

import colorama
class Board:
    def __init__(self):
        self.board = [0,0,0,0,0,0,0,0,0]
        self.xplayer = 1
        self.oplayer = -1
        self.turn = 1
        self.moves = [0,1,2,3,4,5,6,7,8]

    def display(self):
        print("\n  |-----|-----|-----|  \n", end="")
        for i in range(3):
            for j in range(3):
                print("  |  ", end="")
                if self.board[3*i+j] == self.xplayer:
                    print(colorama.Fore.LIGHTGREEN_EX+"X"+colorama.Fore.RESET, end="")
                elif self.board[3*i+j] == self.oplayer:
                    print(colorama.Fore.LIGHTRED_EX+"O"+colorama.Fore.RESET, end="")
                else:
                    print(colorama.Fore.LIGHTBLUE_EX+str(i*3+j)+colorama.Fore.RESET, end="")
            print("  |  ", end="")
            print("\n  |-----|-----|-----|  \n", end="")

    def move(self, move):
        if self.board[move] == 0:
            self.board[move] = self.turn
            self.turn = 1 if (self.board.count(-1)-self.board.count(1)) == 0 else -1
            self.generate_moves()
            return 0
        else:
            return -1

    def unmove(self, move):
        if self.board[move] != 0:
            self.board[move] = 0
            self.turn = 1 if (self.board.count(-1)-self.board.count(1)) == 0 else -1
            self.generate_moves()
            return 0
        else:
            return -1

    def check_win(self):
        for i in range(3):
            if self.board[3*i] == self.board[3*i+1] == self.board[3*i+2] != 0:
                return self.board[3*i]
            if self.board[i] == self.board[i+3] == self.board[i+6] != 0:
                return self.board[i]
        if self.board[0] == self.board[4] == self.board[8] != 0:
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != 0:
            return self.board[2]
        if self.board.count(0) == 0:
            return 0
        return None

    def generate_moves(self):
        moves = []
        for i in range(9):
            if self.board[i] == 0:
                moves.append(i)
        self.moves = moves