import pygame
from player import UcxI
from settings import *


class Level:
	def __init__(self):
		self.player = UcxI(Vec(OX, OY))

	def update(self, dt, keys):
		self.player.update(keys, dt)

	def show(self, surface, debug=False):
		self.player.show(surface, debug)
