# pylint: disable=unused-variable
# Initialisation

    # Declare Variables

difficulty = 1                                          # Current difficulty setting - indexes via: difficulty_options[difficulty]
difficulty_options = ["Easy","Normal","Hard"]           # Possible difficulty options
colour = "d"                                            # Current colour setting - indexes via: colour_options[0][colour_options.index(colour)]
colour_options = [["d","r","y","g","c","b","m","i"],["Default","Red","Yellow","Green","Cyan","Blue","Magenta","Default Inverted"],["\u001b[0m","\u001b[0m\u001b[31m","\u001b[0m\u001b[33m","\u001b[0m\u001b[32m","\u001b[0m\u001b[36m","\u001b[0m\u001b[34m","\u001b[0m\u001b[35m","\u001b[0m\u001b[30;47m"]] # Possible colour options, names and codes
player_health = 50                                # Player hitpoints, when this reaches 0 you lose.
weapon = ["I want twenty attack plz",20]          # Your weapon name, weapon points =len() of this string (- white space maybe?) 
armour = ["Okay Armour",10]                       # Your armour name, armour points =len() of this string (- white space maybe?)

    # Import functions from libraries

import time
from os import chdir, path                              # To set Working Directory
from random import sample, randint, shuffle             # For sampling lists

    # Set Working directory to file directory

chdir(path.dirname(__file__))

    # Import data from .txt into arrays - example layout:
    # var_name = (open("txt_file_name.txt","r").readlines())[0].split(",")

highscore = (open("storage/highscore.txt","r").read()).split("\n")
hs1 = str(highscore[0]).split(",")
hs2 = str(highscore[1]).split(",")
hs3 = str(highscore[2]).split(",")
adjective = (open("storage/adjectives.txt","r").readlines())[0].split(",")
wep_noun = (open("storage/weapon_nouns.txt", "r").readlines())[0].split(",")
arm_noun = (open("storage/armour_nouns.txt", "r").readlines())[0].split(",")
noun2 = (open("storage/nouns2.txt", "r").readlines())[0].split(",")
combat_room = (open("storage/roomscombat.txt","r").readlines())[0].split(",")
puzzle_room = (open("storage/roomspuzzle.txt", "r").readlines())[0].split(",")
# print(highscore, adjective,wep_noun,arm_noun,noun2,combat_room,puzzle_room) # Debug line

# Functions

def start_function(): # Syed's start function (HAS PLACEHOLDER - line 31)
    print("\nstart screen\n")
    var = input("Please enter something to continue : ")
    if var == (""):
        start_function()
    else:
        return

def hs_creds_page():
    def print_highscore():
        print(f"\n=============HIGH SCORES============\n\n{hs1[0]} : {hs1[1]}\n\n{hs2[0]} : {hs2[1]}\n\n{hs3[0]} : {hs3[1]}\n")
    def print_credits():
        print("\n========Codenation Blue-hats========\n\n        Crara Loft made by:\n\nPesh B\n\nSyed R\n\nAmir H\n\nMike D\n\nChris F\n")
    print_highscore()
    print_credits()
    print("====================================\n")
    taken_input = input("\nType something to return to the menu : ")
    while taken_input == "":
        taken_input = input("\nType something to return to the menu : ")
    return

def gen_weapon(): # Weapon Generator - call to generate a weapon - returns a string
    sample_noun1 = sample(wep_noun,1)[0]
    sample_noun2 = sample(noun2,1)[0]
    return (f"{sample_noun1} of {sample_noun2}".title())

def gen_armour(): # Weapon Generator - call to generate armour - returns a string
    sample_noun1 = sample(arm_noun,1)[0]
    sample_noun2 = sample(noun2,1)[0]
    return (f"{sample_noun1} of {sample_noun2}".title())

def add_buff(equip_in,num_of_buffs): # adds adjectives to weapon_in - returns a string
    sample_adj = sample(adjective,num_of_buffs)
    buff = ' '.join(sample_adj)
    return (f"{buff} {equip_in}".title())

