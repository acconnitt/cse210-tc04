from game.player import Player


class Dealer:

    def __init__(self):
        #All variables and class imports are initialized here
        self.player = Player()
        self.pair = []
        self.keep_playing = True
        self.guess = ""

    def play_game(self):
        #This function is what starts the game and keeps looping through until the game is over.
        while self.keep_playing:
            self.getCards()
            self.output()

    def getCards(self):
        #This function calls the dealCards() function in the player class which returns a list which contains two different cards between 1 and 13
        self.pair = self.player.dealCards()

    def output(self):
        print(f"\nThe card is: {self.pair[0]}")     #displays first card to the player
        self.guess = input("Higher or lower? [h/l] ")     #player inputs their guess
        print(f"Next card was: {self.pair[1]}")     #displays the second card to the player
        points = self.player.updateScore(self.guess)    #calls the function updateScore(guess) which returns the current score the player has, and takes their guess as a parameter
        print(f"Your score is: {points}")   #displays the score to the user
        #This if statement checks if the score of the player is 0 or less, and if true then it changes keep_playing to false and ends the game automatically
        if points <= 0:
            dealer.keep_playing = False
        kp = input("Keep playing? [y/n]? ")     #asks the player if they want to keep playing
        #This if statement just checks if they said no, and if true then it ends the game
        if kp == "n":
            self.keep_playing = False
