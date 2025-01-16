class Solution:
    def numIslands(self,grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_islands = 0

        def bfs(r, c):
            queue = [(r, c)]
            while queue:
                row, col = queue.pop(0)
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc
                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            queue.append((new_row, new_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    bfs(r, c)

        return num_islands

'''
Time complexity: O(n*m), or O(rows * columns), The code starts with a nested loop that iterates through each cell in the grid. It iterates through "rows" rows and "cols" columns, resulting in a time complexity of O(rows * columns). Inside the nested loop, the bfs function is called when a land cell ("1") is encountered. In the worst case, when the entire grid consists of a single island, the bfs function can potentially visit all the cells in the grid once. The BFS traversal within the bfs function involves visiting neighboring cells, but each cell is visited at most once. Therefore, the BFS traversal itself has a time complexity of O(rows * columns). 

Things to be aware of:
- Connected Components. Understand the concept of connected components. Each island represents a connected component in the graph. Ensure that your BFS traversal correctly identifies and marks the connected components.
- Neighbor Check. Ensure that the code correctly checks neighbors in all four directions (up, down, left, right) and doesn't miss any adjacent land cells. This is essential for correctly identifying islands.
- Edge Islands. Some islands might be located near the edges of the grid. Ensure that your code handles these cases correctly and doesn't produce boundary-related errors.
'''
