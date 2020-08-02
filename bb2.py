#!/usr/env/python
from random import randrange

from god import Universe, Galaxy, System
from bodies import Star, Planet

known_universe = Universe()

# Create a fixed number of stars in random locations
# within the bounds of the universe

max_stars = 10
universe_bounds = 1000000

stars = []
for _ in range(max_stars):
    x = randrange(0, universe_bounds)
    y = randrange(0, universe_bounds)
    z = randrange(0, universe_bounds)
    stars.append(Star(x,y,z
