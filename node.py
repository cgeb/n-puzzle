class Node:
    def __init__(self, state, parent=None, action=None, g_cost=0, h_cost=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.g_cost = g_cost
        self.h_cost = h_cost
        if self.h_cost:
            self.f_cost = g_cost + h_cost
        else:
            self.f_cost = g_cost

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplementedError
        #if self.h_cost:
        #    return self.state == other.state and self.f_cost == other.f_cost
        return self.state == other.state

    def __hash__(self):
        #if self.h_cost:
        #    return hash((self.state, self.f_cost))
        return hash(self.state)

    def __iter__(self):
        return self

    def __next__(self):
        if self.parent:
            return self.parent
        else:
            raise StopIteration

def child_node(problem, parent, action):
    state = problem.result(parent.state, action)
    g_cost = parent.g_cost + problem.step_cost(parent.state, action)
    h_cost = problem.heuristic(state)
    return Node(state, parent=parent, action=action, g_cost=g_cost, h_cost=h_cost)
