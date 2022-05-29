from random import randint

import pygame

from player import UcxI
from asteroid import AsteroidLv1
from settings import *


class Level:
	def __init__(self):
		self.player = UcxI(Vec(OX, OY))
		self.obstacles = []
		self.generate_obstacles()

		self.padding = round(SHIFT_PADDING/100 * SCR_WIDTH)
		self.cam_padding = round(CAM_PADDING/100 * SCR_WIDTH)

		self.center_pos = Vec(SCR_WIDTH // 2, SCR_HEIGHT // 2)
		self.center_rect = pygame.Rect((0,0), (self.cam_padding, self.cam_padding))
		self.center_rect.center = self.center_pos

		self.padding_rect = pygame.Rect(
			(self.padding, self.padding),
			(SCR_WIDTH - 2 * self.padding, SCR_HEIGHT - 2 * self.padding))

		self.global_speed = Vec()

	def generate_obstacles(self):
		for i in range(5):
			self.obstacles.append(AsteroidLv1(
				pos=Vec(randint(0, SCR_WIDTH), randint(0, SCR_HEIGHT)),
				acc=Vec(randint(-AS_THRUST, AS_THRUST), randint(-AS_THRUST, AS_THRUST))))

	def edges(self):
		sx, sy = self.player.size()
		vel = self.player.vel

		for obstacle in self.obstacles:
			edge = False

			if self.player.pos.x < self.padding + sx:
				self.player.pos.x = sx + self.padding
				edge = True

			elif self.player.pos.x > (SCR_WIDTH - sx - self.padding):
				self.player.pos.x = SCR_WIDTH - sx - self.padding
				edge = True

			if self.player.pos.y < self.padding + sy:
				self.player.pos.y = sy + self.padding
				edge = True

			elif self.player.pos.y > (SCR_HEIGHT - sy - self.padding):
				self.player.pos.y = SCR_HEIGHT - sy - self.padding
				edge = True

			if edge:
				self.global_speed -= vel

	def cam_center(self):
		if not self.player.rect.colliderect(self.center_rect):
			center_dir = (self.player.pos - self.center_pos)
			if center_dir:
				center_dir = center_dir.normalize()
				self.player.pos -= center_dir * CAM_SPEED
				for obstacle in self.obstacles:
					obstacle.pos += center_dir * CAM_SPEED

	def update(self, dt, keys):
		self.edges()
		# self.cam_center()

		self.player.update(keys, dt)
		for obstacle in self.obstacles:
			if keys[pygame.K_SPACE]:
				obstacle.vel.update()
			obstacle.pos += self.global_speed * dt
			obstacle.update(dt)
		self.global_speed.update()

	def show(self, surface, debug=False):
		for obstacle in self.obstacles:
			obstacle.show(surface, debug)
		self.player.show(surface, debug)
		if debug:
			pygame.draw.rect(surface, (255, 0, 0), self.padding_rect, 5)
			pygame.draw.rect(surface, (255, 0, 0), self.center_rect, 5)
