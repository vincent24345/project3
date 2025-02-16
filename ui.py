import pygame

def handle_mouse_click(event, player):
    """Handles mouse clicks to play cards."""
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        card_width = 60  # Approximate card width
        selected_index = (x - 50) // card_width  # Determine which card was clicked
        if 0 <= selected_index < len(player.hand):
            return player.play_card(selected_index)
    return None
