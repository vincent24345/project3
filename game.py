import os
from card import Card
import random


# Suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def create_deck():
    """Creates and returns a shuffled deck of cards."""
    deck = []
    current_dir = os.path.dirname(__file__)
    images_dir = os.path.join(current_dir, "images")
    
    for suit in suits:
        for rank in ranks:
            image_path = os.path.join(images_dir, f"{rank}_of_{suit}.png")
            card = Card(suit, rank, image_path)
            deck.append(card)
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    """Deals cards evenly among four players."""
    # This splits the deck into 4 roughly equal hands.
    return [deck[i::4] for i in range(4)]
