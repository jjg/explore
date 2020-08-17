#!/usr/env/python
import time
from random import randrange

from bodies import Star, Planet

# Create a fixed number of stars in random locations
# within the bounds of the universe

max_stars = 10
star_size = 10
max_planets_per_system = 9
universe_bounds = 1000
universe_max = universe_bounds / 2
universe_min = 0 - universe_max 

print(f"Universe min: {universe_min}, max: {universe_max}")

# First, create the stars
stars = []
for _ in range(max_stars):
    x = randrange(universe_min, universe_max)
    y = randrange(universe_min, universe_max)
    z = randrange(universe_min, universe_max)
    name = str(time.time())
    stars.append(Star(x,y,z, star_size, name))

# Next, add planets to create systems
for star in stars:
    star.planets = []
    # Randomly pick a number of planets to create
    planet_count = randrange(0,max_planets_per_system)
    print(f"Adding {planet_count} planets to {star.name} system")
    for _ in range(planet_count):
        # Generate planets in random positions within the heliosphere
        # The only way I know how to do this is to generate random locations
        # and test to see if they are close enough
        planet = Planet(0,0,0,0)
        while planet.get_distance(star) > star.heliosphere:
            print(".", end="")
            planet.x = randrange(universe_min, universe_max)
            planet.y = randrange(universe_min, universe_max)
            planet.z = randrange(universe_min, universe_max)
            planet.name = str(time.time())
        # Add the generated planets to the star to create a system
        star.planets.append(planet)
        print(f"Planet {planet.name} added to system {star.name}")


def render_list():
    print("--- List -------------------------------------------")
    for star in stars:
        print(f"{star.name}\tX:{star.x}\tY:{star.y}\tZ:{star.z}")
        for planet in star.planets:
            print(f"\t{planet.name}\tX:{planet.x}\tY:{planet.y}\tZ:{planet.z}")
def render_map():
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

print(f"Behold, the known universe!")
#render_map()
render_list()



