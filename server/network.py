import socket
import pickle
import pygame
from config.server import *

class Network:
  def __init__(self):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server = IP_ADDR
    self.port = PORT
    self.addr = (self.server, self.port)
    self.p = self.connect()

  def getPlayer(self):
    return self.p

  def connect(self):
    try:
      self.client.connect(self.addr)
      return pickle.loads(self.client.recv(BUFFER_SIZE))
    except:
      print("Error")

  def send(self, data):
    try:
      self.client.send(pickle.dumps(data))
      return pickle.loads(self.client.recv(BUFFER_SIZE))
    except socket.error as e:
      print(e)