#!/usr/bin/env python3

## Uncomment all the print statements for debug output

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def addEdge(self, node):
        self.edges.append(node)
        self.edges.sort(key=lambda x: x.name)

def dep_resolve(node, resolved):
    for edge in node.edges:
        if edge not in resolved:
            dep_resolve(edge, resolved)
    resolved.append(node)


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


    # the algorithm will be:
    # loop through all the nodes and find the ones with 0 dependencies (len(edges) is 0)
    # sort those names alphabetically, and dep_resolve the first one
    # dep_resolve should add all resolvable letters to a list as it traverses
    # repeat until we're out of unresolved letters

    resolved = []
    while True:
        to_process = []
        resolve_set = set([x.name for x in resolved])
        for k,v in nodes.items():
            if v not in resolved:
                if len([x for x in v.edges if x.name not in resolve_set]) == 0:
                    to_process.append(k)

        to_process.sort()
        if len(to_process) == 0:
            break
        #print(to_process)
        node_name = to_process[0]
        if node_name not in resolved:
            dep_resolve(nodes[node_name], resolved)
    print("PART 1 ANSWER: {}".format(''.join([x.name for x in resolved])))