def options_menu(): # Options Menu - call to run options - does not return anything
    def print_options_main():                                               # Prints the options menu
        print(f"\n============OPTIONS MENU============\n\n       Difficulty||{difficulty_options[difficulty]}\n\n      Text Colour||{colour_options[1][colour_options[0].index(colour)]}\n\n================Exit================\n") #36 characters wide - print menu
    def difficulty_menu():                                                  # Difficulty Menu - call to run diff options - does not return anything
        def print_diff_menu(): # Prints the diff menu
            print(f"\n==========DIFFICULTY MENU===========\n\n  Difficulty is currently: {difficulty_options[difficulty]}\n\n    Easy       Normal       Hard\n\n================Exit================")
        global difficulty
        print_diff_menu() #print difficulty menu
        option_choice = (input("\nPlease select a difficulty : "))[0].lower() #take diff input
        while option_choice not in ["e","n","h"]: #if invalid input, ask again, but sassy
            print_diff_menu
            option_choice = (input("Hmmm, not sure that's an option...\nWhy don't you try something else?\n\nPlease select an option : "))[0].lower()
        if option_choice == "e": #easy
            print("\nSetting difficulty to Easy")
            difficulty = 0
        elif option_choice == "n": #normal
            print("\nSetting difficulty to Normal")
            difficulty = 1
        elif option_choice == "h": #hard
            print("\nSetting difficulty to Hard")
            difficulty = 2
        else: #shouldn't happen, but here just in case
            print("\nThat didn't work, sorry!\n\nReturning you to the options menu...\n")
        return
    def colour_menu():                                                      # Colour Menu - call to run colour options - does not return anything
        def print_colour_menu(): # Prints the colour menu
            print(f"{colour_options[2][colour_options[0].index(colour)]}============COLOUR MENU=============\n\n    Colour is currently: {colour_options[1][colour_options[0].index(colour)]}\n    \u001b[0m                            {colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m|Default |  \u001b[31mRed\u001b[0m   | \u001b[33mYellow\u001b[0m |{colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m                            {colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m| \u001b[32mGreen\u001b[0m  |  \u001b[36mCyan\u001b[0m  |  \u001b[34mBlue\u001b[0m  |{colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m                            {colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m|   \u001b[35mMagenta\u001b[0m  |\u001b[30;47m  Inverted   \u001b[0m|{colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m                            {colour_options[2][colour_options[0].index(colour)]}\n================Exit================")
        global colour # To change back to current colour, use f"{colour_options[2][colour_options[0].index(colour)]}TEXT HERE"
        print_colour_menu() # Print colour menu
        colour_choice = (input("\nPlease select a colour : "))[0].lower()   # Take colour input
        while colour_choice not in (colour_options[0]+["e"]):               # If invalid input, ask again, but sassy
            print_colour_menu
            colour_choice = (input("\nHmmm, not sure that's an option...\nWhy don't you try something else?\n\nPlease select an colour : "))[0].lower()
        if colour_choice in colour_options[0]:                              # If colour selected, change colour
            colour = colour_choice                                          # Make change in variables
            print(f"\nSwitching colour to {colour_options[2][colour_options[0].index(colour)]}{colour_options[1][colour_options[0].index(colour)]}") # Print Message
        elif colour_choice == "e":                                          # If exit selected, exit to the options menu
            print("\nExiting to Options Menu...")                           # Print Message
        else:                                                               # Shouldn't happen, but here just in case
            print("\nThat didn't work, sorry!\n\nReturning you to the options menu...\n") # Print Message
        return                                                              # Go back - I WANT TO BE MONKE
    print_options_main()                                                    # Print menu
    option_choice = (input("\nPlease select an option : "))[0].lower()      # Ask for Input
    while option_choice not in ["d","c","t","e"]:                           # Check if input is valid
        print_options_main()                                                # Print menu when not valid
        option_choice = (input("Hmmm, not sure that's an option...\nWhy don't you try something else?\n\nPlease select an option : "))[0].lower() # Chastise and take new input
    if option_choice == "d":                                                # Check if input was difficulty
        difficulty_menu()                                                   # Run diff menu
        options_menu()                                                      # After diff menu is finished, open up the options menu again
    elif option_choice in ["c","t"]:                                        # Check if input was colour or text
        colour_menu()                                                       # Run colour menu
        options_menu()                                                      # After colour menu is finished, open up the options menu again
    print("\nReturning to Main Menu...")                                    # Exit must have been selected so print a message and exit
    return

