import pygame
from game import create_deck, deal_cards
from player import Player
from ai import choose_card_to_play
from rules import can_beat, check_winner
from card import Card  

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Thirteen")

    # Create and deal the deck
    deck = create_deck()
    hands = deal_cards(deck)
    players = [Player(f"Player {i+1}", hand) for i, hand in enumerate(hands)]

    # Player 1 is the human player
    human_player_index = 0
    current_player_index = 0
    last_card = None
    winner = None
    consecutive_passes = 0  # Tracks consecutive passes

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((34, 139, 34))  # Green table background

        # Check if there is a winner
        winner = check_winner(players)
        if winner:
            print(f"{winner.name} wins!")
            running = False
            break

        current_player = players[current_player_index]

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Human player's turn
            if current_player_index == human_player_index:

                # Pass logic
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    print(f"{current_player.name} passes.")
                    consecutive_passes += 1  # Update first

                    if consecutive_passes >= len(players) or (last_card and last_card.rank == "2"):
                        print("All players have passed. Clearing the table.")
                        last_card = None
                        consecutive_passes = 0  # Reset pass counter

                    # Move to the next player
                    current_player_index = (current_player_index + 1) % len(players)

                # Card selection logic (mouse click)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    # Define variables before use
                    card_width, card_height = 60, 90
                    start_x, start_y = 50, 500
                    spacing = 30

                    # Determine which card was clicked
                    for i, card in enumerate(current_player.hand):
                        card_x = start_x + i * spacing
                        card_y = start_y

                        if card_x <= x <= card_x + card_width and card_y <= y <= card_y + card_height:
                            if can_beat(card, last_card):  # Check if the move is valid
                                played_card = current_player.play_card(i)
                                last_card = played_card
                                print(f"{current_player.name} played {played_card.rank} of {played_card.suit}")

                                # Check for winner after playing
                                if len(current_player.hand) == 0:
                                    print(f"{current_player.name} wins!")
                                    running = False
                                    break

                                # Reset passes & move to next player
                                consecutive_passes = 0
                                current_player_index = (current_player_index + 1) % len(players)
                            else:
                                print("Invalid move! Cannot beat the last card.")
                            break

        # AI Turn
        if current_player_index != human_player_index:
            card_index = choose_card_to_play(current_player, last_card)
            if card_index is not None:
                played_card = current_player.play_card(card_index)
                last_card = played_card
                print(f"{current_player.name} played {played_card.rank} of {played_card.suit}")

                # Check for winner after playing
                if len(current_player.hand) == 0:
                    print(f"{current_player.name} wins!")
                    running = False
                    break

                consecutive_passes = 0  # Reset pass counter
            else:
                # Bot passes
                print(f"{current_player.name} passes.")
                consecutive_passes += 1

                # If all players pass, clear the table
                if consecutive_passes >= len(players):
                    print("All players have passed. Clearing the table.")
                    last_card = None
                    consecutive_passes = 0

            # Move to the next player
            current_player_index = (current_player_index + 1) % len(players)

        # Draw the human player's hand
        draw_player_hand(screen, players[human_player_index].hand, (50, 500))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

def draw_player_hand(screen, hand, start_pos):
    """Draws the human player's hand at the specified position."""
    x, y = start_pos
    spacing = 30  # Space between cards

    for card in hand:
        card.draw(screen, (x, y))
        x += spacing

if __name__ == "__main__":
    main()
