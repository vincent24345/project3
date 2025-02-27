from rules import can_beat

def choose_card_to_play(bot_player, last_card):
    # Sort the bot's hand by rank (and suit if desired)
    bot_player.hand.sort(key=lambda c: c.rank)

    for i, card in enumerate(bot_player.hand):
        if can_beat(card, last_card):
            return i  # Return the index of the card to play
    return None  # No card can beat the last_card
