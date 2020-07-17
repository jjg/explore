class Universe:
  def __init__(self):
    self.galaxies = []

class Galaxy:
  def __init__(self, name, x, y, z):
    self.name = ""
    # TODO: Calculate radius based on systems
    self.radius = 0.0
    self.x = x
    self.y = y
    self.z = z
    self.systems = []

class System:
  def __init__(self, name, x, y, z):
    self.name = name
    self.x = x
    self.y = y
    self.z = z
    # TODO: Calculate radius based on planets
    self.radius = 0.0
    self.stars = []
    self.planets = []
    self.ships = []
