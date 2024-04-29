def print_pause(words):
    import time
    print(words)
    time.sleep(2)


def intro(villain_choice):
    print_pause("You wake up and you are on a"
                " FORKED PATH in a dark forest.")
    print_pause(f"You hear some sounds and find a"
                " frightened merchant hiding behind a tree")
    print_pause(f"He tells you a story about a {villain_choice} nearby"
                " and has been terrifying folks on the road.")
    print_pause("You look down the left path and see an old TOWER")
    print_pause("On the right path you see an old DWELLING")
    print_pause("In your hand you hold a STICK")


def forked_path(items, villain_choice):
    print_pause("Enter 1 to open the door of the TOWER")
    print_pause("Enter 2 to peer into the DWELLING")
    print_pause("What would you like to do?")
    choice1 = input("(Please enter 1 or 2).\n").lower()
    if (
        "1" in choice1 or
        "door" in choice1 or
        "tower" in choice1 or
        "left" in choice1
    ):
        tower(items, villain_choice)
    elif "2" in choice1 or "dwelling" in choice1 or "right" in choice1:
        dwelling(items, villain_choice)
    else:
        print_pause("I'm sorry I don't understand.")
        forked_path(items, villain_choice)


def tower(items, villain_choice):
    print_pause("You open the door of the TOWER")
    print_pause("You are about to enter the dark tower when"
                f" you see the eyes of the {villain_choice}")
    print_pause(f"Yikes! The {villain_choice} is hiding here!")
    print_pause(f"The {villain_choice} attacks you!")
    if "enchanted blade" not in items:
        if len(items) == 1:
            print_pause("You only have a stick to fight!")
        elif len(items) == 2:
            print_pause(f"You may be able to fight the {villain_choice}"
                        " with the " + items[1].upper() + " in your hand!")
        while True:
            choice2 = input("Would you like to"
                            " FIGHT(1) or ESCAPE(2)\n").lower()
            if "1" in choice2 or "fight" in choice2:
                lose(items, villain_choice)
                break
            elif (
                "2" in choice2 or
                "escape" in choice2 or
                "run away" in choice2
            ):
                print_pause("You ESCAPE to the FORKED PATH")
                forked_path(items, villain_choice)
                break
            else:
                print_pause("I'm sorry, I don't understand")
    elif "enchanted blade" in items:
        print_pause("The ENCHANTED BLADE glows bright blue")
        while True:
            choice3 = input("Would you like to"
                            " FIGHT(1) or ESCAPE(2)\n").lower()
            if "1" in choice3 or "fight" in choice3:
                win(items, villain_choice)
                break
            elif (
                "2" in choice3 or
                "escape" in choice3 or
                "run away" in choice3
            ):
                print_pause("You ESCAPE back to the FORKED PATH")
                forked_path(items, villain_choice)
                break
            else:
                print_pause("I'm sorry, I don't understand")


def dwelling(items, villain_choice):
    print_pause("You look into the DWELLING")
    print_pause("It is dark and there are tools hanging on the wall")
    print_pause("There is an AXE, a RAKE, and an ENCHANTED BLADE")
    print_pause("You only have the space to carry one of them")
    item_choices(items, villain_choice)


def item_swap(items, villain_choice, name):
    if name in items:
        print_pause("You already have that item")
        item_choices(items, villain_choice)
    elif name not in items and len(items) == 1:
        items.append(name)
        print_pause("You pick up the " + items[1].upper() + "")
        item_choices(items, villain_choice)
    else:
        print_pause("You drop the " + items[1].upper() + "")
        items.remove(items[1])
        items.append(name)
        print_pause("You pick up the " + items[1].upper() + "")
        item_choices(items, villain_choice)


def item_choices(items, villain_choice):
    choice5 = input("What would you like to do?\n"
                    "1. Take the AXE\n"
                    "2. Take the RAKE\n"
                    "3. Take the ENCHANTED BLADE\n"
                    "4. Go back to the FORKED PATH\n"
                    "Enter option (1-4)").lower()
    if "1" in choice5 or "axe" in choice5:
        item_swap(items, villain_choice, "axe")
    elif "2" in choice5 or "rake" in choice5:
        item_swap(items, villain_choice, "rake")
    elif "3" in choice5 or "enchanted blade" in choice5:
        item_swap(items, villain_choice, "enchanted blade")
    elif "4" in choice5 or "forked path" in choice5 or "leave" in choice5:
        print_pause("You leave the DWELLING for the PATH")
        forked_path(items, villain_choice)
    else:
        print_pause("I'm sorry I don't understand")
        item_choices(items, villain_choice)


def win(items, villain_choice):
    print_pause(f"You repel the {villain_choice}'s attack and"
                " you unsheath the " + items[1].upper() + "")
    print_pause("The glimmering blue BLADE emits"
                " a bolt of lightning and stuns the"
                f" {villain_choice}")
    print_pause(f"As the {villain_choice} is stunned"
                " you smite it with the ENCHANTED BLADE!")
    print_pause(f"You have made safe the forest from the"
                f" {villain_choice}, you are a mighty hero!")
    play_again()


def lose(items, villain_choice):
    if len(items) == 1:
        print_pause(f"You unsheath your mighty... " + items[0].upper())
        print_pause(f"The {villain_choice} laughs hysterically")
        print_pause(f"The {villain_choice} kills you - Whomp whomp")
        print_pause("GAME OVER")
        play_again()
    if len(items) == 2:
        print_pause(f"You unsheath your mighty... " + items[1].upper())
        print_pause(f"You attack with the weapon you"
                    " have (better than a stick)")
        print_pause(f"The {villain_choice} is extremely fast!")
        print_pause(f"You swing the " + items[1].upper() + " but you miss")
        print_pause(f"The {villain_choice} kills you - Whomp whomp")
        print_pause("GAME OVER")
        play_again()


def play_again():
    choice_again = input("Would you like to play again? (y/n)").lower()
    if "y" in choice_again or "yes" in choice_again:
        print_pause("Great, let's adventure again!")
        play_game()
    elif "n" in choice_again or "no" in choice_again:
        print_pause("OK, let's play again sometime")
    else:
        print_pause("Sorry, I don't understand, please respond y/n")
        play_again()


def select_villain():
    import random
    villains = ["DRAGON", "WICKED FAERIE", "UGLY TROLL",
                "MINOTAUR", "CHUPACABRA", "VAMPIRE", "GOBLIN"]
    # global villain_choice
    villain_choice = random.choice(villains)
    return villain_choice


def play_game():
    villain_choice = select_villain()
    items = []
    items.append("stick")
    intro(villain_choice)
    forked_path(items, villain_choice)


play_game()
