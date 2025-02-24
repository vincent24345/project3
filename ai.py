from rules import can_beat

def choose_card_to_play(bot_player, last_card):
    #sort the bot's hand 
    bot_player.hand.sort(key=lambda c: c.rank)

    for i, card in enumerate(bot_player.hand):
        if can_beat(card, last_card):
            return i  
    return None  
