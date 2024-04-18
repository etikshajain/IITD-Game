# game setup
WIDTH    = 1408	
HEIGTH   = 848
FPS      = 60
TILESIZE = 64

# player details
SPEED=4
YULU_SPEED=6
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


TOTAL_TIMER=5000
TIMER_BLINK_THRESHOLD=500
CHECKPOINTS = ['sac', 'lhc', 'hostel1', 'racing', 'hostel12', 'bank', 'guesthouse', 'main_building']
MESSGAES = ['Go to SAC to see how the Insti works', 'Go to LHC to File your Election Nomination', 'Go to Jwala to form Alliance', 'Go to racing ground to hold a public meeting', 'Go to Himadri to eavesdrop on opposition strategies', 'Withdraw money from the bank to organise rally', 'Hide in the guesthouse for some time', 'Reach main building for the final elections!!']
POINTS = [100, 100, 100, 100, 100, 100, 100, 100]

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
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ','t','v','5',' ',' ','t','v','6',' ',' ',' ',' ',' ','t','v','t',' ','t','v','7',' ',' ','t','v','8',' '],
['t',' ',' ','G1','g','g',' ',' ','t','v','t','t','t','v','t','t','t','t','v','t','t','t','t','t','t','t','v','t','t','t','v','t','t','t','t','v','t',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','v','h','h','h','h','h','h','h','h','h','t',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t','t','t','t','t','t','v','t','t','t','t','t','t','t','t','t','v','t','t','t','t','t','t','t','t','t','t',' '],
['t',' ',' ','t','v','1','t','t','t','v','t',' ','T',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','h','h','h','h','v','t',' ',' ',' ',' ',' ','v','t','G9',' ','g',' ',' ',' ',' ','t','v','t','G10',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','t','t','t','t','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','10',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ','v','h','g',' ','g',' ',' ',' ',' ','t','v','h',' ',' ','g',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','G2','g','g',' ',' ','t','c','t',' ',' ',' ',' ','h','v','9',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ','C',' ','t','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ','h','h','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','2','t','t','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ','t','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','h','h','h','h','v','t',' ',' ',' ',' ',' ','v','t','G11',' ','g',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','t','t','t','t','t','v','t',' ',' ',' ',' ',' ','v','11',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ','H',' ',' ',' ',' ',' ','Cs',' ',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t','B','b',' ',' ',' ','v','h','g',' ','g',' ','R',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','G3','g','g',' ',' ','t','v','h','b','b',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ','h','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','p','t','v','t','t','t','v','t','t','t','t',' ',' ',' ',' ','t','v','t','t','t','v','t','t','t','t','t','v','t'],
['t',' ',' ','g','g','g',' ',' ','t','v','h','D','h','h','h','h','v','h','h','h','h','h','h','h','h','h','v','h','h','h','h','h','h','h','h','h','h','h'],
['t',' ',' ','t','v','3','t','t','t','v','t','t','t','t','t','t','v','t','t','t','t','t','t','t','t','t','v','t','t','t','t','t','t','t','v','t','t','t'],
['t',' ',' ','t','v','h','h','h','h','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ','v',' ',' ',' '],
['t',' ',' ','t','t','t','t','t','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ','F',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','G4','g','g',' ',' ','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','4','t','t','t','v','t',' ',' ',' ',' ','t','v','h','Y',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
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
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t','g','g','g','12','v','h','Y',' ',' ',' ',' ',' ',' ',' ',' ','t'],
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
[' ','v',' ',' ',' ',' ',' ',' ',' ',' ',' ','v',' ',' ',' ',' ','Y','h','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v',' ',' ','t','h','h','h','v',' ','t'],
['Bb',' ',' ',' ',' ',' ',' ',' ',' ',' ','Rr',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ','t','v',' ',' ',' ','t','t','t','v',' ','t'],
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