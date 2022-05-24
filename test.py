import pygame
from helper import Vec, Coordinate
from random import randint, uniform


W, H = 800, 600


def rand_color():
	return randint(0, 255), randint(0, 255), randint(0, 255)


def generate_points(a1, b1, a2, b2, n):
	return [Vec(uniform(a1, a2), uniform(b1, b2)) for _ in range(n)]


def draw_circles(surf, cir_arr, r):
	for loc in cir_arr:
		pygame.draw.circle(surf, rand_color(), loc, r)


def main():
	screen = pygame.display.set_mode((W, H))
	clock = pygame.time.Clock()

	pt_sys = Coordinate(W, H)

	top_left = Vec(-1, 1)
	bottom_right = Vec(1, -1)

	w1, h1 = pt_sys.ns_to_ss(top_left)
	w2, h2 = pt_sys.ns_to_ss(bottom_right)

	points = generate_points(w1, h1, w2, h2, 50)

	run = True
	while run:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		screen.fill("black")
		draw_circles(screen, points, 5)
		pygame.display.update()

	pygame.quit()
	exit()


if __name__ == "__main__":
	main()
