# Initialisation

    # Import functions from libraries
from os import chdir, path
from random import sample

    # Set Working directory to file directory

chdir(path.dirname(__file__))

    # import data from .txt into arrays, example layout:
    # var_name = (open("txt_file_name.txt","r").readlines())[0].split(","))

adjective = (open("weapon_adjectives.txt", "r").readlines())[0].split(",")
noun1 = (open("weapon_nouns1.txt", "r").readlines())[0].split(",")
noun2 = (open("weapon_nouns2.txt", "r").readlines())[0].split(",")

# Functions

def gen_weapon(): # Simple Weapon Generator (adjective noun of noun2)
    sample_adjective = sample(adjective,1)[0]
    print(sample_adjective)
    sample_noun1 = sample(noun1,1)[0]
    print(sample_noun1)
    sample_noun2 = sample(noun2,1)[0]
    print(sample_noun2)
    return (f"{sample_adjective} {sample_noun1} of {sample_noun2}")



# Main block

# Hi Chris