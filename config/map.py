# game setup
WIDTH    = 1408	
HEIGTH   = 848
FPS      = 60
TILESIZE = 64

# player details
SPEED=5
YULU_SPEED=8
GRASS_SPEED=2

ENERGY_RATE=0.01
YULU_ENERGY_RATE=0.01
YULU_BLINK_THRESHOLD=400
GRASS_ENERGY_RATE=0.01
FOOD_ENERGY=20
ENERGY_BLINK_THRESHOLD=20
YULU_BILL=0.05

STARTING_COINS=500
COIN_VALUE=50
HOSPITAL_FEES=100
FOOD_FEES=10

DOG_BITE_ENERGY=5
DOG_SPEED=1


# ui 
BAR_HEIGHT = 20
ENERGY_BAR_WIDTH = 200
UI_FONT = './assets/map_mode/font/joystix.ttf'
UI_FONT_SIZE = 18

# ui colors
TEXT_COLOR = '#EEEEEE'
ENERGY_COLOR = 'red'
ENERGY_COLOR_LIGHT = 'pink'
UI_BORDER_COLOR_ACTIVE = 'gold'
UI_BG_COLOR = '#222222'
UI_BG_COLOR_LIGHT = 'grey'
UI_BORDER_COLOR = '#111111'
HIGHLIGHT_COLOR='yellow'
CHECKPOINT_COLOR='blue'


TOTAL_TIMER=500
ENDING_POINT = 'guesthouse'
CHECKPOINTS = ['hostel1', 'lib', 'cycle_shop', 'guesthouse']
MESSGAES = ['TASK 1', 'TASK 2', 'TASK 3', 'TASK 4']
POINTS = [100, 100, 100, 100]
# LEVELS = [    
#     {
#         'points':200,
#         'start':'hospital',
#         'end':'amul',
#         'story':'story',
#         'task':'task',
#         'first_message_on_top':'Go to the Hospital',
#         'second_message_on_top':'Go to Amul'
#     },
#     {
#         'points':200,
#         'start':'hostel1',
#         'end':'shop',
#         'story':'story',
#         'task':'task',
#         'first_message_on_top':'Go to Hostel 1',
#         'second_message_on_top':'Go to the Shop'
#     },
# ]

HOSTELS = {
    1:'Jwala',
    2:'Aravali',
    3:'Karakoram',
    4:'Nilgiri',
    5:'Satpura',
    6:'Girnar',
    7:'Udaigiri',
    8:'Vindy',
    9:'Kumaon',
    10:'Zanskar',
    11:'Shivalik',
    12:'Himadri'
}

