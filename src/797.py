class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        ans = []
        def dfs(root, path):
            for child in graph[root]:
                path.append(child)
                if child == n:
                    ans.append(path.copy())
                dfs(child, path)
                path.pop(-1)
                
        dfs(0, [0])
        return ans
