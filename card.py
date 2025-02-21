import pygame

class Card:
    def __init__(self, suit, rank, image_path):
        self.suit = suit
        self.rank = rank
        original_image = pygame.image.load(image_path)
        
        scaled_width, scaled_height = 80, 120
        self.image = pygame.transform.scale(original_image, (scaled_width, scaled_height))
        
    def draw(self, screen, pos):
        screen.blit(self.image, pos)
