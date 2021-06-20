class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        g = defaultdict(set)
        for a in allowed:
            g[a[:2]].add(a[2])
        
        def dfs(bottom):
            if len(bottom) == 2:
                return bottom in g
            old = ['']
            for i in range(1, len(bottom)):
                new = []
                base = bottom[i-1:i+1]
                if base not in g:
                    return False
                for top in g[base]:
                    for i in range(len(old)):
                        new.append(old[i] + top)
                old = new
            for b in old:
                if dfs(b):
                    return True
            return False
        return dfs(bottom)
