import sys
import argparse

# votre code ici

def lab_mat(filename) : #matrice avec 0 si mur et 1 si passage
    with open(filename) as f :
        M = []
        i = 0
        for line in f :
            i += 1
            M.append([])
            for char in line.strip('\n') :
                if char == '#' :
                    M[i-1].append(0)
                else :
                    M[i-1].append(1)
    return M

def mat_dim(M) : 
    dim_x = len(M)
    dim_y = len(M[0])
    return dim_x, dim_y



def find_s_and_e(filename) : #pour trouver l'entrée et la sortie
    with open(filename) as f :
        s = (0,0)
        e = (0,0)
        M = []
        i = 0
        for line in f :
            i += 1
            M.append([])
            for char in line.strip('\n') :
                    M[i-1].append(char)
    for j, _ in enumerate(M) :
        for k, _ in enumerate(M[j]) :
            if M[j][k] == 's' :
                s = (k,j)
            elif M[j][k] == 'e' :
                e = (k,j)
    return s, e



from collections import deque
def lee(filename, s, e) : #algorithme de Lee, renvoie le chemin et non la chaine de caractère
    s = (s[1],s[0])
    e = (e[1], e[0])
    M_lab = lab_mat(filename)
    dim_x, dim_y = mat_dim(M_lab)
    mur = 0
    visited = [[False for y in range(dim_y)] for x in range(dim_x)]
    to_visit = deque()
    to_visit.append((s[0], s[1], 0))
    predecesseur = {s:[s]}
    (current_x, current_y) = s
    while len(to_visit)>0 :
        (current_x, current_y, dist) = to_visit.popleft()
        current_pos = (current_x, current_y)
        if current_pos == e :
            break
        neighbors = [
            (current_x-1, current_y), 
            (current_x+1, current_y), 
            (current_x, current_y-1), 
            (current_x, current_y+1)
        ]

        for neighbor in neighbors:
            neighbor_x, neighbor_y = neighbor
        
            if (0 <= neighbor_x < dim_x) and (0 <= neighbor_y < dim_y) :
                # si ce voisin est bien un espace libre non deja visité
                if M_lab[neighbor_x][neighbor_y] != mur :
                    if visited[neighbor_x][neighbor_y] == False :
                        visited[neighbor_x][neighbor_y] = True
                        to_visit.append((neighbor_x, neighbor_y, dist + 1))
                        predecesseur[neighbor] = predecesseur[current_pos] + [current_pos]
    depart, arrivee = s, e                
    chemin = predecesseur[arrivee]
    chemin.append(arrivee)
    chemin = [(t[1],t[0]) for t in chemin]
    path = chemin[1:]
    return path


def print_lee(filename, s, e) :
    path = lee(filename, s, e)
    gps = ''
    for position in path :
        gps += str(position) + '\n'
    
    return gps



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








    
