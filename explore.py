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

class Planet:
  def _get_location(self):
    return f"{self.x}:{self.y}:{self.z}"

  def __init__(self):
    self.x = 0
    self.y = 0
    self.z = 0
    self.get_location = self._get_location
    self.atmosphere_diameter = 20
    self.surface_diameter = 15

def render_scene():
  print("Stars as far as the eyes can see...")

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
    else:
      actions += " (b)oard"
  print(f"{actions} ")

# Init
player = Player()
ship = Ship()
planets = []
action = ""

# Begin the main loop
while action != "q":

  # Display the scene
  render_scene()

  # Display the current stats
  render_stats()

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

  # Update the stats
  player.life += -1

print("Goodbye")
