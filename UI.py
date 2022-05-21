class Text:
	def __init__(self, text, color, font_obj, loc, aa=1):
		self.text, self.color, self.font_obj = text, color, font_obj
		self.x, self.y = loc
		self.loc = loc
		self.aa = aa

	def copy(self):
		return Text(self.text, self.color, self.font_obj, self.loc, self.aa)

	def get_textsurf(self):
		return self.font_obj.render(self.text, self.aa, self.color)

	def render(self, surf, top=0):
		txt_srf = self.get_textsurf()
		w = h = 0
		if not top:
			w, h = txt_srf.get_width(), txt_srf.get_height()

		surf.blit(self.get_textsurf(), (self.x - w / 2, self.y - h / 2))
