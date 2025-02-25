#initialise the rank order

RankOrder = {
    "2" : 15, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, 
    "8" : 8, "9" : 9, "10" : 10, "Jack" : 11, "Queen" : 12, 
    "King" : 13, "Ace" : 14
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
    