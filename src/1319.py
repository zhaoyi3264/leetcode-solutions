class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        g = defaultdict(set)
        for src, dst in connections:
            g[src].add(dst)
            g[dst].add(src)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in g[node]:
                dfs(nei)
        count = 0
        for node in g:
            if node not in visited:
                dfs(node)
                count += 1
        return count - 1 + n - len(visited)
