import time

def game_intro():
    print("Welcome to the text-based game!")
    time.sleep(1)
    print("In this game, you will navigate through a series of challenges.")
    time.sleep(1)
    print("Your choices will determine the outcome of the game.")
    time.sleep(1)

def challenge_one():
    print("You come across a fork in the road. Which way do you go?")
    time.sleep(1)
    print("1. Left")
    time.sleep(1)
    print("2. Right")
    time.sleep(1)

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        print("You chose the left path. You encounter a pack of wolves.")
        time.sleep(1)
        print("What do you do?")
        time.sleep(1)
        print("1. Run")
        time.sleep(1)
        print("2. Fight")
        time.sleep(1)

        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            print("You try to run, but the wolves catch up to you and you are killed.")
        elif choice == 2:
            print("You fight off the wolves and continue on your journey.")

    elif choice == 2:
        print("You chose the right path. You come across a river.")
        time.sleep(1)
        print("What do you do?")
        time.sleep(1)
        print("1. Swim across")
        time.sleep(1)
        print("2. Build a raft")
        time.sleep(1)

        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            print("You try to swim across, but the current is too strong and you drown.")
        elif choice == 2:
            print("You build a raft and successfully cross the river.")

    else:
        print("Invalid choice. Please try again.")
        challenge_one()

def challenge_two():
    print("You have reached the second challenge. What do you do?")
    time.sleep(1)
    print("1. Climb a mountain")
    time.sleep(1)
    print("2. Explore a cave")
    time.sleep(1)

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        print("You climb the mountain and reach the summit.")
        time.sleep(1)
        print("Congratulations, you have completed the game!")
    elif choice == 2:
        print("You explore the cave, but get lost and never make it out.")
    else:
        print("Invalid choice. Please try again.")
        challenge_two()

game_intro()
challenge_one()
challenge_two()