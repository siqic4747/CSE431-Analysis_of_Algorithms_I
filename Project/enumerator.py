class DigraphEnumerator:
    def __init__(self, m):
        self.m = m
        self.done = False
        self.current = self._generate_initial()

    def set_current(self, current):
        self.current = current

    def has_next(self):
        return not self.done

    def next(self):
        if self.done:
            return None
        last_graph = self.current.copy()
        self.current = self._step_to_next(self.current)
        if last_graph == self.current:
            self.done = True
        return self.current

    def _generate_initial(self):
        # Return an initial graph based on m value
        return {i: {'a': (i + 1) % self.m + 1, 'b': (i + 2) % self.m + 1} for i in range(1, self.m + 1)}

    def _step_to_next(self, current):
        new_graph = current.copy()
        for i in range(1, self.m + 1):
            new_graph[i]['b'] = (new_graph[i]['b']) % self.m + 1
        return new_graph
