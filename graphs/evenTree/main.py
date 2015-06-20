# https://www.hackerrank.com/challenges/even-tree

import sets

nodes, edges = map(int, raw_input().split(" "))

neighbors = {i:set() for i in range(1,nodes+1)}
weight = {i:0 for i in range(1, nodes+1)}
for i in range(edges):
    u, v = map(int, raw_input().split(" "))
    neighbors[u].add(v)
    neighbors[v].add(u)
    
removable = [0]
def weighNode(node, parent):
    children = neighbors[node]
    children.discard(parent)
    totalWeight = 1
    for child in children:
        childWeight = weighNode(child, node)
        if childWeight % 2 == 0:
            removable[0] += 1
        totalWeight += childWeight
    return totalWeight

weighNode(1, None)
print removable[0]


