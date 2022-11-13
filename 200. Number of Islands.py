class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        visited = dict()
        
        def DFS(i, j):
            adj = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
            
            for k, l in adj:
                if k < 0 or l < 0 or k>= m or l >= n or visited.get((k, l)):
                    continue
                visited[(k, l)] = True
                if grid[k][l] == '1':
                    DFS(k, l)
        
        for i in range(m):
            for j in range(n):
                if not visited.get((i, j)):
                    visited[(i, j)] = True
                    if grid[i][j] == '1':
                        DFS(i, j)
                        islands += 1
        return islands
                        
                    
                    
                    
                    
                
            
        