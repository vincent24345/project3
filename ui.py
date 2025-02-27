import pygame

def handle_mouse_click(event, player):
    """Handles mouse clicks to play cards."""
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        card_width = 60  # Approximate card width
        selected_index = (x - 52) // card_width  # Determine which card was clicked
        if 0 <= selected_index < len(player.hand):
            return player.play_card(selected_index)
    return None

#define a skip button rectangle
SKIP_BUTTON = pygame.Rect(500, 400, 100, 50)  #adjust position and size

def draw_skip_button(screen):
    pygame.draw.rect(screen, (200, 0, 0), SKIP_BUTTON) 
    font = pygame.font.Font(None, 36)
    text = font.render("Skip", True, (255, 255, 255))
    screen.blit(text, (SKIP_BUTTON.x + 20, SKIP_BUTTON.y + 10))

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if SKIP_BUTTON.collidepoint(event.pos): 
                return "skip"
    return None
