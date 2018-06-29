import resource
import time
from node import Node, child_node
from queue import Queue
from stack import Stack
from priority_queue import PriorityQueue

def search(problem, frontier):
    running_time = time.time()
    node = Node(problem.initial_state, h_cost=problem.heuristic(problem.initial_state))
    if problem.goal_test(node.state):
        return node.state
    frontier.add(node)
    explored = set(node.state)
    nodes_expanded = 0
    max_search_depth = 0
    while frontier.entries:
        node = frontier.remove()
        if problem.goal_test(node.state):
            write_to_result_file(node, nodes_expanded, max_search_depth,
                                 time.time() - running_time,
                                 resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return node.state
        explored.add(node.state)
        nodes_expanded += 1
        actions = problem.actions(node.state)
        children = []
        for action in actions:
            child = child_node(problem, node, action)
            if child.state not in explored and child not in frontier:
                children.append(child)
                if child.g_cost > max_search_depth:
                    max_search_depth = child.g_cost
        if children:
            frontier.extend(children)
    return "Failed"

def bfs(problem):
    return search(problem, Queue())

def dfs(problem):
    return search(problem, Stack())

def ast(problem):
    return search(problem, PriorityQueue(key=lambda x: x.f_cost))

def write_to_result_file(node, nodes_expanded, max_search_depth, running_time, max_ram_usage):
    output_file = open("output.txt", "w+")
    path_to_goal = []
    while node:
        if node.action:
            path_to_goal.append(node.action)
        node = node.parent
    output_file.write("path_to_goal: %s\n" % path_to_goal[::-1])
    output_file.write("cost_of_path: %s\n" % len(path_to_goal))
    output_file.write("nodes_expanded: %s\n" % nodes_expanded)
    output_file.write("search_depth: %s\n" % len(path_to_goal))
    output_file.write("max_search_depth: %s\n" % max_search_depth)
    output_file.write("running_time: %s\n" % running_time)
    output_file.write("max_ram_usage: %s\n" % max_ram_usage)
    output_file.close()
    return
