import math

def get_distance(a, b):

  d = math.sqrt(math.pow(b.x - a.x, 2) +
    math.pow(b.y - a.y, 2) +
    math.pow(b.z - a.z, 2) * 1.0)

  return d

class Player:
  def _get_location(self):
    return f"{self.x}:{self.y}:{self.z}"

  def __init__(self):
    self.life = 100.0
    self.x = 0.0
    self.y = 0.0
    self.z = 0.0
    self.get_location = self._get_location 

class Ship:
  def _get_location(self):
    return f"{self.x}:{self.y}:{self.z}"

  def __init__(self):
    self.fuel = 1000.0
    self.x = 0.0
    self.y = 0.0
    self.z = 0.0
    self.get_location = self._get_location 
    self.boarded = False
    self.landed = True

class Planet:
  def _get_location(self):
    return f"{self.x}:{self.y}:{self.z}"

  def _in_range(self, other):
    if get_distance(self, other) < v_range:
      return True
    else:
      return False
    
  def _in_atmosphere(self, other):
    # Calculate to see if the other is within the atmosphere of the planet
    if get_distance(self, other) < (self.atmosphere_diameter/2):
      return True
    else:
      return False

  def _on_surface(self, other):
    # Calculate to see if the other is within the surface of the planet 
    if get_distance(self, other) < (self.diameter/2):
      return True
    else:
      return False

  def __init__(self, description, diameter, x, y, z):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.get_location = self._get_location
    self.diameter = diameter 
    self.atmosphere_diameter = diameter + 5
    self.description = description
    self.in_range = self._in_range
    self.in_atmosphere = self._in_atmosphere
    self.on_surface = self._on_surface

def render_scene():
  # TODO: If you are on a planet, say so and don't enumerate others
  scene = "You see...\n"
  for planet in planets:

    # DEBUG
    #print(f"{planet.description}, distance: {get_distance(planet, ship)}")

    if planet.on_surface(ship):
      scene = f"You have landed on {planet.description}\n"
    else:
      if planet.in_range(ship):
        scene += f"{planet.description} at {planet.get_location()}\n"
  scene += "...and stars as far as the eyes can see..."
  print(scene)

def render_stats():
  stats = f"LIFE: {player.life} FUEL: {ship.fuel} "
  if ship.boarded:
    stats += f"X: {ship.x} Y: {ship.y} Z: {ship.z}"
  else:
    stats += f"X: {player.x} Y: {player.y} Z: {player.z}"
  print(f"{stats} ")

def render_actions():
  actions = f"(m)ove, (q)uit "
  if player.get_location() == ship.get_location():
    if ship.boarded:
      actions += "(u)nboard "
      if ship.landed:
        actions += "(l)aunch "
      else:
        for planet in planets:
          if planet.in_atmosphere(ship):
            actions += "lan(d) "
    else:
      actions += "(b)oard "
  print(f"{actions} ")

# Init
# TODO: We're using "globals" that should probably be scoped better
v_range = 100
player = Player()
ship = Ship()
# TODO: Generate planets procedurally (except perhaps "home"?)
# TODO: These planets are too small
planets = [
  Planet("Your home planet",15,0,0,0),
  Planet("Your home planet's moon",5,150,150,150)
]
action = ""

# Begin the main loop
while action != "q":

  # Display the current stats
  render_stats()

  # Display the scene
  render_scene()

  # Display the avaliable actions
  render_actions()

  # Accept action input from the player
  action = input("> ")

  # Evaluate the action
  if action == "m":
    direction = input("Direction (x,y,z)? ")
    distance = float(input("Distance? "))
    if ship.boarded:
      if distance > ship.fuel:
        print("Not enough fuel to go that far!")
      else:
        # Update ship and player position
        if direction == "x":
            ship.x += distance
            player.x += distance
        if direction == "y":
            ship.y += distance
            player.y += distance
        if direction == "z":
            ship.z += distance
            player.z += distance
        ship.fuel += -distance
    else:
      if distance > player.life:
        print("You'll die before you get there!")
      else:
        # Update player position
        if direction == "x":
          player.x += distance
        if direction == "y":
          player.y += distance
        if direction == "z":
          player.z += distance
        player.life += - distance
  if action == "b":
    if ship.boarded:
      print("You're already onboard!")
    else:
      ship.boarded = True
  if action == "u":
    if ship.boarded:
      ship.boarded = False
    else:
      print("You're not onboard!")
  if action == "d":
    if ship.landed:
      print("The ship is on the ground already!")
    else:
      # TODO: Move ship to planet's surface
      ship.landed = True
  if action == "l":
    if ship.landed:
      # TODO: Move ship to planet's atmosphere
      ship.landed = False
    else:
      print("The ship is already launched!")

  # Update the stats
  player.life += -1

print("Goodbye")
