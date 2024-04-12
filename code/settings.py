# game setup
WIDTH    = 1408	
HEIGTH   = 848
FPS      = 60
TILESIZE = 64

WORLD_MAP_1 = [
['t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t'],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ',' ','t','t','v','t',' ','G','g','g',' ',' ','G','g','g',' ',' ',' ',' ',' ',' ',' ',' ',' ','G','g','g',' ',' ','G','g','g',' '],
['t',' ',' ',' ',' ',' ','Y','h','h','v','t',' ','g','g','g',' ',' ','g','g','g',' ',' ',' ',' ',' ',' ',' ',' ',' ','g','g','g',' ',' ','g','g','g',' '],
['t',' ',' ',' ',' ',' ',' ','t','t','v','t',' ','g','g','g',' ',' ','g','g','g',' ',' ',' ',' ',' ',' ','Y',' ',' ','g','g','g',' ',' ','g','g','g',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ','t','v','t',' ',' ','t','v','t',' ',' ',' ',' ',' ','t','v','t',' ','t','v','t',' ',' ','t','v','t',' '],
['t',' ',' ','G','g','g',' ',' ','t','v','t','t','t','v','t','t','t','t','v','t','t','t','t','t','t','t','v','t','t','t','v','t','t','t','t','v','t',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','v','h','h','h','h','h','h','h','h','h','t',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t','t','t','t','t','t','v','t','t','t','t','t','t','t','t','t','v','t','t','t','t','t','t','t','t','t','t',' '],
['t',' ',' ','t','v','t','t','t','t','v','t',' ','T',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','h','h','h','h','v','t',' ',' ',' ',' ',' ','v','t','G',' ','g',' ',' ',' ',' ','t','v','t','G',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','t','t','t','t','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ','v','h','g',' ','g',' ',' ',' ',' ','t','v','h',' ',' ','g',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','G','g','g',' ',' ','t','v','t',' ',' ',' ',' ','h','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ','C',' ','t','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ','h','h','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','t','t','t','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ','t','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','v','h','h','h','h','v','t',' ',' ',' ',' ',' ','v','t','G',' ','g',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','t','t','t','t','t','v','t',' ',' ',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ','H',' ',' ',' ',' ',' ','Cs',' ',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t','B','b',' ',' ',' ','v','h','g',' ','g',' ','R',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','G','g','g',' ',' ','t','v','h','b','b',' ',' ',' ','v','t',' ',' ',' ',' ',' ',' ',' ','h','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','g','g','g',' ',' ','t','v','p','t','v','t','t','t','v','t','t','t','t','t',' ',' ',' ','t','v','t','t','t','v','t','t','t','t','t','v','t'],
['t',' ',' ','g','g','g',' ',' ','t','v','h','h','h','h','h','h','v','h','h','h','h','h','h','h','h','h','v','h','h','h','h','h','h','h','h','h','h','h'],
['t',' ',' ','t','v','t','t','t','t','v','t','t','t','t','t','t','v','t','t','t','t','t','t','t','t','t','v','t','t','t','t','t','t','t','v','t','t','t'],
['t',' ',' ','t','v','h','h','h','h','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ','F',' ',' ',' ',' ',' ',' '],
['t',' ',' ','t','t','t','t','t','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['t',' ',' ','G','g','g',' ',' ','t','v','t',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ','t','v','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
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
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','P',' ',' ',' ',' ',' ',' ',' ',' ','t','v','t','G','g','g','t','t','t',' ',' ',' ',' ',' ',' ',' ',' ',' ','t'],
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