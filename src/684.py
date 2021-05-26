class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(src, dst):
            if src not in visited:
                visited.add(src)
                if src == dst:
                    return True
                return any(dfs(nei, dst) for nei in g[src])
        
        g = collections.defaultdict(set)
        for u, v in edges:
            visited = set()
            if u in g and v in g and dfs(u, v):
                return u, v
            g[u].add(v)
            g[v].add(u)
