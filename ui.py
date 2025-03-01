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

def show_winner_screen(screen, winner):
    screen.fill((0, 0, 0))  # Clear screen
    font = pygame.font.Font(None, 50)
    
    # Display winner text
    text = font.render(f"{winner.name} Wins!", True, (255, 255, 255))
    screen.blit(text, (300, 200))

    # Draw restart button
    pygame.draw.rect(screen, (0, 255, 0), (300, 300, 200, 50))
    button_text = font.render("Restart", True, (0, 0, 0))
    screen.blit(button_text, (350, 310))

    pygame.display.flip()

def restart_screen(screen):
    font = pygame.font.Font(None, 50)
    while True:
        screen.fill((0, 0, 0))  # Clear screen
        text = font.render("Game Over!", True, (255, 255, 255))
        screen.blit(text, (300, 200))

        # Draw restart button
        pygame.draw.rect(screen, (0, 255, 0), (300, 300, 200, 50))
        button_text = font.render("Restart", True, (0, 0, 0))
        screen.blit(button_text, (350, 310))
        
        pygame.display.flip()  # Update display each loop iteration
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                pygame.quit()
                exit()  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 300 <= x <= 500 and 300 <= y <= 350:  # Restart button clicked
                    return True  # Restart game
        pygame.time.delay(100)  # Prevent CPU overuse

