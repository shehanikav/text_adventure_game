import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = "Level 1: Forest Entrance"
        self.bag = []

    def add_to_bag(self, item):
        if len(self.bag) < 10:
            self.bag.append(item)
            print(f"You obtained {item}.")
        else:
            print("Your bag is full!")

    def check_bag(self):
        if self.bag:
            print("Your bag contains:", ", ".join(self.bag))
        else:
            print("Your bag is empty.")

def get_level_number(position):
    """Extract and return the level number from the position string."""
    return position.split(":")[0]

def display_world(world, player):
    location = world[player.position]
    level_number = get_level_number(player.position)
    print(f"\n This is {level_number}")
    print(location['description'])

    if "item" in location:
        print(f"You see an item here: {location['item']} (Complete the task to get it!)")

    print("Options:")
    for option in location["options"]:
        print(f"- {option}")

def move(world, player, direction):
    if direction in world[player.position]["options"]:
        next_room = world[player.position]["options"][direction]
        if "locked" in world[next_room] and world[next_room]["locked"]:
            if "Key" in player.bag:
                print("You used the Key to unlock the door.")
                world[next_room]["locked"] = False
                player.bag.remove("Key")
            else:
                print("The door is locked. You need a Key.")
                return
        player.position = next_room
        print(f"You moved to {player.position}.")
    else:
        print("You can't go that way!")

def interact(world, player):
    location = world[player.position]

    if "item" in location and "task" in location:
        print(location["task"])
        answer = input("Your answer: ").lower()

        if answer == location["answer"].lower():
            player.add_to_bag(location["item"])
            del location["item"]
            del location["task"]
            del location["answer"]
        else:
            print("That’s not correct. Try again later.")
    else:
        print("Nothing to interact with here.")

# Define the game world
world = {
    "Level 1: Forest Entrance": {
        "description": "You are at the entrance of a dark forest.",
        "options": {"forward": "Level 2: Clearing"},
        "task": "Task: Solve this riddle - What has roots but never grows?",
        "answer": "Mountain",
        "item": "Map"
    },
    "Level 2: Clearing": {
        "description": "A bright clearing with wildflowers.",
        "options": {"forward": "Level 3: Riverbank", "back": "Level 1: Forest Entrance"},
        "task": "Task: What shines at night but disappears by dawn?",
        "answer": "Star",
        "item": "Lantern"
    },
    "Level 3: Riverbank": {
        "description": "A fast-flowing river blocks your path.",
        "options": {"forward": "Level 4: Bridge", "back": "Level 2: Clearing"},
        "task": "Task: How many legs does a spider have?",
        "answer": "8",
        "item": "Rope"
    },
    "Level 4: Bridge": {
        "description": "The bridge creaks under your weight.",
        "options": {"forward": "Level 5: Village Entrance", "back": "Level 3: Riverbank"},
        "task": "Task: What can run but never walks?",
        "answer": "Water",
        "item": "Potion"
    },
    "Level 5: Village Entrance": {
        "description": "The village gate stands tall.",
        "options": {"forward": "Level 6: Village Market", "back": "Level 4: Bridge"},
        "task": "Task: Unscramble this word: 'drows'",
        "answer": "sword",
        "item": "Sword"
    },
    "Level 6: Village Market": {
        "description": "Traders and shoppers bustle around.",
        "options": {"forward": "Level 7: Village Inn", "back": "Level 5: Village Entrance"},
        "task": "Task: What has hands but can’t clap?",
        "answer": "Clock",
        "item": "Shield"
    },
    "Level 7: Village Inn": {
        "description": "A warm place with crackling fireplaces.",
        "options": {"forward": "Level 8: Castle Gate", "back": "Level 6: Village Market"},
        "task": "Task: Guess the number I'm thinking of (1-5):",
        "answer": str(random.randint(1, 5)),
        "item": "Key"
    },
    "Level 8: Castle Gate": {
        "description": "The grand castle gate is locked.",
        "options": {"forward": "Level 9: Castle Hallway", "back": "Level 7: Village Inn"},
        "locked": True
    },
    "Level 9: Castle Hallway": {
        "description": "Echoes fill the hallway. One last task remains.",
        "options": {"forward": "Level 10: Treasure Room", "back": "Level 8: Castle Gate"},
        "task": "Task: What has a neck but no head?",
        "answer": "Bottle",
        "item": "Crown"
    },
    "Level 10: Treasure Room": {
        "description": "Congratulations! You've found the treasure!",
        "options": {}
    }
}

def main():
    name = input("Enter your character's name: ")
    player = Player(name)
    print(f"Welcome, {player.name}! Your 10-level adventure begins now.")

    while player.position != "Level 10: Treasure Room":
        display_world(world, player)
        action = input("What do you want to do? (move/interact/check bag): ").lower()

        if action == "move":
            direction = input("Which direction? (forward/back): ").lower()
            move(world, player, direction)
        elif action == "interact":
            interact(world, player)
        elif action == "check bag":
            player.check_bag()
        else:
            print("Invalid action. Try again.")

    print("You win! The treasure is yours. Glory and riches await!")
    print("Thanks for playing Treasure Quest!")

if __name__ == "__main__":
    main()
