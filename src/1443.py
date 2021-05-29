class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(set)
        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)
        
        def dfs(root, p):
            nonlocal tree
            nonlocal hasApple
            
            a = hasApple[root]
            t = 0
            
            for c in tree[root]:
                if c == p:
                    continue
                c_a, c_t = dfs(c, root)
                if c_a:
                    a = True
                    t += 2 + c_t
            return a, t
        
        return dfs(0, None)[1]
