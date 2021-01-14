import random
import math

def random_coordinates():
    while True:
        latitude = (random.random() * 180.0) - 90.0
        radius_factor = math.cos(latitude * (math.pi/180.0))
        if random.random() <= radius_factor:
            longitude = (random.random() * 360) - 180.0
            return (latitude,longitude)