import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def has_player_won(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_full(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        if player == 'O':
            return 'X'
        else:
            return 'O'

    def print_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        if self.get_random_first_player() == 1:
            player = 'X'
        else:
            player = 'O'
        
        while True:
            print(f"Player {player} turn")

            self.print_board()

            row = int(input("Enter row of desired spot: "))
            col = int(input("Enter column of desired spot: "))
            print()

            self.fix_spot(row - 1, col - 1, player)

            if self.has_player_won(player):
                print(f"Player {player} wins the game!")
                break

            if self.is_board_full():
                print("Match Draw!")
                break

            player = self.swap_player_turn(player)

        print()
        self.print_board()


tic_tac_toe = TicTacToe()
tic_tac_toe.start()
