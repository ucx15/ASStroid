import pygame
from UI import Text
from settings import *


class FirstPage:
	def __init__(self, fnt_title, fnt_plain):
		# Images
		self.asteroid_img = pygame.transform.scale(pygame.image.load("Assets/asteroid_img.png"), (75, 75))
		self.bholu_img = pygame.image.load("Assets/bholuEng.png").convert_alpha()

		# Texts
		title_string = "ASStroid Miner"
		guide_string = "Press 'F' to play"
		self.text_fp_title = Text(title_string, WHITE, fnt_title, CENTER)
		self.text_fp_guide = Text(guide_string, CYAN, fnt_plain, (OX, OY + 100))

	def show(self, surface):
		surface.blit(self.asteroid_img, (OX + 400, OY - 130))
		surface.blit(self.bholu_img, (10, SCR_HEIGHT - 177))
		self.text_fp_title.render(surface)
		self.text_fp_guide.render(surface)
