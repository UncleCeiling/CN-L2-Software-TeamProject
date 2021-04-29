# pylint: disable=unused-variable
# Initialisation

    # Declare Variables

difficulty = 1                                          # Current difficulty setting - indexes via: difficulty_options[difficulty]
difficulty_options = ["Easy","Normal","Hard"]           # Possible difficulty options
level = 1
colour = "d"                                            # Current colour setting - indexes via: colour_options[0][colour_options.index(colour)]
colour_options = [["d","r","y","g","c","b","m","i"],["Default","Red","Yellow","Green","Cyan","Blue","Magenta","Default Inverted"],["\u001b[0m","\u001b[0m\u001b[31m","\u001b[0m\u001b[33m","\u001b[0m\u001b[32m","\u001b[0m\u001b[36m","\u001b[0m\u001b[34m","\u001b[0m\u001b[35m","\u001b[0m\u001b[30;47m"]] # Possible colour options, names and codes
player_health = 100                                     # Player hitpoints, when this reaches 0 you lose.
weapon = ["",0]                                         # Your weapon name, weapon points =len() of this string 
armour = ["",0]                                         # Your armour name, armour points =len() of this string
combat_room_count = 0                                   # Logs the number of combat rooms passed
puzzle_room_count = 0                                   # Logs the number of puzzle rooms passed
damage_dealt = 0                                        # Logs how much damage player has dealt for scoring purposes
damage_taken = 0                                        # Logs how much damage player has taken for scoring purposes
kill_count = 0
enemy_name = ""
enemy_health = 0
enemy_attack = 0
enemy_defence = 0

    # Import functions from libraries

from time import sleep
from os import chdir, path                              # To set Working Directory
from random import sample, randint, shuffle, choice            # For sampling lists

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
combat_room_desc = (open("storage/roomscombat.txt","r").readlines())[0].split(",")
puzzle_room_desc = (open("storage/roomspuzzle.txt", "r").readlines())[0].split(",")
enemies = (open("storage/enemies.txt","r").read()).split("\n")
for x in range(len(enemies)):
    enemies[(x-1)] = enemies[(x-1)].split(",")

# Functions

def reset():
    global player_health,weapon,armour,combat_room_count,puzzle_room_count,damage_dealt,damage_taken,kill_count,level
    player_health = 50
    weapon[0] = gen_weapon()
    armour[0] = gen_armour()
    weapon[1] = int(len(weapon[0].replace(" ","")))
    armour[1] = int(len(armour[0].replace(" ","")))
    combat_room_count = 0
    puzzle_room_count = 0
    damage_dealt = 0
    damage_taken = 0
    kill_count = 0
    level = 1

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
        print("\n========Codenation Blue-hats========\n\n        Cara Loft made by:\n\nPesh B\n\nSyed R\n\nAmir H\n\nMike D\n\nChris F\n")
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

def prize_give(buff_amount): # gives prizes - call to run a prize routine - takes an integer for power of reward
    global player_health
    global weapon
    global armour
    prize = sample(["a new weapon","some new armour","a weapon buff","an armour buff","some health"],1)
    print(f"\nCongratulations!\n\nYou won {prize}!")
    if prize in ["a weapon buff","an armour buff"]:
        if prize == "a weapon buff":
            weapon[0] = add_buff(weapon[0],buff_amount)
            print(f"\nTake a look at your {weapon[0]}!")
        else:
            armour[0] = add_buff(armour[0],buff_amount)
            print(f"\nTake a look at your {armour[0]}!")
        return
    elif prize in ["a new weapon","some new armour"]:
        if prize == "a new weapon":
            prize = add_buff(gen_weapon(),buff_amount)
            accept = input(f"\nDo you want to swap your\n\n{weapon[0]}\n\nFOR\n\n{prize}?\n\n>>>")[0].lower()
            while accept not in ["y","n"]:
                accept = input(f"\nFor real this time, pick an option from yes or no :\n\n>>>")[0].lower()
            if accept == "y":
                weapon[0] = prize
                player_stats
                return
            else:
                return
        else:
            prize = add_buff(gen_armour(),buff_amount)
            accept = input(f"\nDo you want to swap your\n\n{armour[0]}\n\nFOR\n\n{prize}?\n\n>>>")[0].lower()
            while accept not in ["y","n"]:
                accept = input(f"\nFor real this time, pick an option from yes or no :\n\n>>>")[0].lower()
            if accept == "y":
                armour[0] = prize
                player_stats
                return
            else:
                return
    else:
        print(f"\nYou gain {str(20*buff_amount)} Health Points!")
        player_health += (20*buff_amount)
        player_stats()

