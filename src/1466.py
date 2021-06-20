class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(set)
        e = set()
        for src, dst in connections:
            g[src].add(dst)
            g[dst].add(src)
            e.add((src, dst))
        count = 0
        visited = set()
        def dfs(root):
            nonlocal count
            visited.add(root)
            for child in g[root]:
                if child in visited:
                    continue
                if (root, child) in e:
                    count += 1
                dfs(child)
        dfs(0)
        return count
