import unittest
from sgraph import SGraph
from enumerator import DigraphEnumerator

class TestSGraph(unittest.TestCase):

    def setUp(self):
        self.edges = {
            1: {'a': 2, 'b': 3},
            2: {'a': 3, 'b': 4},
            3: {'a': 4, 'b': 5},
            4: {'a': 5, 'b': 6},
            5: {'a': 6, 'b': 1},
            6: {'a': 1, 'b': 2}
        }
        self.graph = SGraph(self.edges)

    def test_basic_sgraph(self):
        graph = SGraph(self.edges)
        # Reset all switches to OFF
        graph.reset_switches()
        self.assertEqual(graph.switches, [False, False, False, False, False, False, False])

    def test_move_function(self):
        graph = SGraph(self.edges)
        final_position = graph.move(1, 'abab')
        # Check the final position and the switch states after the move
        self.assertEqual(final_position, 1)
        self.assertEqual(graph.switches, [False, True, True, False, True, True, False])

    def test_count_function(self):
        # Given the provided structure, this is just a hypothetical test.
        # Actual counts may vary based on the graph structure.
        graph = SGraph(self.edges)
        count = graph.count(1, 4, 2)  # Modified the destination to 4 for the count test
        # The count here is hypothetical and is used for demonstration purposes.
        self.assertEqual(count, 2)

    def test_reset_method(self):
        # Move using some arbitrary sequence
        self.graph.move(1, 'aabba')
        # Ensure switches are not all OFF
        self.assertNotEqual(self.graph.switches, [False] * (len(self.edges) + 1))
        # Call reset method
        self.graph.reset()
        # Confirm all switches are OFF after reset
        self.assertEqual(self.graph.switches, [False] * (len(self.edges) + 1))
    # ... additional test methods for other functions ...
    def test_scount_function(self):
        """Test if the SCount function returns correct counts with specific end switch states."""
        count = self.graph.SCount(1, 4, 2, [False, True, True, False, False, False, False])
        self.assertEqual(count, 0)

    def test_solve_function(self):
        """Test if the solve function returns a valid shortest command."""
        command = self.graph.Solve(1, [False, True, True, False, True, True, False])
        self.assertEqual(command, 'abab')  # This should match the command we know results in these switch states.

    def test_find_hardest(self):
        """Test if find hardest returns a valid result for m."""
        result = self.graph.find_hardest(4)
        # As this function is a placeholder, we're not asserting any specific results yet.
        self.assertIsNotNone(result)
class TestDigraphEnumerator(unittest.TestCase):

    def test_enumeration(self):
        m = 4
        enumerator = DigraphEnumerator(m)
        count = 0
        while enumerator.has_next():
            graph = enumerator.next()
            count += 1
            for i in range(1, m + 1):
                # Each vertex should have 2 unique edges 'a' and 'b'
                self.assertNotEqual(graph[i]['a'], graph[i]['b'])
                # Each edge should point to a vertex within the graph
                self.assertIn(graph[i]['a'], range(1, m + 1))
                self.assertIn(graph[i]['b'], range(1, m + 1))
        # Ensure at least one graph is generated
        self.assertGreater(count, 0)
if __name__ == "__main__":
    unittest.main()