def game_intro(): # gives intro - call to start game process - returns true for start game, false for you lose
    print("\nYou are Cara Loft, international burial chamber pilferer.\n\nYou approach the entrance of an ancient tomb, rumoured to harbour untold dangers and even less told treasures.")
    print("\nᒥつ⑉⚊⑉ᒣつ <---This is you")
    player_stats()
    input_var = (input("\nHead forward? (y/n) :\n\n>>>"))[0].lower()
    while input_var not in ["y","n"]:
        input_var = (input("\nFor real this time, pick an option from yes or no :\n\n>>>"))[0].lower()
    if input_var == "y":
        print("\nYou enter the dungeon!")
        return True
    else:
        print("\nGo home, the burial chamber will remain unpilfered.")
        return False

def main_menu(): # is main menu - call to use menu - returns 1 (gamestart), 2(options), or 3(hs_creds)
    def print_main_menu():
        print("\nWelcome to Cara Loft: Burial Chamber Pilferer!\n\n====================================\n\n    [1] Start Game\n    [2] Settings\n    [3] Highscores and Credits\n    [0] Quit\n")
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

def gen_room(): # generates rooms and takes player selection - returns true if combat room selected, false if puzzle room
    combat_samples = randint(0, 3)   # Generates a random int from 0-3.
    options = sample(combat_room_desc, combat_samples) + sample(puzzle_room_desc, 3 - combat_samples) # Creates a list of 3 randomised strings from roomscombat.txt and roomspuzzle.txt.
    shuffle(options) # Shuffles the list so they aren't always in combat-puzzle order. 
    print(f"""There are 3 rooms before you:
    Door 1: {options[0]}
    Door 2: {options[1]}
    Door 3: {options[2]}""")
    input_var = (input("Please choose a door (A, B or C)"))[0].lower()
    while input_var not in ["a","b","c"]:
        input_var = (input("For real this time, pick an option from A, B or C : "))[0].lower()
    if input_var == "a":
        print("You open door A")
        if options[0] in combat_room_desc:
            print("It's a combat room!")
            return True
        else:
            print("It's a puzzle room!")
            return False
    elif input_var == "b":
        print("You open door B")
        if options[1] in combat_room_desc:
            print("It's a combat room!")
            return True
        else:
            print("It's a puzzle room!")
            return False
    else:
        print("You open door C")
        if options[2] in combat_room_desc:
            print("It's a combat room!")
            return True
        else:
            print("It's a puzzle room!")
            return False

