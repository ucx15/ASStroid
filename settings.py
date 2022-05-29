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

# Debug
DEBUG = False

# Coordinate Setup
SIZE = 1536, 864
SCR_WIDTH, SCR_HEIGHT = SIZE
CENTER = (SCR_WIDTH // 2, SCR_HEIGHT // 2)
OX, OY = CENTER
SHIFT_PADDING = 5  # in percent with window width

# Camera
FPS = 120
CAM_SPEED = 1
CAM_PADDING = 2  # in percent with window width

# Ship Default Settings
THRUST = 1_500
MASS = 10
ANGULAR_VEL = 180  # in degrees per second
BRAKES = .95  # reduction in velocity every frame to this amount

# Asteroid Default Settings
AS_SIZE = 20  # in percent with window width
AS_MASS = 50
AS_THRUST = 1000
