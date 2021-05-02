import random
from abc import ABC, abstractmethod

from decision_tree import Node, build_tree, min_max, alpha_beta_min_max, alpha_beta


class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.game = None
        self.tag = 0
        self.moves = 0

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
    def __init__(self, name, alpha_beta=False):
        super().__init__(name)
        self.alpha_beta = alpha_beta

    def make_move(self, possible_choices, random_choice=False):
        if not random_choice:
            root_node = Node(self.game.board, self,
                             self.game.player1 if self.game.player2 == self else self.game.player2,
                             -1)
            build_tree(4, root_node)
            if not self.alpha_beta:
                min_max(root_node, 4, self)
            else:
                alpha_beta(root_node, 4, self)
            choice = min(root_node.children, key=lambda x: x.minmax_value * -1).chosen_house
        else:
            choice = random.choice(possible_choices)
        print(f"{self.name} choice: {choice}")
        return choice
