class Player:
  def _get_location(self):
    return f"{self.x}:{self.y}:{self.z}"

  def __init__(self):
    self.life = 100
    self.x = 0
    self.y = 0
    self.z = 0
    self.get_location = self._get_location 

class Ship:
  def _get_location(self):
    return f"{self.x}:{self.y}:{self.z}"

  def __init__(self):
    self.fuel = 100
    self.x = 0
    self.y = 0
    self.z = 0
    self.get_location = self._get_location 
    self.boarded = False
    self.landed = True

class Planet:
  def _get_location(self):
    return f"{self.x}:{self.y}:{self.z}"

  def _in_range(self, other):
    # Calculate to see if the planet is within visual range
    if ((abs(self.x) + (self.atmosphere_diameter/2) + v_range) - abs(other.x) > 0 
      and (abs(self.y) + (self.atmosphere_diameter/2) + v_range) - abs(other.y) > 0 
      and (abs(self.z) + (self.atmosphere_diameter/2) + v_range) - abs(other.z) > 0):  
      return True
    else:
      return False

  def __init__(self, description, diameter, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.get_location = self._get_location
    self.surface_diameter = diameter 
    self.atmosphere_diameter = diameter + 5
    self.description = description
    self.in_range = self._in_range

def render_scene():
  # TODO: If you are on a planet, say so and don't enumerate others
  scene = "You see...\n"
  for planet in planets:
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
  actions = f"(m)ove, (q)uit"
  if player.get_location() == ship.get_location():
    if ship.boarded:
      actions += " (u)nboard"
      if ship.landed:
        actions += " (l)aunch"
    else:
      actions += " (b)oard"
  # TODO: If the ship is within the atmosphere of a planet,
  # display the "lan(d)" option
  print(f"{actions} ")

# Init
# TODO: We're using "globals" that should probably be scoped better
v_range = 10
player = Player()
ship = Ship()
planets = [
  Planet("Your home planet",15,0,0,0),
  Planet("Your home planet's moon",5,15,15,0)
]
#planets.append(
#  Planet("Your home planet",15,0,0,0)
#)


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
    distance = int(input("Distance? "))
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
      ship.landed = True
  if action == "l":
    if ship.landed:
      ship.landed = False
    else:
      print("The ship is already launched!")

  # Update the stats
  player.life += -1

print("Goodbye")
