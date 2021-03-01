"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# dfs


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        return self.dfs(node, {})

    def dfs(self, node, cloned_nodes):
        if node in cloned_nodes:
            return cloned_nodes[node]

        clone_node = Node(node.val)
        cloned_nodes[node] = clone_node
        clone_node.neighbors = [self.dfs(node, cloned_nodes) for node in node.neighbors]

        return clone_node

        # val = node.val
        # if val in cloned_nodes:
        #     return cloned_nodes[val]

        # clone_node = Node(val)
        # cloned_nodes[val] = clone_node
        # for n in node.neighbors:
        #     clone_neighbor = self.dfs(n, cloned_nodes)
        #     clone_node.neighbors.append(clone_neighbor)

        # return clone_node
