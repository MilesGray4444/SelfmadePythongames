from sys import exit


def Pokemonroom():
    print("This room is full Pokemons. How many Pokemons do you take?")

# try and except to see if the input is an integer
    try:
        how_many = int(input("> "))
    except:
        dead("Sorry, type a number next time please.")

    if how_many < 20:
        print("Nice, you have enough pokeballs, you WIN!")
        exit(0)
    else:
        dead("You don't have enough pokeballs. Greed is bad!")


def Pikachu_room():
    print("There is a Pikachu here.")
    print("Pikachu is not in a good state today.")
    print("How are you going to make Pikachu happy?")
    Pikachu_moved = False

    while True:
        choice = input("> ")

        if choice == "ignore Pikachu":
            dead("Pikachu electrifies you and you faint.")
        elif choice == "play with Pikachu" and not Pikachu_moved:
            print("pikachu is in a good state now, showing you another door")
            print("You can go through it now")
            Pikachu_moved = True
        elif choice == "play with Pikachu" and Pikachu_moved:
            dead("Pikachu got angrier and electrified you")
        elif choice == "open door" and Pikachu_moved:
            Pokemonroom()
        else:
            print("I got no idea what that means.")


def wrong_room():
    print("Here you encounter the great evil Jun Ishida.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or Do you kill your self?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "kill" in choice:
        dead("Well that was tasty!")
    else:
        wrong_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You wake up and you find yourself at a corridor.")
    print("There are only two doors you can enter: Door1 or Door2.")
    print("Which door would you like to pick?")

    choice = input("> ")

    if choice == "Door1":
        wrong_room()
    elif choice == "Door2":
        Pikachu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
