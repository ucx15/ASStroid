from time import perf_counter as pfc
import sys

import pygame
from Player import PlayerObject
from UI import Text

pygame.init()
Vec = pygame.Vector2

# Some Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (20, 20, 20)
CYAN = (0, 150, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class GAME:
	def __init__(self):
		# Coordinate_System_setup
		self.SIZE = (1280, 720)
		self.FPS = 120
		self.W, self.H = self.SIZE
		self.OX, self.OY = self.W // 2, self.H // 2
		self.CENTER = (self.OX, self.OY)

		# Pygame_Variables_Setup
		self.display = pygame.display
		self.surface = pygame.display.set_mode(self.SIZE)
		self.display.set_caption("ASStroid")
		self.clock = pygame.time.Clock()

		# Fonts
		self.font_title = pygame.font.SysFont("Consolas", 100)
		self.font_plain = pygame.font.SysFont("consolas", 30)
		self.font_debug = pygame.font.SysFont("consolas", 15)

		# Images
		self.asteroid_img = pygame.transform.scale(pygame.image.load("Assets/asteroid_img.png"), (75, 75))
		self.bholu_img = pygame.image.load("Assets/bholuEng.png").convert_alpha()
		self.sship_img = pygame.transform.scale(pygame.image.load("Assets/SpaceShip.png").convert_alpha(), (60, 135))

		# Texts
		title_string = "ASStroid Miner"
		guide_string = "Press 'F' to play"
		self.text_fp_title = Text(title_string, WHITE, self.font_title, self.CENTER)
		self.text_fp_guide = Text(guide_string, CYAN, self.font_plain, (self.OX, self.OY + 100))

	def first_page(self):
		self.surface.blit(self.asteroid_img, (self.OX + 400, self.OY - 130))
		self.surface.blit(self.bholu_img, (10, self.H-177))
		self.text_fp_title.render(self.surface)
		self.text_fp_guide.render(self.surface)

	def mainloop(self):
		# Game_Setup

		runloop = 1
		run_fp = 1
		started = 0
		frame_time = 0

		spaceship = PlayerObject(Vec(self.OX, self.OY), self.sship_img)

		# Game_Loop
		while runloop:
			# Time_Management
			frame_time = pfc() - frame_time
			delta_time = frame_time
			frame_time = pfc()

			# Event_Loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					runloop = 0

			# Keyboard_Input_Handling
			keys = pygame.key.get_pressed()
			kf = keys[pygame.K_f]
			if keys[pygame.K_ESCAPE]:
				runloop = 0

			# Surface_Update
			self.surface.fill(BLACK)
			self.clock.tick(self.FPS)

			# Intro_Screen
			if run_fp:
				self.first_page()
				if kf:
					run_fp = 0
					started = 1

			# Main_Game
			if not run_fp and started:
				spaceship.update(self.W, self.H, keys, delta_time)
				spaceship.show(self.surface, debug=False)
			self.display.update()

		pygame.quit()
		sys.exit()


GameWin = GAME()
GameWin.mainloop()
