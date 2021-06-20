class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not len(rooms[0]):
            return len(rooms) < 2
        visited = {0}
        
        def dfs(root):
            ans = False
            for child in rooms[root]:
                if child not in visited:
                    visited.add(child)
                    if len(visited) == len(rooms):
                        return True
                    ans = ans or dfs(child)
            return ans
        return dfs(0)
