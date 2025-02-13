from card import Card

#suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            image_path = f'images/{rank}_of_{suit}.png'
            card = Card(suit, rank, image_path)
            deck.append(card)
            return deck
        
    def create_deck():
        for card in deck:
            print(card.suit, card.rank)
            print(card.image)



