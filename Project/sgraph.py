class SGraph:

    def __init__(self, edges):
        self.edges = edges  # A dictionary where key is a node and value is a tuple (a-destination, b-destination).
        self.switches = [False] * (len(edges) + 1)
    def reset(self):
        """Reset all switches to OFF state."""
        self.switches = [False] * (len(self.switches))

    def move(self, initpos, input_sequence):
        position = initpos
        for label in input_sequence:
            position = self.edges[position][label]
            self.switches[position] = not self.switches[position]
            # print(f"After move {label}, position = {position}, switches = {self.switches}")
        return position

    def count(self, initpos, dest, n):
        if n == 0:
            return 1 if initpos == dest else 0

        count = 0
        for label in ('a', 'b'):
            nextpos = self.edges[initpos][label]
            count += self.count(nextpos, dest, n - 1)
        return count

    def SCount(self, initpos, dest, n, states):
        def _recursive_count(position, length, current_switches):
            if length == 0:
                return 1 if position == dest and current_switches == states else 0

            count = 0
            for label in ('a', 'b'):
                nextpos = self.edges[position][label]
                next_switches = current_switches.copy()
                next_switches[nextpos] = not next_switches[nextpos]
                count += _recursive_count(nextpos, length - 1, next_switches)
           # print(f"Position: {position}, Length: {length}, Current Switches: {current_switches}, Count: {count}")
            return count


        return _recursive_count(initpos, n, self.switches.copy())

    def Solve(self, initpos, states):

        from collections import deque

        queue = deque([(initpos, "", self.switches.copy())])
        visited = {initpos: set([tuple(self.switches)])}

        while queue:
            position, command, current_switches = queue.popleft()

            if current_switches == states:
                return command

            for label, nextpos in self.edges[position].items():
                next_switches = current_switches.copy()
                next_switches[nextpos] = not next_switches[nextpos]

                if nextpos not in visited or tuple(next_switches) not in visited[nextpos]:
                    if nextpos in visited:
                        visited[nextpos].add(tuple(next_switches))
                    else:
                        visited[nextpos] = set([tuple(next_switches)])

                    queue.append((nextpos, command + label, next_switches))
        return None

    def find_hardest(self, m):
        from enumerator import DigraphEnumerator  # Assuming the enumerator is defined in 'enumerator.py'

        enumerator = DigraphEnumerator(m)
        hardest_instance = None
        longest_command = 0

        while enumerator.has_next():
            graph = enumerator.next()
            for initpos in range(1, m + 1):
                for state_config in self._generate_switch_states(m):
                    self.switches = state_config
                    command = self.Solve(initpos, state_config)
                    if command and len(command) > longest_command:
                        longest_command = len(command)
                        hardest_instance = (graph, initpos, state_config, command)
        return hardest_instance or (None, None, None, "No hardest instance found")
    # def reset_switches(self):
    #     self.switches = [False] * (len(self.edges) + 1)

    def _generate_switch_states(self, m):
        # This will generate all possible switch states for m switches.
        for i in range(2 ** m):
            yield [False] + [bool(int(bit)) for bit in format(i, f'0{m}b')]  # Index 0 is unused.
