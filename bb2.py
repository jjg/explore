#!/usr/bin/env python

import time
from random import randrange

from bodies import Star, Planet, Ship

# Create a fixed number of stars in random locations
# within the bounds of the universe

max_stars = 5 
star_size = 1
max_planets_per_system = 9
# TODO Stuff breakd if bounds doesn't divide evenly, fix that 
universe_bounds = 40 
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
    #print(f"Adding {planet_count} planets to {star.name} system")
    for _ in range(planet_count):
        # Generate planets in random positions within the heliosphere
        # The only way I know how to do this is to generate random locations
        # and test to see if they are close enough
        planet = Planet(0,0,0,0)
        # TODO: Don't create planets that overlap
        while planet.get_distance(star) > star.heliosphere:
            planet.x = randrange(universe_min, universe_max)
            planet.y = randrange(universe_min, universe_max)
            planet.z = randrange(universe_min, universe_max)
            planet.name = str(time.time())
        # Add the generated planets to the star to create a system
        star.planets.append(planet)
        #print(f"Planet {planet.name} added to system {star.name}")

# Add a single ship for testing
ship = Ship()
ship.x = randrange(universe_min, universe_max)
ship.y = randrange(universe_min, universe_max)
ship.z = randrange(universe_min, universe_max)

def render_list():
    print("--- List -------------------------------------------")
    for star in stars:
        print(f"{star.name}\tX:{star.x}\tY:{star.y}\tZ:{star.z}")
        for planet in star.planets:
            print(f"\t{planet.name}\tX:{planet.x}\tY:{planet.y}\tZ:{planet.z}")

def render_map():
    # TODO: Can we merge the list and map to show side-by-side?
    zoom = 1 
    axis_min = int(universe_min/zoom)
    axis_max = int(universe_max/zoom)

    # Draw header
    for x in range(axis_min, axis_max):
        if x % 10 == 0:
            print("|", end="")
        else :
            print("-", end="")
    
    print("")

    for y in range(axis_min, axis_max):
        for x in range(axis_min, axis_max):
            map_point = "."

            # Add stars and planets
            for star in stars:
                # NOTE: This math appears to work for placing bodies on
                # the scaled map, but I'm not 100% sure it's right
                if int(star.x/zoom) == x and int(star.y/zoom) == y:
                    map_point = "*"
                else:
                    for planet in star.planets:
                        if int(planet.x/zoom) == x and int(planet.y/zoom) == y:
                            map_point = "o"

            # Add the ship
            if int(ship.x/zoom) == x and int(ship.y/zoom) == y:
                map_point = ">"

            # Draw the body at the point
            print(map_point, end="")

        print("")

print(f"Behold, the known universe!")
render_list()
render_map()
