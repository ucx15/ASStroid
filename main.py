from time import perf_counter as pfc
import sys
import pygame
from settings import *
from level import Level
from pages import FirstPage

pygame.init()


class GAME:
	def __init__(self):
		# Pygame_Variables_Setup
		self.display = pygame.display
		self.surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT), pygame.NOFRAME, vsync=1)
		self.display.set_caption("ASStroid")
		self.clock = pygame.time.Clock()

		# Fonts
		self.font_title = pygame.font.SysFont("Consolas", 100)
		self.font_plain = pygame.font.SysFont("consolas", 30)
		self.font_debug = pygame.font.SysFont("consolas", 15)

		self.first_page = FirstPage(self.font_title, self.font_plain)

	def mainloop(self):
		# Game_Setup

		runloop = 1
		run_fp = 1
		started = 0
		frame_time = 0

		world = Level()

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
			self.clock.tick(FPS)

			# Intro_Screen
			if run_fp:
				self.first_page.show(self.surface)
				if kf:
					run_fp = 0
					started = 1

			# Main_Game
			if not run_fp and started:
				world.update(delta_time, keys)
				world.show(self.surface, debug=False)
			self.display.update()

		pygame.quit()
		sys.exit()


def main():
	game_win = GAME()
	game_win.mainloop()


if __name__ == "__main__":
	main()
