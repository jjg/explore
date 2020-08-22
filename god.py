import time
from random import randrange

from bodies import Star, Planet, Ship


class Universe:
    def __init__(self, size):

        # Create a number of stars in random locations
        # within the bounds of the universe

        # TODO Stuff breaks if bounds doesn't divide evenly, fix that 
        self.bounds = size 
        self.max = self.bounds / 2
        self.min = 0 - self.max 
        
        # DEBUG
        print(f"Universe min: {self.min}, max: {self.max}")

        # Generate stars of random sizes until the universe is full
        self.stars = []
        
        # TODO: Experiment to find the best way to derive this
        max_star_size = int(self.bounds/10)
        
        # TODO: Find a better way to decide the universe is full
        while len(self.stars) < self.bounds/10:
            x = randrange(self.min, self.max)
            y = randrange(self.min, self.max)
            z = randrange(self.min, self.max)
            star_size = randrange(1, max_star_size)
            name = str(time.time())
            self.stars.append(Star(x,y,z, star_size, name))

        # Next, add planets stars to create systems
        for star in self.stars:
            star.planets = []

            # TODO: Experiment to find the best way to derive this
            max_planets = int(star.radius)

            # Randomly pick a number of planets to create
            planet_count = randrange(0,max_planets)
            
            # DEBUG
            print(f"Adding {planet_count} planets to {star.name} system")

            for _ in range(planet_count):
                # Generate planets in random positions within the heliosphere
                # The only way I know how to do this is to generate random locations
                # and test to see if they are close enough
                planet = Planet(0,0,0,0)
                # TODO: Don't create planets that overlap
                while planet.get_distance(star) > star.heliosphere:
                    planet.x = randrange(self.min, self.max)
                    planet.y = randrange(self.min, self.max)
                    planet.z = randrange(self.min, self.max)
                    planet.name = str(time.time())
                # Add the generated planets to the star to create a system
                star.planets.append(planet)

                # DEBUG
                print(f"Planet {planet.name} added to system {star.name}")
