class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand  # List of Card objects

    def play_card(self, index):
        """Plays a card from the player's hand."""
        if 0 <= index < len(self.hand):
            return self.hand.pop(index)  # Removes and returns the card
        return None


    def add_card(self, card):
        self.hand.append(card)






