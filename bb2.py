#!/usr/env/python
from random import randrange

from god import Universe, Galaxy, System
from bodies import Star, Planet

known_universe = Universe()

# Create a fixed number of stars in random locations
# within the bounds of the universe

max_stars = 10
universe_bounds = 1000
universe_max = universe_bounds / 2
universe_min = universe_bounds - universe_max 

stars = []
for _ in range(max_stars):
    x = randrange(universe_min, universe_max)
    y = randrange(universe_min, universe_max)
    z = randrange(universe_min, universe_max)
    stars.append(Star(x,y,z))
