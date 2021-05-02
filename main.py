from mancala_game import MancalaGame
from player import HumanPlayer, AIPlayer

if __name__ == '__main__':
    player1, player2 = None, None
    print("Welcome to Mancala")
    print("Choose game type (type number):")
    print("1) 2 players game")
    print("2) Player vs AI bot")
    print("3) AI vs AI (Random first move)")
    game_type = int(input())
    pause = False
    while game_type not in range(1, 4):
        print("Incorrect choice, try again")
        game_type = int(input())
    if game_type == 1:
        player1 = HumanPlayer(input("Enter player's 1 name: "))
        player2 = HumanPlayer(input("Enter player's 2 name: "))
    if game_type == 2:
        player1 = HumanPlayer(input("Enter player's name: "))
        player2 = AIPlayer("AI Bot")
    if game_type == 3:
        player1 = AIPlayer("AI Bot 1")
        player2 = AIPlayer("AI Bot 2")
        print("Pause between moves? \n1) Yes\n2) No:")
        pause = int(input()) == 1
    print("+------+------+------+------+------+------+------+------+\n")
    game = MancalaGame(player1, player2, pause)
    game.play_game()
