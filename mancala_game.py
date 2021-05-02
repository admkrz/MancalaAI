import random


def get_opposite_seeds(house_number, board):
    diff = abs(house_number - 6)
    if house_number in range(0, 6):
        opposite_house = house_number + diff * 2
    else:
        opposite_house = house_number - diff * 2
    return opposite_house, board[opposite_house]


def move_seeds(current_player, board, chosen_house):
    seeds_to_move = board[chosen_house]
    board[chosen_house] = 0
    i = chosen_house + 1
    turn_ended = True
    while seeds_to_move > 0:
        if i > len(board) - 1:
            i = 0
        if (current_player.tag == 1 and i != 13) or (current_player.tag == 2 and i != 6):
            board[i] += 1
            if seeds_to_move == 1:
                if (current_player.tag == 1 and i == 6) or (current_player.tag == 2 and i == 13):
                    turn_ended = False
                if board[i] == 1:
                    if current_player.tag == 1 and i in range(0, 6):
                        opposite_house, opposite_house_seeds = get_opposite_seeds(i, board)
                        if opposite_house_seeds > 0:
                            board[6] += board[i]
                            board[6] += opposite_house_seeds
                            board[i] = 0
                            board[opposite_house] = 0
                    elif current_player.tag == 2 and i in range(7, 13):
                        opposite_house, opposite_house_seeds = get_opposite_seeds(i, board)
                        if opposite_house_seeds > 0:
                            board[13] += board[i]
                            board[13] += opposite_house_seeds
                            board[i] = 0
                            board[opposite_house] = 0
            seeds_to_move -= 1
        i += 1
    return turn_ended


def get_players_possible_choices(player, board):
    possible_choices = []
    if player.tag == 1:
        houses = range(0, 6)
    else:
        houses = range(7, 13)
    for i in houses:
        if board[i] != 0:
            possible_choices.append(i)
    return possible_choices


def is_game_finished(board, current_player):
    return (sum(board[0:6]) == 0 and current_player.tag == 1) or (sum(board[7:13]) == 0 and current_player.tag == 2)


class MancalaGame:
    def __init__(self, player1, player2, pause) -> None:
        self.player1 = player1
        self.player2 = player2
        self.player1.tag = 1
        self.player1.game = self
        self.player2.tag = 2
        self.player2.game = self
        self.pause = pause
        self.board = []
        self.create_board()
        self.current_player = random.choice([self.player1, self.player2])

    def create_board(self):
        for i in range(0, 14):
            if i == 6 or i == 13:
                self.board.append(0)
            else:
                self.board.append(4)

    def play_game(self):
        from player import AIPlayer

        if isinstance(self.player1, AIPlayer) and isinstance(self.player2, AIPlayer):
            self.make_move(random_move=True)
        while not is_game_finished(self.board, self.current_player):
            self.change_player()
            self.make_move()
        self.print_results()

    def make_move(self, random_move=False):
        turn_ended = False
        possible_choices = self.get_possible_choices()
        if random_move:
            choice = self.current_player.make_move(possible_choices, random_choice=True)
            turn_ended = move_seeds(self.current_player, self.board, choice)
        while not turn_ended and not is_game_finished(self.board, self.current_player):
            # self.print_board()
            possible_choices = self.get_possible_choices()
            if len(possible_choices) == 0:
                break
            choice = self.current_player.make_move(possible_choices)
            turn_ended = move_seeds(self.current_player, self.board, choice)

            from player import AIPlayer

            if self.pause and isinstance(self.current_player, AIPlayer):
                input()

            self.current_player.moves += 1

    def get_possible_choices(self):
        possible_choices = []
        if self.current_player == self.player1:
            houses = range(0, 6)
        else:
            houses = range(7, 13)
        for i in houses:
            if self.board[i] != 0:
                possible_choices.append(i)
        return possible_choices

    def change_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def print_results(self):
        self.print_board()
        results1, results2 = self.get_results()
        print(f"{self.player1.name} score: {results1}")
        print(f"{self.player2.name} score: {results2}")
        if results1 > results2:
            print("Player 1 has won!")
        if results1 < results2:
            print("Player 2 has won!")
        if results1 == results2:
            print("Draw!")

    def get_results(self):
        return sum(self.board[0:7]), sum(self.board[7:14])

    def print_board(self):
        print("\n+------+------+------+------+------+------+------+------+")
        print(f"|------|  [5] |  [4] |  [3] |  [2] |  [1] |  [0] |------|  <=== {self.player1.name} houses")
        print("+------+------+------+------+------+------+------+------+")
        print("|      |      |      |      |      |      |      |      |")
        line = "|      |"
        for i in reversed(range(0, 6)):
            if self.board[i] < 10:
                line += " "
            line += f"  {self.board[i]}  |"
        print(line + "      |")
        print("|      |      |      |      |      |      |      |      |")
        line = "|"
        if self.board[6] < 10:
            line += " "
        line += f"  {self.board[6]}  |------+------+------+------+------+------|"
        if self.board[13] < 10:
            line += " "
        print(line + f"  {self.board[13]}  |")
        print("|      |      |      |      |      |      |      |      |")
        line = "|      |"
        for i in range(7, 13):
            if self.board[i] < 10:
                line += " "
            line += f"  {self.board[i]}  |"
        print(line + "      |")
        print("|      |      |      |      |      |      |      |      |")
        print("+------+------+------+------+------+------+------+------+")
        print(f"|------|  [7] |  [8] |  [9] | [10] | [11] | [12] |------|   <=== {self.player2.name} houses")
        print("+------+------+------+------+------+------+------+------+\n")
