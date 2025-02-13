import pygame

from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (90, 80))
        self.surf = pygame.transform.flip(self.surf, True, False)
        self.rect = self.surf.get_rect(topleft=position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

