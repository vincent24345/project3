class Player:
    def __init__(self, name, hand):
        self.name = name  # Store the player's name
        self.hand = hand  # Store the player's hand (a list of Card objects)

    def play_card(self, index):
        if 0 <= index < len(self.hand):
            return self.hand.pop(index)
        else:
            print("Invalid index!")
            return None

    def add_card(self, card):
        self.hand.append(card)



