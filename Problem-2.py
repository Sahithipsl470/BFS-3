# Time Complexity : O(V + E)  # Visit each node and edge once
# Space Complexity : O(V)     # Hashmap storing cloned nodes
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Explanation:
# Use DFS to traverse the graph and clone nodes.
# Maintain a hashmap to avoid cloning the same node twice.
# Recursively clone neighbors and attach them to the copied node.

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        visited = {}
        
        def dfs(curr):
            if curr in visited:
                return visited[curr]
            
            copy = Node(curr.val)
            visited[curr] = copy
            
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node)