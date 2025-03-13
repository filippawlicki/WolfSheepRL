GRID_SIZE = 10
PYGAME_SCALE = 80
NUM_WOLVES = 3
NUM_SHEEP = 5
TARGET_RADIUS = 2
MIN_DISTANCE_SHEEP = 2
SHEEP_VISION_RANGE = GRID_SIZE*4/5 # New setting for sheep's vision range

# Reward settings
SHEEP_NEAR_TARGET_REWARD = 5
SHEEP_CAPTURED_PENALTY = -3
SHEEP_MOVEMENT_PENALTY = -1
DOG_MOVEMENT_REWARD = 1

# Miscellaneous settings
RANDOM_SEED = None

# Path to images
DOG_IMAGE = "images/dog.png"
SHEEP_IMAGE = "images/sheep.png"
TARGET_IMAGE = "images/fence.png"
