from bodies import Player, Ship, Planet

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
        scene += f"{planet.description} at {planet.x}:{planet.y}:{planet.z}\n"
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
  if player.get_distance(ship) == 0:
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
player = Player()
ship = Ship()
# TODO: Generate planets procedurally (except perhaps "home"?)
planets = [
  Planet("Petra", "Your home planet", 100, 0,0,0),
  Planet("Elno", "Petra's moon", 50, 200,0,0)
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
      if abs(distance) > ship.fuel:
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
        ship.fuel += -abs(distance)
    else:
      if abs(distance) > player.life:
        print("You'll die before you get there!")
      else:
        # Update player position
        if direction == "x":
          player.x += distance
        if direction == "y":
          player.y += distance
        if direction == "z":
          player.z += distance
        player.life += -abs(distance)
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
