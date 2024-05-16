from subprocess import check_output, TimeoutExpired
import os


def parse_tuple(test_case, line_number, str_tuple):
    x, y = str_tuple.strip("()\n ").split(",")
    try:
        return int(x), int(y)
    except Exception as e:
        test_case.fail(
            f"Impossible de lire la ligne #{line_number}: {str_tuple}. Le format attendu est un tuple (x, y) avec x et y des entiers. Erreur: {e}")


def __foobar(file_in):
    with open(file_in, 'r') as f:
        lines = f.readlines()
        maze = [[True] * len(lines) for i in range(len(lines[0].strip("\n")))]
        start = None
        end = None
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip("\n")):
                maze[x][y] = char != "#"
                if char == "s":
                    start = (x, y)
                elif char == "e":
                    end = (x, y)

        return maze, start, end


def validate(test_case, module, file_in, file_out, timeout=1, path_length=None):
    try:
        check_output(["python", module,
                     file_in, file_out], timeout=timeout)
    except TimeoutExpired:
        test_case.fail(
            f"Trop long: la résolution doit se faire en moins de {timeout} secondes.")
    except:
        test_case.fail(
            f"L'algorithme de résolution a renvoyé une erreur sur le fichier {file_in}")
    test_case.assertTrue(os.path.isfile(file_out),
                         "Le fichier de sortie n'existe pas")
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    with open(file_out, 'r') as f:
        maze, start, end = __foobar(file_in)
        width = len(maze)
        height = len(maze[0])
        lines = [parse_tuple(test_case, line_number, tup)
                 for line_number, tup in enumerate(f)]
        test_case.assertEqual(
            start, lines[0], f"Mauvaise valeur pour START. Atttendu {start=}, dans le fichier={lines[0]}")
        test_case.assertEqual(
            end, lines[-1], f"Mauvaise valeur pour END. Atttendu {end=}, dans le fichier={lines[-1]}")
        if path_length:
          test_case.assertLessEqual(len(lines), path_length, f"Chemin non-optimal: le plus court chemin fait {path_length} positions. Dans le fichier il y a {len(lines)} positions.")
        xprev, yprev = start
        for line_number, line in enumerate(lines[1:], start=1):
            x, y = line
            test_case.assertGreaterEqual(x, 0, f"Mauvaise position, ligne #{line_number}. x < 0")
            test_case.assertLess(x, width, f"Mauvaise position, ligne #{line_number}. x >= largeur ({width})")
            test_case.assertGreaterEqual(y, 0, f"Mauvaise position, ligne #{line_number}. y < 0")
            test_case.assertLess(y, height, f"Mauvaise position, ligne #{line_number}. y >= hauteur ({height})")
            test_case.assertTrue(
                maze[x][y], f"Mauvaise position, ligne #{line_number} - mur du labyrinthe")
            movement = x - xprev, y - yprev
            test_case.assertIn(container=directions,
                               member=movement, msg=f"Mouvement non autorisé, ligne #{line_number}: {xprev, yprev} -> {x, y}")
            xprev, yprev = x, y
