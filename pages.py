import pygame
from UI import Text
from settings import *


class FirstPage:
	def __init__(self, fnt_title, fnt_plain):
		# Images
		self.bholu1_img = pygame.image.load("Assets/bholuEng.png").convert_alpha()
		self.bholu2_img = pygame.image.load("Assets/BholuEngLogo.png").convert_alpha()

		# Texts
		title_string = "ASStroid Miner"
		guide_string = "Press 'F' to play"
		self.text_fp_title = Text(title_string, WHITE, fnt_title, CENTER)
		self.text_fp_guide = Text(guide_string, CYAN, fnt_plain, (OX, OY + 100))

	def show(self, surface):
		x_off = round((.5/100) * SCR_WIDTH)
		y_off = round((4/100) * SCR_HEIGHT)
		blit_pos1 = (x_off, SCR_HEIGHT - y_off - 135)
		blit_pos2 = (x_off + 125, SCR_HEIGHT - y_off - 135)
		surface.blit(self.bholu1_img, blit_pos1)
		surface.blit(self.bholu2_img, blit_pos2)
		self.text_fp_title.render(surface)
		self.text_fp_guide.render(surface)
