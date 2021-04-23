from mancala_game import MancalaGame
from player import HumanPlayer, AIPlayer

if __name__ == '__main__':
    player1 = HumanPlayer("HUMAN PLAYER")
    player2 = AIPlayer("AI PLAYER")
    #player2 = HumanPlayer("HUMAN PLAYER 2")
    game = MancalaGame(player1, player2)
    game.play_game()