def update_equipment(): # Updates integer values for equipment
    global weapon
    global armour
    weapon[1] = len(weapon[0].replace(" ", "")) 
    armour[1] = len(armour[0].replace(" ", "")) 

def player_stats(): # prints player inv/stats
    update_equipment() 
    print(f"You have:\n{player_health} hit points remaining\n{weapon[0]}: {weapon[1]} power\n{armour[0]}: {armour[1]} defence")

def game_intro(): # gives intro - call to start game process - returns true for start game, false for you lose
    print("You are Crara Loft, international burial chamber pilferer.\n\nYou approach the entrance of an ancient tomb, rumoured to harbour untold dangers and even less told treasures.\n")
    print("ᒥつ⑉⚊⑉ᒣつ <---This is you\n")
    player_stats()
    input_var = (input("\nHead forward? (y/n) : "))[0].lower()
    while input_var not in ["y","n"]:
        input_var = (input("\nFor real this time, pick an option from yes or no : "))[0].lower()
    if input_var == "y":
        print("\nYou enter the dungeon!")
        return True
    else:
        print("\nGo home, the burial chamber will remain unpilfered.")
        return False

def main_menu(): # is main menu - call to use menu - returns 1 (gamestart), 2(options), or 3(hs_creds)
    def print_main_menu():
        print("\nWelcome to Crara Loft: Burial Chamber Pilferer!\n\n====================================\n\n    [1] Start Game\n    [2] Settings\n    [3] Highscores and Credits\n    [0] Quit\n")
    print_main_menu()
    option = int(input("Enter your selection "))
    while option != 0:
        if option == 1:
            print("Lets Goooo!")
            return 1
        elif option == 2:
            options_menu()
            return
        elif option == 3:
            hs_creds_page()
            return
        else:
            print("Invalid option")
    quit()

def room_generator(): # generates rooms and takes player selection - returns true if combat room selected, false if puzzle room
    combat_samples = randint(0, 3)   # Generates a random int from 0-3.
    options = sample(combat_room, combat_samples) + sample(puzzle_room, 3 - combat_samples) # Creates a list of 3 randomised strings from roomscombat.txt and roomspuzzle.txt.
    shuffle(options)   # Shuffles the list so they aren't always in combat-puzzle order. 

    print(f"""There are 3 rooms before you:
    Door 1: {options[0]}
    Door 2: {options[1]}
    Door 3: {options[2]}""")
    input_var = (input("Please choose a door (A, B or C)"))[0].lower()
    while input_var not in ["a","b","c"]:
        input_var = (input("For real this time, pick an option from A, B or C : "))[0].lower()
    if input_var == "a":
        print("You open door A")
        if options[0] in (open(path.join("storage", "roomscombat.txt"),"r").readlines())[0].split(","):
            print("It's a combat room!")
            return True
        else:
            print("It's a puzzle room!")
            return False
    elif input_var == "b":
        print("You open door B")
        if options[1] in (open(path.join("storage", "roomscombat.txt"),"r").readlines())[0].split(","):
            print("It's a combat room!")
            return True
        else:
            print("It's a puzzle room!")
            return False
    else:
        print("You open door C")
        if options[2] in (open(path.join("storage", "roomscombat.txt"),"r").readlines())[0].split(","):
            print("It's a combat room!")
            return True
        else:
            print("It's a puzzle room!")
            return False

# Testing

