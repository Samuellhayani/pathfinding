

import numpy as np
import matplotlib.pyplot as plt
from maze import *


def repr(filename) :
    with open(filename) as f :
        M = []
        i = 0
        for line in f :
            i += 1
            M.append([])
            for char in line.strip('\n') :
                if char == '#' :
                    M[i-1].append((0,0,0))
                if char == ' ' :
                    M[i-1].append((255,255,255))
                if char == 's' :
                    M[i-1].append((255,0,0))
                if char == 'e' :
                    M[i-1].append((0,255,0))
    return M


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('maze_file', help = 'name of the file containing the maze you want to solve', type = str)
    args = parser.parse_args()
    maze_file = sys.argv[1]
    s, e = find_s_and_e(maze_file)
    Labyrinthe = repr(maze_file)
    chemin = lee(maze_file, s, e)
    for coord in chemin[1:-1] :
        Labyrinthe[coord[1]][coord[0]] = (0,0,255)
    plt.imshow((Labyrinthe))
    plt.title(maze_file)
    plt.show()





