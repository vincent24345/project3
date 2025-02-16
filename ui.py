import pygame
from game import create_deck, deal_cards

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Thirteen - Tien Len")

# Load cards
deck = create_deck()
players = deal_cards(deck)

def draw_cards(player_hand, screen):
    x = 50
    for card in player_hand:
        card.draw(screen, x, 400)
        x += 50  # Space between cards

running = True
while running:
    screen.fill((34, 139, 34))  # Green background for card table

    # Draw player cards
    draw_cards(players[0], screen)  # Draw Player 1 cards

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
