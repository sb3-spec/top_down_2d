import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super.init(groups)
        
        self.image = pygame.image.load()