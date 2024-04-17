import os
import sys
import socket
from _thread import *
import pickle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.fighter import Fighter
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

WARRIOR_SIZE = 128
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 128
WIZARD_SCALE = 4
WIZARD_OFFSET = [72, 56]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

WARRIOR_ANIMATION_STEPS = [5, 9, 8, 4, 5, 4, 2, 7, 2, 6]
WIZARD_ANIMATION_STEPS = [6, 9, 8, 4, 5, 4, 2, 9, 3, 6]

players = [None, None]
def threaded_client(conn, player):
    if player == 0:
        players[player] = Fighter(1, 200, 310, False, WARRIOR_DATA, WARRIOR_ANIMATION_STEPS)
    else:
        players[player] = Fighter(2, 1300, 310, True, WIZARD_DATA, WIZARD_ANIMATION_STEPS)
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