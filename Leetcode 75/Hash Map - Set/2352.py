class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = {}
        
        # Count each row's occurrence
        for row in grid:
            row_str = ' '.join(map(str, row))
            if row_str in row_counts:
                row_counts[row_str] += 1
            else:
                row_counts[row_str] = 1
        
        count = 0
        # Count occurrences of each column in the row_counts
        for i in range(len(grid)):
            col_str = ' '.join(str(grid[j][i]) for j in range(len(grid)))
            count += row_counts.get(col_str, 0)

        return count