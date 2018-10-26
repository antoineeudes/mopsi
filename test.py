from algo import *
import unittest

def is_cycle(tab):
    seen = dict()
    for x in tab:
        seen[x]=True

    return len(seen) == len(tab)


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(100)
        self.sol = Solution(self.graph)

    def test_disturbs(self):
        sol = disturb(self.sol)
        sol2 = disturb2(self.sol)
        sol3 = disturb3(self.sol)
        sol4 = disturb4(self.sol)
        for i in range(1000):
            sol = disturb(sol)
            sol2 = disturb2(sol2)
            sol3 = disturb3(sol3)
            sol4 = disturb3(sol4)
        self.assertTrue(is_cycle(sol.path_index))
        self.assertTrue(is_cycle(sol2.path_index))
        self.assertTrue(is_cycle(sol3.path_index))
        self.assertTrue(is_cycle(sol4.path_index))

unittest.main()
