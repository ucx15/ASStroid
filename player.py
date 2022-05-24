import pygame
from settings import *


class DefaultShip:
	def __init__(self, pos, img):
		# Location
		self.pos = pos
		self.orig_pos = Vec(pos)
		self.vel = Vec()
		self.acc = Vec()
		self.thrust = THRUST
		self.mass = MASS

		# Rotation
		self.head = Vec()
		self.angle = 0
		self.ang_max = ANGULAR_VEL
		self.braking = BRAKES

		# Art
		self.img = img
		self.img_dynamic = img
		self.rect = self.img_dynamic.get_rect()

	def size(self):
		return Vec(self.img_dynamic.get_size())

	def retard(self, amt=.95):
		self.vel *= amt

	def apply_force(self, f):
		self.acc += f / self.mass

	def motion(self, dt, keys, offset=90):
		w, s, a, d, r, spc, lctrl = [
									keys[pygame.K_w],
									keys[pygame.K_s],
									keys[pygame.K_a],
									keys[pygame.K_d],
									keys[pygame.K_r],
									keys[pygame.K_SPACE],
									keys[pygame.K_LCTRL]]

		angle = self.angle + offset
		self.head.from_polar([1, -angle])

		if w:
			self.apply_force(self.head * self.thrust)
		if a:
			self.angle += self.ang_max * dt
		if s:
			self.apply_force(-self.head * self.thrust)
		if d:
			self.angle -= self.ang_max * dt
		if spc:
			self.retard(self.braking)
		if lctrl and r:
			self.pos = self.orig_pos
			self.vel.update()
			self.angle = 0

	def edges(self):
		sx, sy = self.size() / 2
		if self.pos.x < sx:
			self.pos.x = sx
			self.vel.x *= -1
			self.retard()
		elif self.pos.x > (SCR_WIDTH - sx):
			self.pos.x = SCR_WIDTH - sx
			self.vel.x *= -1
			self.retard()
		if self.pos.y < sy:
			self.pos.y = sy
			self.vel.y *= -1
			self.retard()
		elif self.pos.y > (SCR_HEIGHT - sy):
			self.pos.y = SCR_HEIGHT - sy
			self.vel.y *= -1
			self.retard()

	def update(self, keys, dt):
		self.motion(dt, keys)
		self.edges()
		self.vel += self.acc * dt
		self.pos += self.vel * dt
		self.acc.update()

		self.img_dynamic = pygame.transform.rotozoom(self.img, round(self.angle), 1)
		self.rect = self.img_dynamic.get_rect(center=(round(self.pos.x), round(self.pos.y)))

	def show(self, surface, debug=False):
		surface.blit(self.img_dynamic, self.rect)

		if debug:
			const = 50
			x, y = round(self.pos.x), round(self.pos.y)
			pygame.draw.rect(surface, "yellow", self.rect, 2, 2)
			pygame.draw.circle(surface, "white", (x, y), 5)
			head_x, head_y = self.head.x * const, self.head.y * const
			vel_x, vel_y = self.vel.x, self.vel.y
			pygame.draw.line(surface, "green", (x, y), (x + head_x, y + head_y), 2)
			pygame.draw.line(surface, "cyan", (x, y), (x + vel_x, y + vel_y), 2)


class UcxI(DefaultShip):
	def __init__(self, pos):
		img = pygame.transform.scale(pygame.image.load("Assets/SpaceShip.png").convert_alpha(), (60, 135))
		super().__init__(pos, img)
