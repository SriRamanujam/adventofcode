#!/usr/bin/env python3

## Uncomment all the print statements for debug output

from string import ascii_lowercase
from collections import defaultdict

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.completion_time = 60 + 1 + ascii_lowercase.index(self.name.lower())

    def addEdge(self, node):
        self.edges.append(node)
        self.edges.sort(key=lambda x: x.name)


def dep_resolve(node, resolved):
    for edge in node.edges:
        if edge.name not in resolved:
            dep_resolve(edge, resolved)
    resolved.append(node.name)


if __name__ == '__main__':
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]

    nodes = {}

    for line in lines:
        parts = line.split()
        first = parts[1]
        second = parts[7]

        if first not in nodes:
            nodes[first] = Node(first)

        if second not in nodes:
            nodes[second] = Node(second)

        nodes[second].addEdge(nodes[first])

    resolved = []
    assigned = []
    time_taken = 0
    workers = [{'name': '', 'time': -1} for i in range(5)] # five workers

    while True:
        #print("Elapsed time: {} seconds".format(time_taken), end=',')

        # first things first, decrement and resolve all tasks
        for idx in range(len(workers)):
            workers[idx]['time'] -= 1
            if workers[idx]['time'] < 1:
                if workers[idx]['name'] != '':
                    # this is a resolved task, do the busywork and then reset
                    # the worker
                    task_name = workers[idx]['name']
                    #print("Resolving task {}".format(task_name), end=',')
                    finished_task = nodes[task_name]
                    dep_resolve(nodes[task_name], resolved)
                    assigned.remove(task_name)
                    workers[idx]['name'] = ''
                    workers[idx]['time'] = -1

        to_process = []
        resolve_set = set([x for x in resolved])
        for k, v in nodes.items():
            if k not in resolved:
                if len([x for x in v.edges if x.name not in resolve_set]) == 0:
                    to_process.append(k)

        if len(to_process) == 0:
            #print()
            break

        # to_process represents the total set of all workable tasks at the current
        # time, including tasks that may already be in progress. we only want to
        # go further with the subset of workable tasks that are neither assigned
        # nor resolved.

        queued_tasks = [x for x in to_process if x not in resolved + assigned]
        queued_tasks.sort()
        #print("queued_tasks: {}".format(queued_tasks), end=',')
        #print("assigned: {}".format(assigned), end=',')

        # try to assign queued tasks to an idle worker
        for idx in range(len(workers)):
            if workers[idx]['name'] == '': # idle worker
                try:
                    new_task = nodes[queued_tasks.pop(0)]
                except IndexError: # no more queued tasks:
                    break
                workers[idx]['name'] = new_task.name
                workers[idx]['time'] = new_task.completion_time
                assigned.append(new_task.name)

        time_taken += 1
        #print("workers: {}".format(workers))


    print("PART 2 ORDER: {}".format(''.join(resolved)))
    print("PART 2 ANSWER: {} seconds".format(time_taken))
