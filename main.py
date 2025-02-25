import pygame
from game import create_deck, deal_cards
from player import Player
from ai import choose_card_to_play
from rules import can_beat, check_winner

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Thirteen")

    #deck created
    deck = create_deck()
    hands = deal_cards(deck)
    players = [Player(f"Player {i+1}", hand) for i, hand in enumerate(hands)]

    #player 1 for user
    human_player_index = 0

    #variables
    current_player_index = 0
    last_card = None 
    winner = None

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((34, 139, 34))  

        #check if there's a winner
        winner = check_winner(players)
        if winner:
            print(f"{winner.name} wins!")
            running = False
            break

        #current player
        current_player = players[current_player_index]

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #check mouse click for user
            if current_player_index == human_player_index and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #card width and height
                card_width, card_height = 60, 90  
                start_x, start_y = 50, 500
                spacing = 30

                #determine which card was clicked
                for i, card in enumerate(current_player.hand):
                    card_x = start_x + i * spacing
                    card_y = start_y
                    if card_x <= x <= card_x + card_width and card_y <= y <= card_y + card_height:
                        #check if can beat
                        if can_beat(card, last_card):
                            # Play the card
                            played_card = current_player.play_card(i)
                            last_card = played_card
                            print(f"{current_player.name} played {played_card.rank} of {played_card.suit}")
                            # Move to next player
                            current_player_index = (current_player_index + 1) % len(players)
                        else:
                            print("Invalid move! Cannot beat the last card.")
                        break

        #bot turn
        if current_player_index != human_player_index:
            card_index = choose_card_to_play(current_player, last_card)
            if card_index is not None:
                played_card = current_player.play_card(card_index)
                last_card = played_card
                print(f"{current_player.name} played {played_card.rank} of {played_card.suit}")
            else:
                 # Bot passes
                print(f"{current_player.name} passes.")
                consecutive_passes += 1

                # If all players pass in a row, clear the table
                if consecutive_passes >= len(players):
                    print("All players have passed. Clearing the table.")
                    last_card = None
                    consecutive_passes = 0
            
            #next turn
            current_player_index = (current_player_index + 1) % len(players)

        #human hand
        draw_player_hand(screen, players[human_player_index].hand, (50, 500))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

def draw_player_hand(screen, hand, start_pos):
    x, y = start_pos
    spacing = 30
    card_width, card_height = 60, 90  
    for card in hand:
        card.draw(screen, (x, y))
        x += spacing

if __name__ == "__main__":
    main()
