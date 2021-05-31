class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1 for _ in range(n)]
        ans = [0 for _ in range(n)]
        
        def postorder(node = 0, parent = None):
            for child in graph[node]:
                if child == parent:
                    continue
                postorder(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]
                
        def inorder(node = 0, parent = None):
            for child in graph[node]:
                if child == parent:
                    continue
                ans[child] = ans[node] - count[child] + n - count[child]
                inorder(child, node)
        
        postorder()
        inorder()
        
        return ans
