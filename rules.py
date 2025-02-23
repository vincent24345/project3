#initialise the rank order

RankOrder = {
    "2" : 14, "3" : 1, "4" : 2, "5" : 3, "6" : 4, "7" : 5, 
    "8" : 6, "9" : 7, "10" : 8, "Jack" : 9, "Queen" : 10, 
    "King" : 11, "Ace" : 12
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
    