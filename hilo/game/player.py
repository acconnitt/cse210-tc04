import random


class Player:

    def __init__(self):
        self.score = 300
        self.firstCard = 0
        self.secondCard = 0
        self.cards = []

    def dealCards(self):
        self.firstCard = random.randint(1, 13)
        self.secondCard = random.randint(1, 13)
        while self.secondCard == self.firstCard:
            self.secondCard = random.randint(1, 13)
            # This makes it impossible to get the same card twice
        self.cards = [self.firstCard, self.secondCard]
        return self.cards

    def updateScore(self, guess):
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


