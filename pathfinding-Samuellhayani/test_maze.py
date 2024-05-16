import unittest
from tempfile import TemporaryDirectory
from shutil import copyfile
from pathlib import Path
import os
from test_utils import __foobar, validate


class TestMaze(unittest.TestCase):

    def setUp(self):
        self.test_dir = TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)
        self.output_path = self.test_path / "output"
        source = Path(".github", "data")
        for file in os.listdir(source):
            copyfile(source / file, self.test_path / file)
        os.mkdir(self.output_path)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_maze_example(self):
        self.__validate(
            "perfect-example.txt",
            "perfect-example-output.txt"
        )

    def test_maze_example_reversed(self):
        self.__validate(
            "perfect-example-reversed.txt",
            "perfect-example-reversed-output.txt"
        )

    def test_maze_small(self):
        self.__validate(
            "perfect-small.txt",
            "perfect-small-output.txt"
        )

    def test_maze_small_middle(self):
        self.__validate(
            "perfect-small-middle.txt",
            "perfect-small-middle-output.txt"
        )

    def test_maze_rectangle(self):
        self.__validate(
            "perfect-rectangle.txt",
            "perfect-rectangle-output.txt"
        )

    def test_maze_big(self):
        self.__validate(
            "perfect-big.txt",
            "perfect-big-output.txt"
        )

    def test_shortest_path(self):
        self.__validate(
            "perfect-big.txt",
            "perfect-big-output.txt",
            path_length=1583
        )

    def test_maze_huge(self):
        self.__validate(
            "perfect-huge.txt",
            "perfect-huge-output.txt",
            timeout=5
        )

    def __validate(self, file_in, file_out, timeout=3, path_length=None):
        validate(self, "maze.py", self.test_path / file_in,
                 self.output_path / file_out, timeout, path_length)


if __name__ == "__main__":
    unittest.main()
