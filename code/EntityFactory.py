import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
              list_bg = []
              for i in range(3):
                  list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                  list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
              return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enimy1':
                return Enemy('Enimy1', (WIN_WIDTH + 10, random.randint(40 , WIN_HEIGHT - 40)))

            case 'Enimy2':
                return Enemy('Enimy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))