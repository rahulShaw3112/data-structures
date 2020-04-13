# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        return self.cloneG(node, visited)
    
    def cloneG(self, root, visited):
        if(not root):
            return None
        if(root.val in visited):
            return visited[root.val]
        
        temp = Node(root.val)
        visited[temp.val] = temp 
        
        for n in root.neighbors:
            temp.neighbors.append(self.cloneG(n, visited))
            
        return temp