# Main block

start_function()
main_menu_selection = 0
while main_menu_selection != 1:
    main_menu_selection = main_menu()
intro_complete = game_intro()
if intro_complete == False:
    print("THE END") # PLACEHOLDER
else:
    print("You play the game") # PLACEHOLDER

# TEMP
from os import chdir, path, scandir, walk                            # To set Working Directory
from random import sample, randint, shuffle                              # For sampling lists


chdir(path.dirname(__file__))


def room_selecter():
    combat_room = (open(path.join("storage", "roomscombat.txt"),"r").readlines())[0].split(",")
    puzzle_room = (open(path.join("storage", "roomspuzzle.txt"), "r").readlines())[0].split(",")
    combat_samples = randint(0, 3)   # Generates a random int from 0-3.
    options = sample(combat_room, combat_samples) + sample(puzzle_room, 3 - combat_samples) # Creates a list of 3 randomised strings from roomscombat.txt and roomspuzzle.txt.
    shuffle(options)   # Shuffles the list so they aren't always in combat-puzzle order. 

    print(f"""There are 3 rooms before you:
    Door 1: {options[0]}
    Door 2: {options[1]}
    Door 3: {options[2]}""")
    input_var = (input("Please choose a door (A, B or C)"))[0].lower()
    while input_var not in ["a","b","c"]:
        input_var = (input("For real this time, pick an option from A, B or C : "))[0].lower()
    if input_var == "a":
        print("You open door A")
        if options[0] in (open(path.join("storage", "roomscombat.txt"),"r").readlines())[0].split(","):
            return True
        else:
            return False
    elif input_var == "b":
        print("You open door B")
        if options[1] in (open(path.join("storage", "roomscombat.txt"),"r").readlines())[0].split(","):
            return True
        else:
            return False
    else:
        print("You open door C")
        if options[2] in (open(path.join("storage", "roomscombat.txt"),"r").readlines())[0].split(","):
            return True
        else:
            return False
# You choose between doors A, B and C and the function returns true if that door is a combat room and false if it is a puzzle room.

# room_selecter()

def room_generator():
    global combat_rooms
    global puzzle_rooms
    room_type =room_selecter()
    if room_type == True:
        combat_rooms += 1
        print("It's a combat room!")
        # Code to call a random combat???
    else:
        puzzle_rooms += 1
        print("It's a puzzle room!")
        # Code to call a random puzzle???

room_generator()

from os import chdir, path, scandir, walk                            # To set Working Directory
from random import sample, randint, shuffle                              # For sampling lists


chdir(path.dirname(__file__))


def room_selecter():
    combat_room = (open(path.join("storage", "roomscombat.txt"),"r").readlines())[0].split(",")
    puzzle_room = (open(path.join("storage", "roomspuzzle.txt"), "r").readlines())[0].split(",")
    combat_samples = randint(0, 3)   # Generates a random int from 0-3.
    options = sample(combat_room, combat_samples) + sample(puzzle_room, 3 - combat_samples) # Creates a list of 3 randomised strings from roomscombat.txt and roomspuzzle.txt.
    shuffle(options)   # Shuffles the list so they aren't always in combat-puzzle order. 

    print(f"""There are 3 rooms before you:
    Door 1: {options[0]}
    Door 2: {options[1]}
    Door 3: {options[2]}""")
    input_var = (input("Please choose a door (A, B or C)"))[0].lower()
    while input_var not in ["a","b","c"]:
        input_var = (input("For real this time, pick an option from A, B or C : "))[0].lower()
    if input_var == "a":
        print("You open door A")
        if options[0] in (open(path.join("storage", "roomscombat.txt"),"r").readlines())[0].split(","):
            return True
        else:
            return False
    elif input_var == "b":
        print("You open door B")
        if options[1] in (open(path.join("storage", "roomscombat.txt"),"r").readlines())[0].split(","):
            return True
        else:
            return False
    else:
        print("You open door C")
        if options[2] in (open(path.join("storage", "roomscombat.txt"),"r").readlines())[0].split(","):
            return True
        else:
            return False
