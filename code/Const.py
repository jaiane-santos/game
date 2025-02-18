import pygame

C_ORANGE = (255, 165, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 125)
C_GREEN = (0,255,0)
C_CYAN = (0,255,255)


EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2


ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 2,
    'Level1Bg2': 3,
    'Level1Bg3': 4,
    'Level1Bg4': 5,
    'Level1Bg5': 6,
    'Level2Bg0': 1,
    'Level2Bg1': 2,
    'Level2Bg2': 3,
    'Level2Bg3': 4,
    'Level2Bg4': 5,
    'Level2Bg5': 6,
    'Level2Bg6': 7,
    'Level2Bg7': 8,
    'Level2Bg8': 9,
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
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Level2Bg6': 999,
    'Level2Bg7': 999,
    'Level2Bg8': 999,
    'Player1': 30,
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

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level2Bg7': 0,
    'Level2Bg8': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
    'Enemy3': 1,
    'Enemy3Shot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level2Bg7': 0,
    'Level2Bg8': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 150,
    'Enemy2Shot': 0,
    'Enemy3': 125,
    'Enemy3Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 15,
    'Player2': 15,
    'Enemy1': 150,
    'Enemy2': 100,
    'Enemy3': 170,
}


MENU_OPTION = ( 'NEW GAME 1P (DEMO)',
                'NEW GAME 2P - COOP (DEMO)',
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

TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 40000

WIN_WIDTH = 700
WIN_HEIGHT = 480
