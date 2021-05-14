from game.player import Player


class Dealer:

    def __init__(self):
        self.player = Player()
        self.pair = []
        self.keep_playing = True
        self.guess = ""

    def play_game(self):
        while self.keep_playing:
            self.getCards()
            self.output()

    def getCards(self):
        self.pair = self.player.dealCards()

    def output(self):
        print(f"\nThe card is: {self.pair[0]}")
        self.guess = input("Higher or lower? [h/l] ")
        print(f"Next card was: {self.pair[1]}")
        points = self.player.updateScore(self.guess)
        print(f"Your score is: {points}")
        if points <= 0:
            dealer.keep_playing = False
        kp = input("Keep playing? [y/n]? ")
        if kp == "n":
            self.keep_playing = False
