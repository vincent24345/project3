#initialise the rank order

RankOrder = {
     "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, 
    "8" : 8, "9" : 9, "10" : 10, "Jack" : 11, "Queen" : 12, 
    "King" : 13, "Ace" : 14, "2" : 15
}

#suit order
SuitOrder = {
    "Spades" : 1,
    "Clubs" : 2,
    "Diamonds" : 3,
    "Hearts" : 4
    
}
#compare ranks
def can_beat(firstcard,lastcard):
    if lastcard is None:
        return True
    rank_new = RankOrder[firstcard.rank]
    rank_old = RankOrder[lastcard.rank]
    if rank_new > rank_old:
        return True
    elif rank_new == rank_old:
        suit_new = SuitOrder[firstcard.suit]
        suit_old = SuitOrder[lastcard.suit]
        if suit_new > suit_old:
            return True
    else:
        return False

#check winner

def check_winner(players):
    for player in players:
        if len(player.hand) == 0:
            return player
        return None
#double/triple/quad
def is_valid_double_triple_quad(cards):
    if len(cards) == 1:
        return True
    elif len(cards) == 2:
        return cards[0].rank == cards[1].rank
    elif len(cards) == 3:
        return cards[0].rank == cards[1].rank == cards[2].rank
    elif len(cards) == 4:
        return cards[0].rank == cards[1].rank == cards[2].rank == cards[3].rank
    else:
        print("invalid combo: must be double, triple or quad")
    return False
#combo
def is_valid_combo(cards):
    if len(cards) >= 3 & cards[0].rank != "2":
        return len(cards)
    else:
        print("invalid combo")
        return False
#chop
def is_valid_chop(cards):
    """
    Returns True if 'cards' form three consecutive pairs (e.g., 4-4, 5-5, 6-6).
    Otherwise, returns False.
    """
    # We need exactly 6 cards for a chop of three pairs
    if len(cards) != 6:
        return False
    
    # Sort cards by rank so pairs line up in order
    sorted_cards = sorted(cards, key=lambda c: RankOrder[c.rank])
    
    # Check that each pair is the same rank
    # Pair 1: sorted_cards[0], sorted_cards[1]
    # Pair 2: sorted_cards[2], sorted_cards[3]
    # Pair 3: sorted_cards[4], sorted_cards[5]
    if (sorted_cards[0].rank != sorted_cards[1].rank or
        sorted_cards[2].rank != sorted_cards[3].rank or
        sorted_cards[4].rank != sorted_cards[5].rank):
        return False
    
    # Extract the rank values of the three pairs
    r1 = RankOrder[sorted_cards[0].rank]  # rank of first pair
    r2 = RankOrder[sorted_cards[2].rank]  # rank of second pair
    r3 = RankOrder[sorted_cards[4].rank]  # rank of third pair
    
    # Check if the pairs are in consecutive rank order
    return (r2 == r1 + 1) and (r3 == r2 + 1)