def puzzle_room():
    def riddler():
        global player_health
        print("\nYou walk into a peculiar room, indescribable by words.\n\nI'm really struggling here as a narrator actually, it's impossible to give an accurate account of the qualities of this room using mere words alone.\n\nOne thing about this room is for sure though, it's a room of riddles.\n\nA riddler approaches, they too are indescribable, with their short red hair and green top hat with little ? symbols all over it. This riddler riddles you this.\n\n\"What question can you never answer yes to?\"\n\nWhat is your answer?\n\nA: Do you think CodeNation is a bit rubbish?\n\nB: Would you please stop trying to use 漢字 in everything Mike? It breaks the code.\n\nC: Can someone think of something to put here later?")
        input_var = input("A, B or C?")[0].lower()
        while input_var not in ["a","b","c"]:
            input_var = (input("\nFor real this time, pick an option from A, B or C :\n\n>>>"))[0].lower()
        if input_var == "a":
            print("\nCorrect! CodeNation is really really great!\n\nYou'd never say yes to that! Well done!")
            prize_give(level)
        else:
            print("\nWrong you fool! take your punishment!\nThe riddler's riddle proved to be indescribably difficult. You lost 20 Health points!")
            player_health -= 20
            player_stats()
    def monty_hall():
        global player_health
        global weapon
        global armour
        doors = ["trap", "trap", "prize"]
        ongoing = True
        shuffle(doors)
        print("\nAND OUR NEXT CONTESTANT... CARA LOFT!!!\n\nYou enter a room to thunderous applause, some sort of game show appears to be going on as a man in a crisp suit addresses a live studio audience.\n\nHe stands in front of 3 doors labelled A, B and C.\n\nBehind one of these doors is the equipment of your dreams, and behind the two others, deadly danger!\n\nStep right up Cara and choose a door!")
        input_var = input("\nChoose a door, A, B or C\n\n>>>")[0].lower()
        while input_var not in ["a","b","c"]:
            input_var = (input("\nFor real this time, pick an option from A, B or C :\n\n>>>"))[0].lower()
        while ongoing == True:
            if input_var == "a":
                print("\nYou chose door A!")
                if doors[0] == "trap":
                    print("\nDoor B is a trap door...\n\nDo you want to change to door C?")
                    input_2 = input("\nYes or no?\n\n>>>")
                    while input_2 not in ["y","n"]:
                        input_2 = (input("\nFor real this time, pick an option from yes or no :\n\n>>>"))[0].lower()
                    if input_2 == "y":
                        ongoing = False
                        input_var = "c"
                    elif input_2 == "n":
                        ongoing = False
                elif doors[2] == "trap":
                    print("\nDoor C is a trap door...\n\nDo you want to change to door B?\n\n>>>")
                    input_2 = input("\nYes or no?\n\n>>>")
                    while input_2 not in ["y","n"]:
                        input_2 = (input("\nFor real this time, pick an option from yes or no :\n\n>>>"))[0].lower()
                    if input_2 == "y":
                        ongoing = False
                        input_var = "b"
                    elif input_2 == "n":
                        ongoing = False
            if input_var == "b" and ongoing == True:
                print("\nYou chose door B!")
                if doors[0] == "trap":
                    print("\nDoor A is a trap door...\n\nDo you want to change to door C?")
                    input_2 = input("\nYes or no?\n\n>>>")
                    while input_2 not in ["y","n"]:
                        input_2 = (input("\nFor real this time, pick an option from yes or no :\n\n>>>"))[0].lower()
                    if input_2 == "y":
                        ongoing = False
                        input_var = "c"
                    elif input_2 == "n":
                        ongoing = False
                elif doors[2] == "trap":
                    print("\nDoor C is a trap door...\n\nDo you want to change to door A?")
                    input_2 = input("\nYes or no?\n\n>>>")
                    while input_2 not in ["y","n"]:
                        input_2 = (input("\nFor real this time, pick an option from yes or no :\n\n>>>"))[0].lower()
                    if input_2 == "y":
                        ongoing = False
                        input_var = "a"
                    elif input_2 == "n":
                        ongoing = False
            if input_var == "c" and ongoing == True:
                print("\nYou chose door C!")
                if doors[0] == "trap":
                    print("\nDoor A is a trap door...\n\nDo you want to change to door B?")
                    input_2 = input("\nYes or no?\n\n>>>")
                    while input_2 not in ["y","n"]:
                        input_2 = (input("\nFor real this time, pick an option from yes or no :\n\n>>>"))[0].lower()
                    if input_2 == "y":
                        ongoing = False
                        input_var = "b"
                    elif input_2 == "n":
                        ongoing = False
                elif doors[1] == "trap":
                    print("\nDoor B is a trap door!\n\nDo you want to change to door A?")
                    input_2 = input("\nYes or no?\n\n>>>")
                    while input_2 not in ["y","n"]:
                        input_2 = (input("\nFor real this time, pick an option from yes or no :\n\n>>>"))[0].lower()
                    if input_2 == "y":
                        ongoing = False
                        input_var = "a"
                    elif input_2 == "n":
                        ongoing = False
        if input_var == "a":
            print(f"\nWhat's behind door {input_var}?")
            print(f"\nIt's a {doors[0]}!")
            if doors[0] == "prize":
                prize_give(level)
            else:
                print("Oh no! the trap dealt 15 damage to you!")
                player_health -= 10
                player_stats()
        elif input_var == "b":
            print(f"What's behind door {input_var}?")
            print(f"It's a {doors[1]}!")
            if doors[0] == "prize":
                prize_give(level)
            else:
                print("Oh no! the trap dealt 15 damage to you!")
                player_health -= 10
                player_stats()
        elif input_var == "c":
            print(f"What's behind door {input_var}?")
            print(f"It's a {doors[2]}!")
            if doors[0] == "prize":
                prize_give(level)
            else:
                print("Oh no! the trap dealt 15 damage to you!")
                player_health -= 10
                player_stats()
        print("\nI've been your host, Honty Mall.\n\nSee you next time on \"What the heck is going on behind that dooooooooor!\"")
    def rock_paper_scissors():
        global player_health
        global weapon
        global armour
        enemy_choice = ["r","p","s"]
        shuffle(enemy_choice)
        print("You enter a large room filled with small gremlin like creatures. The gremlins are all sitting on picnic blankets playing rock paper scissors for food and weapons. A sign on the wall reads \"No Yogis\". You spot an empty place and decide to play.")
        input_var = (input("Choose rock, paper or scissors!"))[0].lower()
        while input_var not in ["r","p","s"]:
            input_var = (input("For real this time, pick an option from rock, paper or scissors : "))[0].lower()
        if input_var == "r":
            print("You choose rock!")
            if enemy_choice[0] == "p":
                print("\nThe gruff gremlin chose paper.")
                print("\nToo bad, you lost!")
                print("\nOh no!\n\nThe gremlin dealt 10 damage to you!")
                player_health -= 10
                player_stats()
            elif enemy_choice[0] == "s":
                print("The gruff gremlin chose scissors.")
                print("Congratulations, you win!")
                prize_give(level)
            else:
                print("The gruff gremlint chose rock.")
                print("It's a tie! Rematch!")
                rock_paper_scissors()
        elif input_var == "p":
            print("You choose paper!")
            if enemy_choice[0] == "s":
                print("\nThe gruff gremlin chose paper.")
                print("\nToo bad, you lost!")
                print("\nOh no!\n\nThe gremlin dealt 10 damage to you!")
                player_health -= 10
                player_stats()
            elif enemy_choice[0] == "r":
                print("The gruff gremlin chose rock.")
                print("Congratulations, you win!")
                prize_give(level)
            else:
                print("The gruff gremlin chose paper.")
                print("It's a tie! Rematch!")
                rock_paper_scissors()
        elif input_var == "s":
            print("You choose scissors!")
            if enemy_choice[0] == "r":
                print("\nThe gruff gremlin chose paper.")
                print("\nToo bad, you lost!")
                print("\nOh no!\n\nThe gremlin dealt 10 damage to you!")
                player_health -= 10
                player_stats()
            elif enemy_choice[0] == "p":
                print("The gruff gremlin chose paper.")
                print("Congratulations, you win!")
                prize_give(level)
            else:
                print("The gruff gremlin chose scissors.")
                print("It's a tie! Rematch!")
                rock_paper_scissors()
        else:
            print("Hmmm, that was weird... Shame I can't describe it to you...")
    def match_2():
        global weapon
        global armour
        print("snap")
    def fruit_and_anvil():
        global player_health
        global weapon
        global armour
        print("\nYou enter a room with a large pile of fruit and an anvil, the door locks behind you.\n\nA large sign above the opposite door informs you that you have 1 hour until you can proceed.\n\nSeems like you'll only have time to use one, what do you do?")
        input_var = (input("\nEat the fruit or use the anvil?\n\n>>>"))[0].lower()
        while input_var not in ["a","f","u","e"]:
            input_var = (input("\nFor real this time, pick an option from eating the fruit or using the anvil :\n\n>>>"))[0].lower()
        if input_var in ["a","u"]:
            input_var = (input(f"\nWhat would you like to upgrade on?\n\nYour Weapon - {weapon[0]}?\nOR\nYour Armour - {armour[0]}?\n\n>>>"))[0].lower()
            while input_var not in ["w","a"]:
                input_var = (input("\nFor real this time, pick an option from eating the fruit or using the anvil :\n\n>>>"))[0].lower()
            if input_var == "w":
                print(f"\nYour weapon '{weapon[0]}' becomes:")
                weapon[0] = add_buff(weapon[0],1)
                print(f"\n'{weapon[0]}'")
            else:
                print(f"\nYour armour '{armour[0]}' becomes:")
                armour[0] = add_buff(armour[0],1)
                print(f"\n'{armour[0]}'")
            player_stats()
            return
        else:
            print("\nYou eat the pile of fruit and gain 50 Health Points!")
            player_health += 50
            player_stats()
        return
    puzzle_list = [monty_hall,rock_paper_scissors,match_2,fruit_and_anvil,riddler]
    choice(puzzle_list)()
    return