WORLD_MAP_1 = [
['t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t'],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ',' ','t','t','v','t',' ','G5','g','g',' ',' ','G6','g','g',' ',' ',' ',' ',' ',' ',' ',' ',' ','G7','g','g',' ',' ','G8','g','g',' '],
['t',' ',' ',' ',' ',' ','Y','h','h','v','t',' ','g','g','g',' ',' ','g','g','g',' ',' ',' ',' ',' ',' ',' ',' ',' ','g','g','g',' ',' ','g','g','g',' '],
['t',' ',' ',' ',' ',' ',' ','t','t','v','t',' ','g','g','g',' ',' ','g','g','g',' ',' ',' ',' ',' ',' ','Y',' ',' ','g','g','g',' ',' ','g','g','g',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ','t','v','t',' ',' ','t','v','t',' ',' ',' ',' ',' ','t','v','t',' ','t','v','t',' ',' ','t','v','t',' '],
['t',' ',' ','G1','g','g',' ',' ','t','v','t','t','t','v','t','t','t','t','v','t','t','t','t','t','t','t','v','t','t','t','v','t','t','t','t','v','t',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','v','h','h','h','h','h','h','h','h','h','t',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t','t','t','t','t','t','v','t','t','t','t','t','t','t','t','t','v','t','t','t','t','t','t','t','t','t','t',' '],
['t',' ',' ','t','v','t','t','t','t','v','t',' ','T',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','h','h','h','h','v','t',' ',' ',' ',' ',' ','v','t','G9',' ','g',' ',' ',' ',' ','t','v','t','G10',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','t','t','t','t','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ','v','h','g',' ','g',' ',' ',' ',' ','t','v','h',' ',' ','g',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','G2','g','g',' ',' ','t','c','t',' ',' ',' ',' ','h','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ','C',' ','t','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ','h','h','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','t','t','t','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ','t','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','h','h','h','h','v','t',' ',' ',' ',' ',' ','v','t','G11',' ','g',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','t','t','t','t','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ','H',' ',' ',' ',' ',' ','Cs',' ',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t','B','b',' ',' ',' ','v','h','g',' ','g',' ','R',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','G3','g','g',' ',' ','t','v','h','b','b',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ','h','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','p','t','v','t','t','t','v','t','t','t','t',' ',' ',' ',' ','t','v','t','t','t','v','t','t','t','t','t','v','t'],
['t',' ',' ','g','g','g',' ',' ','t','v','h','D','h','h','h','h','v','h','h','h','h','h','h','h','h','h','v','h','h','h','h','h','h','h','h','h','h','h'],
['t',' ',' ','t','v','t','t','t','t','v','t','t','t','t','t','t','v','t','t','t','t','t','t','t','t','t','v','t','t','t','t','t','t','t','v','t','t','t'],
['t',' ',' ','t','v','h','h','h','h','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ','F',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','t','t','t','t','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','G4','g','g',' ',' ','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','t','t','t','t','v','t',' ',' ',' ',' ','t','v','h','Y',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','h','h','h','h','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','t','t','t','t','t','v','t',' ',' ',' ',' ',' ','S','s','s','s',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ','s','s','s','s',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ',' ','t','t','v','t',' ',' ',' ',' ',' ','s','s','s','s',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ','Y','h','h','v','t',' ',' ',' ',' ',' ','s','s','s','s',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ',' ','t','t','v','t',' ',' ',' ',' ',' ','v',' ',' ',' ',' ',' ',' ',' ',' ','t','v','h','h','h','h','h','h','h','h','h','h','h'],
['t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t'],
]

WORLD_MAP_2 = [
['t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','P',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t','G12','g','g','t','t','t',' ',' ',' ',' ',' ',' ',' ',' ',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t','g',' ','g','h','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t','g','g','g','t','v','h','Y',' ',' ',' ',' ',' ',' ',' ',' ','t'],
[' ',' ',' ','E','e','e','t','t','t','t','t','t','t','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ','t','v','t','v','t','t','t','t','t','t','t','t','t'],
[' ',' ',' ','e','e','e','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','t'],
[' ',' ',' ',' ',' ',' ','t','v','t','t','t','t','t','v',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ','t','v',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ','t','v',' ','I',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ','t','v','h','h','h','h',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ','Lh',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t','t',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','h','v',' ','t'],
[' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','h','h',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ','t','v','t','t',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ','Q',' ',' ',' ','v','t','t','t','t','t','v','t','t','t','t','t','t','t','t','v','t',' ',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ','v','h','h','h','h','h','h','h','h','h','h','h','h','h','h','v','t',' ',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ','v','t','t','t','t','t','t','v','t',' ',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ','v','t','A',' ',' ',' ',' ','L',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ','t','v','h','h','h','h','h','h','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ','v','h',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ','t','v',' ','X',' ',' ',' ','t','v',' ','t'],
['t','t','t','t','t','t','t','v','t','t','t','t','t','t','t','t','t','t','t','t','t','t','v','t',' ',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
['h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','t',' ',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ','t','v',' ','t'],
['t','v','t','t','t','t','t','t','t','t','t','v','t','t','t','t','v','t','v','t','t','t','t','t',' ',' ',' ',' ',' ','t','v',' ',' ','t','v','t','t','v',' ','t'],
['Bb',' ',' ',' ',' ',' ',' ',' ',' ',' ','Rr',' ',' ',' ',' ',' ','Y','h','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v',' ',' ','t','h','h','h','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v',' ',' ',' ','t','t','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v',' ',' ',' ',' ',' ',' ','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','G',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','h','h','h','h','h','h','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t','t','t','t','t','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','h','Y',' ',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t','v','t',' ',' ','t','v',' ','t'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t','v','t',' ',' ','t','v',' ','t'],
['h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','t'],
['t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t'],
]

WORLD_MAP = WORLD_MAP_1.copy()
for i,r2 in enumerate(WORLD_MAP_2):
    WORLD_MAP[i]=WORLD_MAP[i] + r2