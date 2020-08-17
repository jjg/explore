import math

# TODO: This constant probably belongs elsewhere
v_range = 100

class Body:
  def __init__(self):
    self.x = 0.0
    self.y = 0.0
    self.z = 0.0
    self.radius = 1.0

  def get_distance(self, other_body):
    d = math.sqrt(math.pow(other_body.x - self.x, 2) +
      math.pow(other_body.y - self.y, 2) +
      math.pow(other_body.z - self.z, 2) * 1.0)

    return d


class Star(Body):
  def __init__(self, x, y, z, radius, name=""):
    super().__init__()
    self.radius = radius
    # TODO: Calculate the heliosphere based on mass, etc.
    self.heliosphere = self.radius * 5
    self.name = name
    self.x = x
    self.y = y
    self.z = z

  def in_range(self, other_body):
    if self.get_distance(other_body) < v_range:
      return True
    else:
      return False

class Planet(Body):
  def __init__(self, x, y, z, radius, name="", description=""):
    super().__init__()
    self.radius = radius
    self.atmosphere_radius = self.radius + 5
    self.name = name
    self.description = description
    self.x = x
    self.y = y
    self.z = z

  def in_range(self, other_body):
    if self.get_distance(other_body) < v_range:
      return True
    else:
      return False

  def in_atmosphere(self, other_body):
    if self.get_distance(other_body) < self.atmosphere_radius:
      return True
    else:
      return False

  def on_surface(self, other_body):
    if self.get_distance(other_body) == self.radius:
      return True
    else:
      return False

class Player(Body):
  def __init__(self):
    super().__init__()
    self.life = 100

class Ship(Body):
  def __init__(self):
    super().__init__()
    self.fuel = 1000
    self.boarded = False
    self.landed = True