# You choose between doors A, B and C and the function returns true if that door is a combat room and false if it is a puzzle room.

# room_selecter()

def room_generator():
    global combat_rooms
    global puzzle_rooms
    room_type =room_selecter()
    if room_type == True:
        combat_rooms += 1
        print("It's a combat room!")
        # Code to call a random combat???
    else:
        puzzle_rooms += 1
        print("It's a puzzle room!")
        # Code to call a random puzzle???

room_generator()

import random as r
# Monty Hall problem
def monty_hall():
    a = ["a", "A"]
    b = ["b", "B"]
    c = ["c", "C"]
    yes = ["Y", "y", "Yes", "yes", "YES"]
    no = ["N", "n", "No", "no", "NO"]
    invalid_ans = ("\nPlease use a valid input!\n")
    doors = ["trap", "trap", "prize"]
    ongoing = True

    r.shuffle(doors)
    # print(doors) #Debug code

    print("Pick a door(a, b or c)")
    choice_1 = input(">>>").lower()
    if choice_1 in a and ongoing == True or choice_1 in b and ongoing == True or choice_1 in c and ongoing == True:
        while choice_1 in a and ongoing == True:
            if doors[0] == "trap":
                print("Door b is a trap door! Do you want to change to door c? (y/n)")
                choice_2 = input(">>>")
                if choice_2 in yes:
                    ongoing = False
                    choice_1 = "c"
                elif choice_2 in no:
                    ongoing = False
                else:
                    print(invalid_ans)
            elif doors[2] == "trap":
                print("Door c is a trap door! Do you want to change to door b? (y/n)")
                choice_2 = input(">>>")
                if choice_2 in yes:
                    ongoing = False
                    choice_1 = "b"
                elif choice_2 in no:
                    ongoing = False
                else:
                    print(invalid_ans)
        while choice_1 in b and ongoing == True:
            if doors[0] == "trap":
                print("Door a is a trap door! Do you want to change to door c? (y/n)")
                choice_2 = input(">>>")
                if choice_2 in yes:
                    ongoing = False
                    choice_1 = "c"
                elif choice_2 in no:
                    ongoing = False
                else:
                    print(invalid_ans)
            elif doors[2] == "trap":
                print("Door c is a trap door! Do you want to change to door a? (y/n)")
                choice_2 = input(">>>")
                if choice_2 in yes:
                    ongoing = False
                    choice_1 = "a"
                elif choice_2 in no:
                    ongoing = False
                else:
                    print(invalid_ans)
        while choice_1 in c and ongoing == True:
            if doors[0] == "trap":
                print("Door a is a trap door! Do you want to change to door b? (y/n)")
                choice_2 = input(">>>")
                if choice_2 in yes:
                    ongoing = False
                    choice_1 = "b"
                elif choice_2 in no:
                    ongoing = False
                else:
                    print(invalid_ans)
            elif doors[1] == "trap":
                print("Door b is a trap door! Do you want to change to door a? (y/n)")
                choice_2 = input(">>>")
                if choice_2 in yes:
                    ongoing = False
                    choice_1 = "a"
                elif choice_2 in no:
                    ongoing = False
                else:
                    print(invalid_ans)

    else:
        print(invalid_ans)
        monty_hall()

    if choice_1 == "a":
        print(f"What's behind door {choice_1}?")
        print(f"{doors[0]}")
    elif choice_1 == "b":
        print(f"What's behind door {choice_1}?")
        print(f"{doors[1]}")
    elif choice_1 == "c":
        print(f"What's behind door {choice_1}?")
        print(f"{doors[2]}")

import time
import random as r
import math

