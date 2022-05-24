from pygame import Vector2 as Vec


class Coordinate:
	def __init__(self, w, h):
		self.W = w
		self.H = h
		self.OX = self.W // 2
		self.OY = self.H // 2
		self.SIZE = Vec(self.W, self.H)
		self.CENTER = Vec(self.OX, self.OY)

	def ns_to_ss(self, v: Vec) -> Vec:
		"""Convert NormalizedSpace to ScreenSpace """
		new_v = (Vec(v.x, -v.y) + Vec(1, 1)) / 2
		return new_v * self.SIZE.elementwise()

	def ss_to_ns(self, v: Vec) -> Vec:
		"""Convert ScreenSpace to NormalizedSpace"""
		new_v = (2 * v / self.SIZE.elementwise()) - Vec(1, 1)
		return Vec(new_v.x, -new_v.y)