def player_turn(): # Function for player attacking the enemy.
    global enemy_health
    global damage_dealt
    player_damage = randint(int(round(weapon[1]-weapon[1]/2)), weapon[1])
    enemy_block = randint(int(round(enemy_defence-enemy_defence/2)), enemy_defence)
    damage = player_damage - enemy_block
    
    if damage > 0:
        enemy_health = enemy_health - damage
        damage_dealt = damage_dealt + damage
        print(f"You attacked for {player_damage} damage!")
        sleep(0.5)
        print(f"{enemy_name} blocked {enemy_block}!")
        sleep(0.5)
        print(f"You dealt {damage} damage to the enemy!")
    else:
        print(f"You attacked {enemy_name} for {player_damage} damage!")
        sleep(0.5)
        print(f"{enemy_name} blocked {enemy_block}!")
        sleep(0.5)
        print(f"You dealt no damage to {enemy_name}!")

def enemy_turn(): # Function for basic enemy attack
    global player_health
    global damage_taken
    enemy_damage = randint(int(round(enemy_attack-enemy_attack/2)), enemy_attack)
    player_block = randint(int(round(armour[1]-armour[1]/2)), armour[1])
    damage = enemy_damage - player_block
    
    if damage > 0:
        player_health = player_health - damage
        damage_taken = damage_taken + damage
        print(f"{enemy_name} attacked for {enemy_damage} damage!")
        sleep(0.5)
        print(f"You blocked {player_block}!")
        sleep(0.5)
        print(f"{enemy_name} did {damage} damage to you!")
        if player_health < 0:
            death_screen()
    else:
        print(f"{enemy_name} attacked for {enemy_damage} damage!")
        sleep(0.5)
        print(f"You blocked {player_block}!")
        sleep(0.5)
        print(f"You blocked all the damage!")

