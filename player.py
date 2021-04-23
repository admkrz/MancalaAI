from abc import ABC, abstractmethod

from decision_tree import Node, build_tree, min_max_tree


class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.game = None
        self.tag = 0

    @abstractmethod
    def make_move(self, possible_choices):
        pass


class HumanPlayer(Player):
    def make_move(self, possible_choices):
        print(f"{self.name} possible choices: " + possible_choices.__str__())
        choice = int(input("Enter a number: "))
        if choice not in possible_choices:
            print("Incorrect house number")
            choice = self.make_move(possible_choices)
        return choice


class AIPlayer(Player):
    def make_move(self, possible_choices):
        root_node = Node(self.game.board, self, self.game.player1 if self.game.player2 == self else self.game.player2,
                         -1)
        build_tree(4, root_node)
        min_max_tree(root_node, 4, self)
        choice = min(root_node.children, key=lambda x: x.minmax_value * -1).chosen_house
        print(f"{self.name} choice: {choice}")
        return choice
