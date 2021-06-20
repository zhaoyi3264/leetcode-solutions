class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        m = len(board)
        n = len(board[0])
        
        def isValid(i,j):
            nonlocal m,n
            return 0 <= i < m and 0 <= j < n
        
        def neighbours(i,j):
            directions = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]
            return [(i+p,j+q) for p,q in directions if isValid(p+i,j+q)]
        
        def f(i,j,vis):
            vis.add((i,j))
            neighs = neighbours(i,j)
            
            minecount = 0
            for n in neighs:
                if board[n[0]][n[1]] == 'M':
                    minecount+=1
            
            if not minecount:
                board[i][j] = 'B'
                for n in neighs:
                    if board[n[0]][n[1]] == 'E' and n not in vis:
                        f(n[0],n[1],vis)
            else:
                board[i][j] = str(minecount)
        
        
        f(click[0],click[1],set())
        return board
