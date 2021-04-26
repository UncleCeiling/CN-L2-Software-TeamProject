# import data from .txt file read first line only print in sorted order highest to lowest

def highscore():
    hs1 = [highscore[0]]
    hs2 = [highscore[1]]
    hs3 = [highscore[2]]
    def print_hs():
        print(f"=============HIGH SCORES============\n\n{hs1[0]}:{hs1[1]}\n\n{hs2[0]}:{hs2[1]}\n\n{hs3[0]}:{hs3[1]}")
