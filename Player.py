import pygame

Vec = pygame.Vector2


class PlayerObject:
	def __init__(self, pos, img):
		# Location
		self.pos = pos
		self.orig_pos = Vec(pos)
		self.vel = Vec()
		self.acc = Vec()
		self.thrust = 1_000
		self.mass = 2

		# Rotation
		self.head = Vec()
		self.angle = 0
		self.ang_max = 2
		self.braking = .98

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

	def motion(self, keys, offset=90):
		w, s, a, d, r, spc, lctrl = [keys[pygame.K_w],
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
			self.angle += self.ang_max
		if s:
			self.apply_force(-self.head * self.thrust)
		if d:
			self.angle -= self.ang_max
		if spc:
			self.retard(self.braking)
		if lctrl and r:
			self.pos = self.orig_pos
			self.vel.update()
			self.angle = 0

	def edges(self, width, height):
		sx, sy = self.size() / 2
		if self.pos.x < sx:
			self.pos.x = sx
			self.vel.x *= -1
			self.retard()
		elif self.pos.x > (width - sx):
			self.pos.x = width - sx
			self.vel.x *= -1
			self.retard()
		if self.pos.y < sy:
			self.pos.y = sy
			self.vel.y *= -1
			self.retard()
		elif self.pos.y > (height - sy):
			self.pos.y = height - sy
			self.vel.y *= -1
			self.retard()

	def update(self, w, h, keys, dt):
		self.motion(keys)
		self.edges(w, h)
		self.vel += self.acc * dt
		self.pos += self.vel * dt
		self.acc.update()

		self.img_dynamic = pygame.transform.rotozoom(self.img, self.angle, 1)
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
