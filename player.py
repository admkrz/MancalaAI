import random
import time
from abc import ABC, abstractmethod

from decision_tree import Node, build_tree, min_max, alpha_beta_min_max, alpha_beta


class Player(ABC):
    def __init__(self, name, depth, heuristic=1, alpha_beta=False):
        self.name = name
        self.game = None
        self.tag = 0
        self.moves = 0
        self.timeElapsed = 0
        self.depth = depth
        self.alpha_beta = alpha_beta
        self.heuristic = heuristic

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
    def __init__(self, name, depth, heuristic, alpha_beta=False):
        super().__init__(name, depth, heuristic, alpha_beta)
        self.depth = depth


    def make_move(self, possible_choices, random_choice=False):
        if not random_choice:
            root_node = Node(self.game.board, self,
                             self.game.player1 if self.game.player2 == self else self.game.player2,
                             -1)
            start = time.time()
            build_tree(self.depth, root_node)

            if not self.alpha_beta:
                min_max(root_node, self.depth, self, self.heuristic)
            else:
                alpha_beta(root_node, self.depth, self, self.heuristic)
            end = time.time()
            self.timeElapsed += (end - start)
            choice = min(root_node.children, key=lambda x: x.minmax_value * -1).chosen_house
        else:
            choice = random.choice(possible_choices)
        print(f"{self.name} choice: {choice}")
        return choice