def combat_room():
    global player_health,enemy_name,enemy_health,enemy_attack,enemy_defence,kill_count
    combat = True
    dead = False
    dead = False
    enemy_stats = sample(enemies,1)[0]
    print(enemy_stats)
    enemy_name = enemy_stats[0]
    enemy_health = int(enemy_stats[1])
    enemy_attack = int(enemy_stats[2])
    enemy_defence = int(enemy_stats[3])
    print(f"A {enemy_name} appears! What do you do?")
    while combat == True:
        input_var = (input("Attack, talk or run?"))[0].lower()
        while input_var not in ["a","t", "r"]:
            input_var = (input("For real this time, pick an option from attack, talk or run : "))[0].lower()
        if input_var == "a":
            player_turn()
            sleep(0.5)
            if enemy_health > 0:
                print(f"***{enemy_name}'s turn***")
                enemy_turn()
            else:
                combat = False
                dead = True
        elif input_var == "t":
            print("You try making smalltalk with the enemy.")
            sleep(0.5)
            print("...")
            sleep(0.5)
            print("The enemy attacks you!")
            enemy_turn()
        else:
            combat = False
    if dead == True:
        kill_count += 1
        print("You killed the enemy!")
        sleep(0.5)
        prize_give(level)
    else:
        if enemy_health < weapon[1] + armour[1]:
            print(f"You managed to escape {enemy_name}!")
        else:
            print("Can't escape!") 


def death_screen():
    print(f"""
    Oh no! You died!

    You dealt {damage_dealt} damage, but received {damage_taken}.
    
    You visited {combat_room_count} Combat rooms and {puzzle_room_count} Puzzle rooms.

    You killed {kill_count} enemies""")
    input("\nEnter something to return to the main menu:\n\n>>>")

def highscore_screen():
    global hs1,hs2,hs3
    score = combat_room_count+puzzle_room_count
    if score < hs3[1]:
        print("\nYou did not beat any highscores...")
        reset()
        return
    else:
        name = input("\nNew Highscore!\n\nEnter your name below :\n\n>>>").title()
        if score < hs2[1]:
            hs3 = [name,score]
        elif score < hs1[1]:
            hs3 = hs2
            hs2 = [name,score]
        elif score >= hs1[1]:
            hs3 = hs2
            hs2 = hs1
            hs1 = [name,score]
        reset()
        return

def store_highscore():
    print("store_highscore")
# Generate starting weapon and armour

weapon[0] = gen_weapon()
armour[0] = gen_armour()

# Testing

# Main block


start_function()
main_menu_selection = 0
while main_menu_selection != 1:
    main_menu_selection = main_menu()
intro_complete = game_intro()
if intro_complete == False:
    print("THE END") # PLACEHOLDER
    quit()
else:
    while player_health > 0:
        room_type = gen_room()
        if room_type == True:
            combat_room()
            combat_room_count += 1
        else:
            puzzle_room()
            puzzle_room_count += 1
    death_screen()
    highscore_screen()
    store_highscore()