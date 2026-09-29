"""Behavior checks for the A* function in the published notebook."""

import json
import unittest
from pathlib import Path


NOTEBOOK = Path(__file__).resolve().parents[1] / "Code" / "Capstone_RoboNavSim_WillianeYarro_ITAI2277.ipynb"


def load_astar():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    cells = ["".join(cell["source"]) for cell in notebook["cells"] if cell["cell_type"] == "code"]
    source = next(source for source in cells if source.startswith("import heapq\n\ndef astar("))
    namespace = {}
    exec(compile(source, str(NOTEBOOK), "exec"), namespace)
    return namespace["astar"]


class AStarTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.astar = staticmethod(load_astar())

    def test_shortest_clear_route(self):
        self.assertEqual(self.astar((0, 0), (3, 3), [], 4),
                         [(0, 0), (1, 1), (2, 2), (3, 3)])

    def test_routes_around_wall_without_crossing_corners(self):
        blocked = {(1, 0), (1, 1), (1, 2)}
        path = self.astar((0, 1), (2, 1), blocked, 4)
        self.assertEqual(path[0], (0, 1))
        self.assertEqual(path[-1], (2, 1))
        self.assertEqual(len(path), 7)
        self.assertTrue(blocked.isdisjoint(path))
        for (x, y), (nx, ny) in zip(path, path[1:]):
            self.assertLessEqual(max(abs(nx - x), abs(ny - y)), 1)
            if nx != x and ny != y:
                self.assertNotIn((nx, y), blocked)
                self.assertNotIn((x, ny), blocked)

    def test_blocked_corner_is_unreachable(self):
        self.assertEqual(self.astar((0, 0), (1, 1), {(1, 0), (0, 1)}, 2), [])

    def test_invalid_endpoints_and_unreachable_goal(self):
        for start, goal, blocked in [
            ((-1, 0), (1, 1), set()),
            ((0, 0), (2, 0), set()),
            ((0, 0), (1, 1), {(0, 0)}),
            ((0, 0), (1, 1), {(1, 1)}),
        ]:
            with self.subTest(start=start, goal=goal):
                self.assertEqual(self.astar(start, goal, blocked, 2), [])

    def test_start_equals_goal(self):
        self.assertEqual(self.astar((1, 1), (1, 1), [], 3), [(1, 1)])


if __name__ == "__main__":
    unittest.main()
