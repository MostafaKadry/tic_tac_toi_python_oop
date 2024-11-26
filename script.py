import os
def clear_screen():
    os.system("cls")

class Player():
    def __init__(self):
      self.name = ''
      self.symbol = ''

    def choose_name(self):
        while True:
            name = input("insert your name (letter only*) : ")
            if name.isalpha():
                self.name = name
                break
            print("please insert valid name!")
    def choose_symbol(self):
        while True:
            symbol =  input(f"{self.name}, Choose Symbol (one letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("please insert valid symble!")

class Board():
    def __init__(self):
      self.board = [i for i in range(1, 10)]      
    
    
    def display_board(self):
            rows = [self.board[i:i + 3] for i in range(0, 9, 3)]
            print("\n----------\n".join(" | ".join(map(str, row)) for row in rows))
    
    
    def update_board(self,choice, symbol):
        while True:
            try:
                if self.is_valide_move(choice):
                    self.board[choice-1] = symbol
                    return True
                return False
            except ValueError:
                return False
    def is_valide_move(self, choice):
        if isinstance(self.board[choice - 1], int) and 1 <= choice <= 9:
            return True
        return False
    
    def reset_board(self):
        self.board = [i for i in range(1, 10)]
        rows = [self.board[i:i + 3] for i in range(0, 9, 3)]
        print("\n----------\n".join(" | ".join(map(str, row)) for row in rows))

class Menu():
    def display_main_menu(self):
        print("welcome to tic tack toi")
        print("1. Start Game")
        print("2.Quit Game")
        while True:
            try:
                choose = int(input("Enter Your Choice (1 or 2): "))
                if choose in {1, 2}:  # Check if input is 1 or 2
                    return choose
                print("Invalid input, please enter 1 or 2.")
            except ValueError:
                print("Invalid input, please enter an integer.")
    def display_end_game_menu(self):
        while True:
            try:
                choose = int(input(""""
End Game?
Enter 1 for Yes
or    2 for No
"""))
                if choose in {1, 2}:  # Check if input is 1 or 2
                    return choose
                print("Invalid input, please enter 1 or 2.")
            except ValueError:
                print("Invalid input, please enter an integer.")

class Game():
    def __init__(self):
        self.players = [Player(), Player()]  
        self.menu = Menu()
        self.board = Board()
        self.current_player_index = 0 


    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    
    def setup_players(self):
        for num, player in enumerate(self.players, start=1):
            print(f"Player {num}, enter your info.")
            player.choose_name()
            player.choose_symbol()
            clear_screen()
    
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win():  # Check if there's a winner
                self.board.display_board()
                print(f"{self.players[self.current_player_index].name} wins!")
                self.quit_game()
                break
            elif self.check_draw():  # Check if it's a draw
                self.board.display_board()
                print("It's a draw!")
                self.quit_game()
                break

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input(f"Choose a cell (1-9): "))
                if self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid Move!")
            except ValueError:
                print("Please inserte number between 1-9!")
        if not self.check_win() and not self.check_draw():
            self.switch_player()
    
    def switch_player(self):
        self.current_player_index ^= 1
    
    def check_win(self):
        # Winning combinations (rows, columns, diagonals)
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        # Check each winning combination
        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]] and self.board.board[combo[0]] != " ":
                return True  # A winner is found
        return False  # No winner yet
    
    def check_draw(self):
        # Check if the board is full (all cells are chosen)
        if all(isinstance(cell, str) for cell in self.board.board):  # Check if all cells have 'X' or 'O'
            return True  # Draw condition (board is full, no winner)
        return False  # The game is not a draw yet
    
    def restart_game(self):
        self.board.reset_board()
    def quit_game(self):
        if self.menu.display_end_game_menu() == 1:
            print("quit game")
            return
        else: 
            self.start_game()



game=Game()
game.start_game()