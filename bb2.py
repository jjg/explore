#!/usr/env/python
import time
from random import randrange

from god import Universe, Galaxy, System
from bodies import Star, Planet

known_universe = Universe()

# Create a fixed number of stars in random locations
# within the bounds of the universe

max_stars = 10
star_size = 10
universe_bounds = 1000
universe_max = universe_bounds / 2
universe_min = 0 - universe_max 

print(f"Universe min: {universe_min}, max: {universe_max}")

stars = []
for _ in range(max_stars):
    x = randrange(universe_min, universe_max)
    y = randrange(universe_min, universe_max)
    z = randrange(universe_min, universe_max)
    name = str(time.time())
    stars.append(Star(x,y,z, star_size, name))


print(f"Behold, the known universe!")
print("--- List -------------------------------------------")
for star in stars:
    print(f"{star.name}\tX:{star.x}\tY:{star.y}\tZ:{star.z}")

print("--- Map --------------------------------------------")
zoom = 100 
for y in range(int(universe_min/zoom), int(universe_max/zoom)):
    for x in range(int(universe_min/zoom), int(universe_max/zoom)):
        for star in stars:
            if int(star.x/zoom) == x and int(star.y/zoom) == y:
                print("*", end="")
            else:
                print(" ", end="")
    print("\n")
print("----------------------------------------------------")


