# Initialisation

    # Import
from os import chdir, path
from random import sample

    # Set Working directory

chdir(path.dirname(__file__))

    # import data from .txt into arrays
    # var_name = (open("txt_file_name.txt","r").readlines())[0].split(","))

adjective = (open("weapon_adjectives.txt", "r").readlines())[0].split(",")
noun1 = (open("weapon_nouns1.txt", "r").readlines())[0].split(",")
noun2 = (open("weapon_nouns2.txt", "r").readlines())[0].split(",")

# Functions

# Main block

