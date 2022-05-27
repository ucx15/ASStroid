from pygame import Vector2

Vec = Vector2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (20, 20, 20)
CYAN = (0, 150, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Coordinate Setup
SIZE = 1536, 864
SCR_WIDTH, SCR_HEIGHT = SIZE
CENTER = (SCR_WIDTH // 2, SCR_HEIGHT // 2)
OX, OY = CENTER

# FrameRate
FPS = 120

# Ship Default Settings
THRUST = 1_500
MASS = 2
ANGULAR_VEL = 360  # in degrees per second
BRAKES = .98  # reduction in velocity every frame to this amount
