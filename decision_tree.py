import copy
from typing import List

from mancala_game import is_game_finished, move_seeds, get_players_possible_choices


def build_tree(depth: int, node):
    if depth == 0:
        return
    choices = get_players_possible_choices(node.player, node.board)
    for choice in choices:
        board_copy = copy.deepcopy(node.board)
        turn_ended = move_seeds(node.player, board_copy, choice)
        if turn_ended:
            next_player = node.other_player
            other_player = node.player
        else:
            next_player = node.player
            other_player = node.other_player
        new_child = Node(board_copy, next_player, other_player, choice)
        node.children.append(new_child)
        build_tree(depth - 1 if turn_ended else depth, new_child)


def min_max_tree(node, depth, maximizing_player):
    if depth == 0 or is_game_finished(node.board, node.player):
        node.minmax_value = node.get_board_value()
        return node.get_board_value()
    if maximizing_player == node.player:
        value = float('-inf')
        for child in node.children:
            value = max(value, min_max_tree(child, depth - 1, maximizing_player))
            node.minmax_value = value
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, min_max_tree(child, depth - 1, maximizing_player))
            node.minmax_value = value
        return value


class Node:
    def __init__(self, board: List[int], player, other_player, chosen_house):
        self.board = board
        self.player = player
        self.other_player = other_player
        self.chosen_house = chosen_house
        self.children = []
        self.minmax_value = None

    def get_board_value(self):
        return sum(self.board[0:7]) if self.player.tag == 1 else sum(self.board[7:14])

    def __str__(self):
        return f"Node({self.minmax_value},{type(self.player)}, {type(self.other_player)})"
