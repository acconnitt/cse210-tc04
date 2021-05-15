from game.player import Player


class Dealer:
    """This class provides the functionality of our HiLo game. 
    - Creates and calls a Player Object.
    - Creates a new list, pair, to store result of the Player dealCards funciton.
    - Creates a boolean variable, keep_playing, to stop the game when changed.
    - Creates a variable to store the players input."""

    def __init__(self):
        self.player = Player()
        self.pair = []
        self.keep_playing = True
        self.guess = ""

    def play_game(self):
        """Stops the program if the boolean keep_playing is false.
        - Calls functions to loop the main game functions while true."""
        
        while self.keep_playing:
            self.getCards()
            self.output()

    def getCards(self):
        """Stores card values from Player Object."""
        
        self.pair = self.player.dealCards()

    def output(self):
        """Displays the first card value, asks for a guess of high or low, outputs the second card value, 
        calls a Player Method to update the score according to their guess, prints the score stored in the Player Object,
        stops the game if the score is less than or equal to 0, or asks the user if they want to keep playing(Changes the keep_playing boolean to do this.)."""
        
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
