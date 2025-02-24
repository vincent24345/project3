import pygame
from game import create_deck, deal_cards
from player import Player
from ai import choose_card_to_play
from rules import can_beat, check_winner

def main():
    # Initialize Pygame and set up the window
    pygame.init()
    WIDTH, HEIGHT = 1200, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Card Game")

    # Create a deck and deal the cards among four players
    deck = create_deck()
    hands = deal_cards(deck)
    players = [Player(f"Player {i+1}", hand) for i, hand in enumerate(hands)]

    clock = pygame.time.Clock()
    running = True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a green background (like a card table)
        screen.fill((34, 139, 34))

        # Draw Player 1's hand at the bottom of the screen
        x = 50  # Starting x position
        y = 500  # y position for Player 1's hand
        for card in players[0].hand:
            card.draw(screen, (x, y))
            x += 60  # Space between cards

        pygame.display.flip()  # Update the display
        clock.tick(30)  # Limit the frame rate to 30 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
