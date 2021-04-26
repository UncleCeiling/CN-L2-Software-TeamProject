# pylint: disable=unused-variable
# Initialisation

    # Declare Variables

difficulty = 1                                          # Current difficulty setting - indexes via: difficulty_options[difficulty]
difficulty_options = ["Easy","Normal","Hard"]           # Possible difficulty options
colour = "d"                                            # Current colour setting - indexes via: colour_options[0][colour_options.index(colour)]
colour_options = [["d","r","y","g","c","b","m","i"],["Default","Red","Yellow","Green","Cyan","Blue","Magenta","Default Inverted"],["\u001b[0m","\u001b[0m\u001b[31m","\u001b[0m\u001b[33m","\u001b[0m\u001b[32m","\u001b[0m\u001b[36m","\u001b[0m\u001b[34m","\u001b[0m\u001b[35m","\u001b[0m\u001b[30;47m"]] # Possible colour options, names and codes

    # Import functions from libraries

from os import chdir, path                              # To set Working Directory
from random import sample                               # For sampling lists

    # Set Working directory to file directory

chdir(path.dirname(__file__))

    # Import data from .txt into arrays - example layout:
    # var_name = (open("txt_file_name.txt","r").readlines())[0].split(",")

highscore = (open("highscore.txt","r").readlines())[0].split(",")
adjective = (open("weapon_adjectives.txt", "r").readlines())[0].split(",")
noun1 = (open("weapon_nouns1.txt", "r").readlines())[0].split(",")
noun2 = (open("weapon_nouns2.txt", "r").readlines())[0].split(",")

# Functions

def sar_start_function(): # Syed's start function (HAS PLACEHOLDER - line 31)
    print("start screen")
    var = input("Please enter something to continue : ")
    if var == (""):
        sar_start_function()
    else:
        return

def gen_weapon(): # Weapon Generator - call to generate a weapon - returns a string
    sample_adjective = sample(adjective,1)[0]
    sample_noun1 = sample(noun1,1)[0]
    sample_noun2 = sample(noun2,1)[0]
    return (f"{sample_adjective} {sample_noun1} of {sample_noun2}")

def options_menu(): # Options Menu - call to run options - does not return anything
    def print_options_main():                                               # Prints the options menu
        print(f"\n============OPTIONS MENU============\n\n       Difficulty||{difficulty_options[difficulty]}\n\n      Text Colour||{colour_options[1][colour_options[0].index(colour)]}\n\n================Exit================") #36 characters wide - print menu
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



player_health = 50                                # Player hitpoints, when this reaches 0 you lose.
weapon = "I want twenty attack plz"               # Your weapon name, weapon points =len() of this string (- white space maybe?) 
armour = "Okay Armour"                            # Your armour name, armour points =len() of this string (- white space maybe?) 
weapon_points = len(weapon.replace(" ", ""))      # player weapon points, effects how much damage player attacks do.
armour_points = len(armour.replace(" ", ""))      # Player armour points, effects how much damage player blocks when they defend.

def equipment_calc():
    weapon_points = len(weapon.replace(" ", "")) 
    armour_points = len(armour.replace(" ", "")) 

# Call to update weapon and armour points.

def player_stats():
    equipment_calc() 
    print(f"You have:\n{player_health} hit points remaining\n{weapon}: {weapon_points} power\n{armour}: {armour_points} defence")

# Call to update weapon and armour points and print the current player stats.

def game_intro():
    print("You are Crara Loft, international burial chamber pilferer. You approach the entrance of an ancient tomb, rumoured to harbour untold dangers and even less told treasures.")
    print("ᒥつ⑉⚊⑉ᒣつ <---This is you")
    player_stats()
    input_var = (input("Head forward? (y/n)"))[0].lower()
    while input_var not in ["y","n"]:
        input_var = (input("For real this time, pick an option from yes or no : "))[0].lower()
    if input_var == "y":
        print("You enter the dungeon!")
        return True
    else:
        print("Go home, the burial chamber will remain unpilfered.")
        reuturn False

# Call to start the game

# Main block
