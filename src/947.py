class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        n = len(stones)
        graph = defaultdict(set)
        
        for i, (x, y) in enumerate(stones):
            rows[x].append(i)
            cols[y].append(i)
        
        for i, (x, y) in enumerate(stones):
            for c in rows[x] + cols[y]:
                graph[i].add(c)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return 0
            size = 1
            visited.add(i)
            for c in graph[i]:
                size += dfs(c)
            return size

        islands = []
        for i in range(n):
            if i not in visited:
                islands.append(dfs(i))
        
        return sum(islands) - len(islands)
