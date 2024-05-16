from maze import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('maze_file', help = 'name of the file containing the maze you want to solve', type = str)
    parser.add_argument('solution_file', help = 'name of the file upon which you want to write the solution', type = str)
    args = parser.parse_args()
    maze_file = sys.argv[1]
    s, e = find_s_and_e(maze_file)
    solution = print_lee(maze_file, s, e)
    with open(sys.argv[2], 'w') as f:
        f.write(solution)





