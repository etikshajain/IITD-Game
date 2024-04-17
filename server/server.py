import os
import sys
import socket
from _thread import *
import pickle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.fighter import Fighter
from src.player import Player
from config.main import SAMURAI1_ANIMATION_LIST,SAMURAI2_ANIMATION_LIST
from config.main import SAMURAI1_DATA,SAMURAI2_DATA
from config.main import SCREEN_HEIGHT,SCREEN_WIDTH,CHARACTER_X_OFFSET,CHARACTER_Y_OFFSET
from config.server import * # server params

ip = IP_ADDR
port = PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((ip, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [None, None]
def threaded_client(conn, player):
    if player == 0:
        players[player] = Fighter(1, CHARACTER_X_OFFSET, SCREEN_HEIGHT-CHARACTER_Y_OFFSET, False, SAMURAI1_DATA, SAMURAI1_ANIMATION_LIST)
    else:
        players[player] = Fighter(2, SCREEN_WIDTH-CHARACTER_X_OFFSET, SCREEN_HEIGHT-CHARACTER_Y_OFFSET, True, SAMURAI2_DATA, SAMURAI2_ANIMATION_LIST)
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(BUFFER_SIZE))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                # print("Received: ", data)
                # print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1