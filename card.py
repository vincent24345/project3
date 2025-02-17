import pygame

class Card:
    def __init__(self, suit, rank, image_path):
        self.suit = suit
        self.rank = rank
        self.image = pygame.image.load(image_path)
    
    def draw(self, screen, pos):
        screen.blit(self.image, pos)
