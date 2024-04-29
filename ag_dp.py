
def print_pause(words):
    import time
    print(words)
    time.sleep(0)

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a DRAGON is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a HOUSE")
    print_pause("To the right of you is a dark CAVE")
    print_pause("In your hand you hold your trusty (but not very effective) DAGGER")
 
def first_choice():
    print("first choice")

def open_field():
    print_pause("Enter 1 to knock on the door of the HOUSE")
    print_pause("Enter 2 to peer into the CAVE")
    print_pause("What would you like to do?")

def house():
    print_pause("You approach the door of the HOUSE")
    print_pause("You are about to knock when the door opens and out steps a DRAGON")
    print_pause("Eeep! This is the DRAGON's house")
    print_pause("The DRAGON attacks you!")
    if "sword of ogoroth" not in items and "dagger" in items:
        print_pause("You feel a little under-prepared with just your tiny DAGGER")
        choice2 = input("Would you like to FIGHT(1) or RUN AWAY(2)\n").lower()
        if "1" in choice2 or "fight" in choice2:
            print_pause("The dragon kills you Whomp whomp")
            break
        elif "2" in choice2 or "run" in choice2 or "away" in choice2:
            print_pause("You run back out to the field")
    elif "sword of ogoroth" in items:
        print_pause("You feel very confident with your new SWORD")
        choice3 = input("Would you like to FIGHT(1) or RUN AWAY(2)\n").lower()
        if "1" in choice3 or "fight" in choice3:
            win()
            break
        elif "2" in choice3 or "run" in choice3 or "away" in choice3:
            print_pause("You run back out to the field")

def win():
    print_pause("As the DRAGON moves to attack you, you unsheath the SWORD OF OGOROTH")
    print_pause("The sword shimmers brightly in your hand as you brace for the attack")
    print_pause("But the DRAGON sees the SWORD OF OGOROTH and flees!")
    print_pause("You have rid the village of the evil DRAGON, you are victorious!")

def play_again():
    choice_again = input("Would you like to play again? (y/n)").lower()
    if "y" in choice_again or "yes" in choice_again:
        print_pause("Great, let's adventure again!")
        #break
    elif "n" in choice_again or "no" in choice_again:
        print_pause("OK, let's play again sometime")
        #break
    else:
        print_pause("Sorry, I don't understand, please respond y/n")
    if "n" in choice_again or "no" in choice_again:
        return True #might need to delete this
        #break

def play_game():
    return True

while True:
    items = []
    items.append("dagger")
    intro()
    while True:
        open_field()
        choice1 = input("(Please enter 1 or 2).\n").lower()
        if "1" in choice1 or "door" in choice1 or "house" in choice1:
            print_pause("You approach the door of the HOUSE")
            print_pause("You are about to knock when the door opens and out steps a DRAGON")
            print_pause("Eeep! This is the DRAGON's house")
            print_pause("The DRAGON attacks you!")
            if "sword of ogoroth" not in items and "dagger" in items:
                print_pause("You feel a little under-prepared with just your tiny DAGGER")
                choice2 = input("Would you like to FIGHT(1) or RUN AWAY(2)\n").lower()
                if "1" in choice2 or "fight" in choice2:
                    print_pause("The dragon kills you Whomp whomp")
                    break
                elif "2" in choice2 or "run" in choice2 or "away" in choice2:
                    print_pause("You run back out to the field")
            elif "sword of ogoroth" in items:
                print_pause("You feel very confident with your new SWORD")
                choice3 = input("Would you like to FIGHT(1) or RUN AWAY(2)\n").lower()
                if "1" in choice3 or "fight" in choice3:
                    win()
                    break
                elif "2" in choice3 or "run" in choice3 or "away" in choice3:
                    print_pause("You run back out to the field")
        elif "2" in choice1 or "peer" in choice1 or "cave" in choice1:
            if "sword of ogoroth" not in items:
                print_pause("You peer cautiously into the CAVE")
                print_pause("It turns out to only be a very small CAVE")
                print_pause("Your eye catches a glint of metal behind a rock")
                print_pause("You have found the magical SWORD of OGOROTH")
                print_pause("You discard your silly old DAGGER and take the SWORD with you")
                items.append("sword of ogoroth")
                items.remove("dagger")
                print_pause("You walk back out to the open field")
            elif "sword of ogoroth" in items:
                print_pause("You peer into the cave again, seeing only your old dagger on the ground")
                print_pause("You walk back out to the open field")
    while True:
        choice_again = input("Would you like to play again? (y/n)").lower()
        if "y" in choice_again or "yes" in choice_again:
            print_pause("Great, let's adventure again!")
            break
        elif "n" in choice_again or "no" in choice_again:
            print_pause("OK, let's play again sometime")
            break
        else:
            print_pause("Sorry, I don't understand, please respond y/n")
    if "n" in choice_again or "no" in choice_again:
        break
