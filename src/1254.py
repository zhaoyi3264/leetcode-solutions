class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        island_count = 0
        for irow in range(len(grid)):
            for icol in range(len(grid[0])):
                island_count += (not grid[irow][icol]) and is_closed(irow, icol, grid)
                
        return island_count
                
                
def is_closed(irow, icol, grid):
    if not (0 <= irow < len(grid) and 0 <= icol < len(grid[0])):
        return False
    if grid[irow][icol]:
        return True
    grid[irow][icol] = 1
    is_up_closed = is_closed(irow - 1, icol, grid)
    is_down_closed = is_closed(irow + 1, icol, grid)
    is_left_closed = is_closed(irow, icol - 1, grid)
    is_right_closed = is_closed(irow, icol + 1, grid)
    return is_up_closed and is_down_closed and is_left_closed and is_right_closed
