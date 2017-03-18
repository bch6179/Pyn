0] + [1,2,3,4,5,6,7,8] = [0,1,2,3,4,5,6,7,8]
[1,2,3,4,5,6,7,8] + [0] = [1,2,3,4,5,6,7,8,0]

basically, operator.ne compares 1 with 0 and 2, and compares 2 with 1 and 3...... It compares every element with its two neighbors.

ince there are no lakes, every pair of neighbour cells with different values is part of the perimeter (more precisely, the edge between them is). So just count the differing pairs, both horizontally and vertically (for the latter I simply transpose the grid).

def islandPerimeter(self, grid):
    return sum(sum(
        map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))


               public int islandPerimeter(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int result = 0;
        for (int[] aGrid : grid) {
            if (aGrid[0] == 1) {
                result++;
            }
            for (int i = 1; i < n; i++) {
                if (aGrid[i - 1] != aGrid[i]) {
                    result++;
                }
            }
            if (aGrid[n - 1] == 1) {
                result++;
            }
        }
        for (int j = 0; j < n; j++) {
            if (grid[0][j] == 1) {
                result++;
            }
            for (int i = 1; i < m; i++) {
                if (grid[i - 1][j] != grid[i][j]) {
                    result++;
                }
            }
            if (grid[m - 1][j] == 1) {
                result++;
            }
        }
        return result;
    }
3 months ago reply quote 
0

First, for row in... is list comprehension, where row is a row or column of the map. Second, the + map(list, zip(*grid))) is appending the transposition of the map, so columns become rows. The resulting extended grid looks like

[0, 1, 0, 0]
[1, 1, 1, 0]
[0, 1, 0, 0]
[1, 1, 0, 0]
[0, 1, 0, 1]
[1, 1, 1, 1]
[0, 1, 0, 0]
[0, 0, 0, 0]
.

public static int islandPerimeter(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        int result = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    result += 4;
                    if (i > 0 && grid[i-1][j] == 1) result -= 2;
                    if (j > 0 && grid[i][j-1] == 1) result -= 2;
                }
            }
        }
        return result;
    }
    def islandPerimeter(self, grid):
        def water_around(y, x):
        return ((x == 0              or grid[y][x-1] == 0) +
                (x == len(grid[0])-1 or grid[y][x+1] == 0) +
                (y == 0              or grid[y-1][x] == 0) +
                (y == len(grid)-1    or grid[y+1][x] == 0) )
    return sum(water_around(y, x) for y in xrange(len(grid)) for x in xrange(len(grid[0])) if grid[y][x])

    return sum(water_around(y, x) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell)
loop over the matrix and count the number of islands;
if the current dot is an island, count if it has any right neighbour or down neighbour;
the result is islands * 4 - neighbours * 2
public class Solution {
    public int islandPerimeter(int[][] grid) {
        int islands = 0, neighbours = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    islands++; // count islands
                    if (i < grid.length - 1 && grid[i + 1][j] == 1) neighbours++; // count down neighbours
                    if (j < grid[i].length - 1 && grid[i][j + 1] == 1) neighbours++; // count right neighbours
                }
            }
        }

        return islands * 4 - neighbours * 2;
    }
}
4 months ago reply quote 
descriptions of this problem implies there may be an "pattern" in calculating the perimeter of the islands.
and the pattern is islands * 4 - neighbours * 2, since every adjacent islands made two sides disappeared(as picture below).
the next problem is: how to find the neighbours without missing or recounting? i was inspired by the problem: https://leetcode.com/problems/battleships-in-a-board/
+--+     +--+                   +--+--+
|  |  +  |  |          ->       |     |
+--+     +--+                   +--+--+

public int islandPerimeter(int[][] grid) {
    if(grid.length == 0) return 0;
    for(int i = 0; i < grid.length; i++){
      for(int j = 0; j < grid[0].length; j++){
        if(grid[i][j] == 1){
          return helper(grid, i, j);
        }
      }  
    } 
    return 0;
  }
  
  private int helper(int[][] grid, int i, int j){
    grid[i][j] = -1;
    int count = 0;
    
    if(i - 1 < 0 || grid[i - 1][j] == 0) count++;
    else if(grid[i - 1][j] == 1) count += helper(grid, i - 1, j);
    
    if(i + 1 >= grid.length || grid[i + 1][j] == 0) count++;
    else if(grid[i + 1][j] == 1) count += helper(grid, i + 1, j);
    
    if(j - 1 < 0 || grid[i][j - 1] == 0) count++;
    else if(grid[i][j - 1] == 1) count += helper(grid, i, j - 1); 
    
    if(j + 1 >= grid[0].length || grid[i][j + 1] == 0) count++;
    else if(grid[i][j + 1] == 1) count += helper(grid, i, j + 1);
    
    return count;
  }

          int count = 0;
        int m = grid.length;
        if(m==0)    return 0;
        int n = grid[0].length;
        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++) {
                if(grid[i][j]==1) {
                    count += 4;
                    if(i>0 && grid[i-1][j]==1) {
                        count -= 2;
                    }
                    if(j>0 && grid[i][j-1]==1) {
                        count -= 2;
                    }
                }
            }
        }
        return count;
    }
4 months ago reply quote 
