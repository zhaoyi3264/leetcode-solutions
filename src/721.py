class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_user = {}
        for account in accounts:
            acc = account[0]
            for email in account[1:]:
                email_to_user[email] = acc
                graph[email].add(account[1])
                graph[account[1]].add(email)
        
        ans = []
        visited = set()
        
        def dfs(email):
            if email in visited:
                return []
            visited.add(email)
            res = [email]
            for e in graph[email]:
                res.extend(dfs(e))
            return res
        
        for email in graph:
            if email not in visited:
                res = sorted(dfs(email))
                res.insert(0, email_to_user[email])
                ans.append(res)
        return ans
