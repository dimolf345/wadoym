

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def clear(self):
        self.hand = []

    def draw(self, deck, count=1):
        for _ in range(0, count):
            self.hand.append(deck.pop(0))