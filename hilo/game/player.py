import random
#Imports the random module

class Player:

    def __init__(self):
        #All variables are initialized here
        self.score = 300
        self.firstCard = 0
        self.secondCard = 0
        self.cards = []

    def dealCards(self):
        #This function generates two random cards between 1 and 13 that are guaranteed not to be the same, and returns them as one list object
        self.firstCard = random.randint(1, 13)
        self.secondCard = random.randint(1, 13)
        while self.secondCard == self.firstCard:
            self.secondCard = random.randint(1, 13)
            #This makes it impossible to get the same card twice
        self.cards = [self.firstCard, self.secondCard]
        return self.cards

    def updateScore(self, guess):
        #This function updates the score of the player based on the guess they have made, and returns the updated score
        if guess == "h":
            #If guess was higher
            if self.cards[0] < self.cards[1]:
                #Correct guess
                self.score += 100

            elif self.cards[0] > self.cards[1]:
                #Incorrect guess
                self.score -= 75

        elif guess == "l":
            #If guess was lower
            if self.cards[0] > self.cards[1]:
                #Correct guess
                self.score += 100

            elif self.cards[0] < self.cards[1]:
                #Incorrect guess
                self.score -= 75

        return self.score


