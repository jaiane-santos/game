import pygame

COLOR_ORANGE = (255,165,0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 125)

EVENT_ENEMY = pygame.USEREVENT + 1


ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 2,
    'Level1Bg2': 3,
    'Level1Bg3': 4,
    'Level1Bg4': 5,
    'Level1Bg5': 6,
    'Player1': 2,
    'Player1Shot': 3,
    'Player2': 2,
    'Player2Shot': 3,
    'Enemy1': 2,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 3,
    'Enemy3': 1,
    'Enemy3Shot': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 90,
    'Enemy2Shot': 1,
    'Enemy3': 70,
    'Enemy3Shot': 1,
}


ENTITY_SHOT_DELAY = {
    'Player1': 15,
    'Player2': 15,
    'Enemy1': 150,
    'Enemy2': 100,
    'Enemy3': 170,
}


MENU_OPTION = ( 'NEW GAME 1P',
                'NEW GAME 2P - COOP',
                'SCORE',
                'EXIT'

)


PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                   'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                   'Player2': pygame.K_LCTRL}

SPAWN_TIME = 4000

WIN_WIDTH = 700
WIN_HEIGHT = 480
