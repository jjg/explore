#!/usr/bin/env python

from god import Universe

def render_map(universe, zoom=1):

    axis_min = int(universe.min/zoom)
    axis_max = int(universe.max/zoom)

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
            for star in universe.stars:
                # NOTE: This math appears to work for placing bodies on
                # the scaled map, but I'm not 100% sure it's right
                if int(star.x/zoom) == x and int(star.y/zoom) == y:
                    map_point = "*"
                else:
                    for planet in star.planets:
                        if int(planet.x/zoom) == x and int(planet.y/zoom) == y:
                            map_point = "o"

            # Add the ship
            #if int(ship.x/zoom) == x and int(ship.y/zoom) == y:
            #    map_point = ">"

            # Draw the body at the point
            print(map_point, end="")

        print("")

# Create the universe
universe = Universe(40)

# Show it
render_map(universe)
