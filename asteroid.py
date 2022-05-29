import pygame
from settings import *


class DefaultAsteroid:
	w = round(AS_SIZE / 100 * SCR_WIDTH)
	h = round(1.77 * w)

	def __init__(self, pos, acc, img):
		# Location
		self.pos = pos
		self.orig_pos = Vec(pos)
		self.vel = Vec()
		self.acc = acc
		self.mass = AS_MASS

		# Art
		self.img = img
		self.img_dynamic = img
		self.rect = self.img_dynamic.get_rect()
		self.sx, self.sy = self.size() / 2

	def size(self):
		return Vec(self.img_dynamic.get_size())

	def apply_force(self, f):
		self.acc += f / self.mass

	def update(self, dt):
		self.vel += self.acc * dt
		self.pos += self.vel * dt
		self.acc.update()
		self.rect.center = round(self.pos.x), round(self.pos.y)

	def show(self, surface, debug=False):
		surface.blit(self.img_dynamic, self.rect)

		if debug:
			const = 50
			x, y = round(self.pos.x), round(self.pos.y)
			pygame.draw.rect(surface, "yellow", self.rect, 2, 2)
			pygame.draw.circle(surface, "white", (x, y), 5)
			vel_x, vel_y = self.vel.x, self.vel.y
			pygame.draw.line(surface, "cyan", (x, y), (x + vel_x, y + vel_y), 2)


class AsteroidLv1(DefaultAsteroid):
	def __init__(self, pos, acc):
		img = pygame.transform.scale(pygame.image.load("Assets/Asteroid.png").convert_alpha(), (self.w, self.h))
		super().__init__(pos, acc, img)