battle_choice = "Attack, talk or run?"
player_health = 9001                              # Player hitpoints, when this reaches 0 you lose.
weapon = ["I want twenty attack plz", 20]         # Your weapon name, weapon points =len() of this string (- white space maybe?) 
armour = ["Okay Armour", 10]                      # Your armour name, armour points =len() of this string (- white space maybe?) 
damage_dealt = 0                                  # Logs how much damage player has dealt for scoring purposes
damage_taken = 0                                  # Logs how much damage player has taken for scoring purposes

def death_screen():
    print("You died lol")

def player_attack():
    global enemy_health
    global player_damage
    global enemy_defence_p
    global damage_dealt
    player_damage = r.randint(int(round(weapon[1]-weapon[1]/2)), weapon[1])
    enemy_block = r.randint(int(round(enemy_defence_p-enemy_defence_p/2)), enemy_defence_p)
    damage = player_damage - enemy_block
    
    if damage > 0:
        enemy_health = enemy_health - damage
        damage_dealt = damage_dealt + damage
        print(f"You attacked for {player_damage} damage!")
        time.sleep(0.5)
        print(f"{enemy_name} blocked {enemy_block}!")
        time.sleep(0.5)
        print(f"You dealt {damage} damage to the enemy!")
    else:
        print(f"You attacked {enemy_name} for {player_damage} damage!")
        time.sleep(0.5)
        print(f"{enemy_name} blocked {enemy_block}!")
        time.sleep(0.5)
        print(f"You dealt no damage to {enemy_name}!")
# Function for player attacking the enemy.

def enemy_attack():
    global player_health
    global enemy_damage
    global damage_taken
    enemy_damage = r.randint(int(round(enemy_attack_p-enemy_attack_p/2)), enemy_attack_p)
    player_block = r.randint(int(round(armour[1]-armour[1]/2)), armour[1])
    damage = enemy_damage - player_block
    
    if damage > 0:
        player_health = player_health - damage
        damage_taken = damage_taken + damage
        print(f"{enemy_name} attacked for {enemy_damage} damage!")
        time.sleep(0.5)
        print(f"You blocked {player_block}!")
        time.sleep(0.5)
        print(f"{enemy_name} did {damage} damage to you!")
        if player_health < 0:
            death_screen()
    else:
        print(f"{enemy_name} attacked for {enemy_damage} damage!")
        time.sleep(0.5)
        print(f"You blocked {player_block}!")
        time.sleep(0.5)
        print(f"You blocked all the damage!")
# Function for basic enemy attack, although more complex attacks can be made for specific enemies. See Mathemagician for example

def enemy_1():
    global enemy_name
    global enemy_health
    global enemy_attack_p
    global enemy_defence_p
    global player_defence_p
    global player_health
    global player_health
    global enemy_damage
    global player_block
    global kill_count
    combat = True
    dead = False
    battle = True
    dead = False
    enemy_name = "The enemy"
    enemy_health = 100
    enemy_attack_p = 20
    enemy_defence_p = 2
    print(f"An {enemy_name} appears! What do you do?")
    while battle == True:
        input_var = (input("Attack, talk or run?"))[0].lower()
        while input_var not in ["a","t", "r"]:
            input_var = (input("For real this time, pick an option from attack, talk or run : "))[0].lower()
        if input_var == "a":
            player_attack()
            time.sleep(0.5)
            if enemy_health > 0:
                print(f"***{enemy_name}'s turn***")
                enemy_attack()
            else:
                battle = False
                dead = True
        elif input_var == "t":
            print("You try making smalltalk with the enemy.")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print("The enemy ignores you.")
            time.sleep(0.5)
        else:
            battle = False
    if dead == True:
        kill_count += 1
        print("You killed the enemy!")
        time.sleep(0.5)
        print(f"You have {player_health} hit points left.")
    else:
        print(f"You casually walk past {enemy_name}")
        time.sleep(0.5)
        print(f"{enemy_name} watches you leave.")
        time.sleep(0.5)
        print(f"You managed to escape {enemy_name}!")
    print(f"You have dealt {damage_dealt} damage.")    
    print(f"You have taken {damage_taken} damage.")    
# A basic enemy/ template for combats.