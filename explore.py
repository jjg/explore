class Player:
    def __init__(self):
        self.life = 100

class Ship:
    def __init__(self):
        self.fuel = 100
        self.x = 0
        self.y = 0
        self.z = 0

def render_scene():
    print("Stars as far as the eyes can see...")

def render_stats():
    print(f"LIFE: {player.life} FUEL: {ship.fuel} X: {ship.x} Y: {ship.y} Z: {ship.z}")

def render_actions():
    print(f"(m)ove, (q)uit")

# Init
player = Player()
ship = Ship()
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
    action = input(">")

    # Evaluate the action
    if action == "m":
        direction = input("Direction (x,y,z)? ")
        distance = int(input("Distance? "))
        if distance < ship.fuel:
            # Update position
            if direction == "x":
                ship.x += distance
            if direction == "y":
                ship.y += distance
            if direction == "z":
                ship.z += distance
            ship.fuel += -distance
        else:
            print("Not enough fuel!")

    # Update the stats
    player.life += -1

print("Goodbye")
