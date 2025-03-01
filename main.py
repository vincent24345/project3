import pygame
from game import create_deck, deal_cards
from player import Player
from ai import choose_card_to_play
from rules import can_beat, check_winner
from card import Card  
from ui import draw_skip_button, handle_events, SKIP_BUTTON, show_winner_screen, restart_screen
import time

def handle_mouse_click(event, player, last_card):
    """Handles mouse clicks to play cards."""
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        card_width = 130
        spacing = 30
        start_x, start_y = 50, 500

        # Determine which card was clicked
        for i, card in enumerate(player.hand):
            card_x = start_x + i * spacing
            card_y = start_y

            if card_x <= x <= card_x + card_width and card_y <= y <= card_y + 90:  # 90 is card height
                print(f"Clicked on: {card.rank} of {card.suit}")

                # Ensure the move is valid before playing
                if last_card is None or can_beat(card, last_card):
                    return player.play_card(i)  # Remove and return the played card
                else:
                    print("Invalid move! Cannot play this card.")
    return None

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Thirteen")

    # Create and deal the deck
    deck = create_deck()
    hands = deal_cards(deck)
    players = [Player(f"Player {i+1}", hand) for i, hand in enumerate(hands)]

    human_player_index = 0
    current_player_index = 0
    last_card = None
    winner = None
    consecutive_passes = 0  

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((34, 139, 34))  # Green table background
        draw_skip_button(screen)
        draw_player_hand(screen, players[human_player_index].hand, (50, 500))

        current_player = players[current_player_index]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle skip button
            if event.type == pygame.MOUSEBUTTONDOWN and SKIP_BUTTON.collidepoint(event.pos):
                print(f"{current_player.name} skipped their turn.")
                consecutive_passes += 1  
                current_player_index = (current_player_index + 1) % len(players)

                if consecutive_passes >= len(players):
                    print("All players have passed. Clearing the table.")
                    last_card = None
                    consecutive_passes = 0  
                continue

            # Human player's turn (clicking to play)
            if current_player_index == human_player_index:
                played_card = handle_mouse_click(event, current_player, last_card)
                if played_card:
                    last_card = played_card
                    print(f"{current_player.name} played {played_card.rank} of {played_card.suit}")

                    # Reset pass count and move to next player
                    consecutive_passes = 0
                    current_player_index = (current_player_index + 1) % len(players)

        # AI Player Turn
        if current_player_index != human_player_index:
            card_index = choose_card_to_play(players[current_player_index], last_card)
            if card_index is not None:
                played_card = players[current_player_index].play_card(card_index)
                last_card = played_card
                print(f"{players[current_player_index].name} played {played_card.rank} of {played_card.suit}")
                consecutive_passes = 0  
            else:
                print(f"{players[current_player_index].name} passes.")
                consecutive_passes += 1  

                if consecutive_passes >= len(players):
                    print("All players have passed. Clearing the table.")
                    last_card = None
                    consecutive_passes = 0  

            current_player_index = (current_player_index + 1) % len(players)
        #game logic (handling player turns, checking for winner)
        winner = check_winner(players)
        
        if winner:
            show_winner_screen(screen, winner)
            running = restart_screen(screen)  #restart game once clicked


        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

def draw_player_hand(screen, hand, start_pos):
    """Draws the human player's hand at the specified position."""
    x, y = start_pos
    spacing = 30  

    for card in hand:
        card.draw(screen, (x, y))
        x += spacing

if __name__ == "__main__":
    while True:  
        main()


