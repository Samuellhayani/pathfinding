import unittest
from tempfile import TemporaryDirectory
from shutil import copyfile
from pathlib import Path
import os
from test_utils import validate


class TestPathfinding(unittest.TestCase):

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

    def test_pathfinding_example(self):
        self.__validate(
            "pathfinding-example.txt",
            "pathfinding-example-output.txt"
        )

    def test_pathfinding_medium(self):
        self.__validate(
            "pathfinding-medium.txt",
            "pathfinding-medium-output.txt"
        )

    def test_pathfinding_huge(self):
        self.__validate(
            "pathfinding-huge.txt",
            "pathfinding-huge-output.txt"
        )


    def test_maze_big(self):
        self.__validate(
            "perfect-big.txt",
            "perfect-big-output.txt"
        )


    def __validate(self, file_in, file_out, timeout=3):
                validate(self, "pathfinding.py", self.test_path / file_in,
                 self.output_path / file_out, timeout)

if __name__ == "__main__":
    unittest.main()
