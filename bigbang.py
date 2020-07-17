from random import randrange

from faker import Faker

from god import Universe, Galaxy, System
from bodies import Planet

fake = Faker()

# Config
numerosity = 10 # the number of things to create (fixed for now)
coordinate_start = -10000
coordinate_end = 10000

# Create the universe 
# This part is easy, there's only one (that we know of)
known_universe = Universe()

# TODO: Generate some galaxies
# A galaxy has a name and coordinates that define its center.
# Its bounds are defined by the size and coordinates of the
# Systems it contains.
for _ in range(numerosity):
  x = randrange(coordinate_start, coordinate_end)
  y = randrange(coordinate_start, coordinate_end)
  z = randrange(coordinate_start, coordinate_end)
  known_universe.galaxies.append(Galaxy(fake.last_name(),x,y,z))


# TODO: Generate some systems
# A system has a name and coordinates that define its center.
# A system consists of a fixed-number of planets and a star
# located at its center. A system can also contain a dynamic
# number of ships (and potentially other dynamic objets.
# A systems bounds are defined by the orbit of the furthest
# planet from the system's star.

# TODO: Generate some planets
# A planet has a name and coordinates that define the location
# of its center.  A planets bounds are defined by its radius,
# as well as the radius of its atmosphere.  There is a need to
# make planets more interesting so let's explore that here.

# Display the results
for g in known_universe.galaxies:
  print(f"{g.name}")
  for s in g.systems:
    print(f"\t{s.name}")
      for p in s.planets:
        print(f"\t{p.name}")
