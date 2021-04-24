# pylint: disable=unused-variable
# Initialisation

    # Declare Variables

difficulty = 1                                          # Current difficulty setting - indexes via: difficulty_options[difficulty]
difficulty_options = ["Easy","Normal","Hard"]           # Possible difficulty options
colour = "d"                                            # Current colour setting - indexes via: colour_options[0][colour_options.index(colour)]
colour_options = [["d","r","y","g","c","b","m","i"],["Default","Red","Yellow","Green","Cyan","Blue","Magenta","Default Inverted"],["\u001b[0m","\u001b[31m","\u001b[33m","\u001b[32m","\u001b[36m","\u001b[34m","\u001b[35m","\u001b[30;47m"]] # Possible colour options, names and codes

    # Import functions from libraries

from os import chdir, path                              # To set Working Directory
from random import sample                               # For sampling lists

    # Set Working directory to file directory

chdir(path.dirname(__file__))

    # Import data from .txt into arrays - example layout:
    # var_name = (open("txt_file_name.txt","r").readlines())[0].split(","))

adjective = (open("weapon_adjectives.txt", "r").readlines())[0].split(",")
noun1 = (open("weapon_nouns1.txt", "r").readlines())[0].split(",")
noun2 = (open("weapon_nouns2.txt", "r").readlines())[0].split(",")

# Functions

def gen_weapon(): # Simple Weapon Generator - returns a string
    sample_adjective = sample(adjective,1)[0]
    print(sample_adjective)
    sample_noun1 = sample(noun1,1)[0]
    print(sample_noun1)
    sample_noun2 = sample(noun2,1)[0]
    print(sample_noun2)
    return (f"{sample_adjective} {sample_noun1} of {sample_noun2}")



# Main block