import random


class Player:
    """This class is used to store all needed values for the HiLo game. 
    Creates an object that stores a score value, two randomly generated numbers, and a list which holds the random numbers until overwritten."""

    def __init__(self):
        self.score = 300
        self.firstCard = 0
        self.secondCard = 0
        self.cards = []

    def dealCards(self):
        """The overall function provides the numbers used in the HiLo game.
        - When called, generates and stores two numbers in two variables. 
        - When the program randomly generates the same number for both cards, the second card is regenerated.
        - The function then stores the two variables inside the cards list, and then returns the list.
        """
        
        self.firstCard = random.randint(1, 13)
        self.secondCard = random.randint(1, 13)
        while self.secondCard == self.firstCard:
            self.secondCard = random.randint(1, 13)
            # This makes it impossible to get the same card twice
        self.cards = [self.firstCard, self.secondCard]
        return self.cards

    def updateScore(self, guess):
        """This function adds-to/takes-from the score depending on two things. The given argument (high/low), and the stored calrd values.
        - The function first asks if the argument given equals h or l. 
        - If h, adds 100 points if the second card value is higher than the first, or takes away 75 points if the second card is lower.
        - If l, takes 75 points if the second card value is higher than the first, or adds 100 points if the second care is lower. 
        - The score value is then returned. """
        
        if guess == "h":
            if self.cards[0] < self.cards[1]:
                self.score += 100

            elif self.cards[0] > self.cards[1]:
                self.score -= 75

        elif guess == "l":
            if self.cards[0] > self.cards[1]:
                self.score += 100

            elif self.cards[0] < self.cards[1]:
                self.score -= 100

        return self.score


