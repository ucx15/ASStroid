from random import randint

from player import UcxI
from asteroid import AsteroidLv1
from settings import *


class Level:
	def __init__(self):
		self.player = UcxI(Vec(OX, OY))
		self.obstacles = []

	def generate_obstacles(self):
		self.obstacles.append(AsteroidLv1(
			pos=Vec(randint(0, SCR_WIDTH), randint(0, SCR_HEIGHT)),
			acc=Vec(randint(-AS_THRUST, AS_THRUST), randint(-AS_THRUST, AS_THRUST))))

	def update(self, dt, keys):
		self.player.update(keys, dt)
		for obstacle in self.obstacles:
			obstacle.update(dt)

	def show(self, surface, debug=False):
		for obstacle in self.obstacles:
			obstacle.show(surface, debug)
		self.player.show(surface, debug)
