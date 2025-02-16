
player_1 =[]
player_2 =[]
player_3=[]
player_4=[]

if not player_1:
    print("Player 1 wins!")
elif not player_2:
    print("Player 2 wins!")
elif not player_3:
    print("Player 3 wins!")
elif not player_4:
    print("Player 4 wins!")
else:
    print("No one wins!")

class Player:
    class Player:
        def __init__(self, name, hand):
            self.name = name  # Store the player's name
            self.hand = hand  # Store the player's hand (a list of cards)

    def play_card(self, index):
        if 0 <= index < len(self.hand):
            return self.hand.pop(index)
        else:
            print("Invalid index!")
            return None

    def add_card(self, card):
        self.hand.append(card)



