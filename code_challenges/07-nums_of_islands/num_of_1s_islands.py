# Problem: https://leetcode.com/problems/number-of-islands/

_WATER = "0"
_LAND = "1"


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Return the amount of islands in a grid
        """
        if len(grid) == 0:
            return 0

        """
        Sort of Deepth Traversal
        directions: Up, Down, Right, Left
        1. Check currPos(i,j) and look up for adjacent neightbors
        1.1. If currPos == '1':
        1.2. If j-1 >= 0 and j-1 <= len(grid) and Up(i,j-1) == '1': add it to Stack
        2. X
        currPos => Stack of neighbors  | Hash Map (Python Set) seen
        (0,0)   => [(1,0),(0,1)]       | []
        (0,1)   => [(1,0),(1,1),(0,2)] | [(0,0)]
        (0,2)   => [(1,0),(1,1),(0,3)] | [(0,0),(0,1)]
        (0,3)   => [(1,0),(1,1),(1,3)] | [(0,0),(0,1),(0,2)]
        (1,3)   => [(1,0),(1,1)]       | [(0,0),(0,1),(0,2),(0,3)]
        (1,1)   => [(1,0),(2,1)]       | [(0,0),(0,1),(0,2),(0,3),(1,3)]
        (2,1)   => [(1,0),(2,0)]       | [(0,0),(0,1),(0,2),(0,3),(1,3),(1,1)]
        (2,0)   => [(1,0)]             | [(0,0),(0,1),(0,2),(0,3),(1,3),(1,1),(2,1)]
        (1,0)   => []                  | [(0,0),(0,1),(0,2),(0,3),(1,3),(1,1),(2,1),(2,0)]
        ()      => []                  | [(0,0),(0,1),(0,2),(0,3),(1,3),(1,1),(2,1),(2,0),(1,0)]
        """
        number_of_islands = 0
        seen_coords = set()
        iPtr, jPtr = self.getNextStartPoint(
            grid, 0, 0, seen_coords
        )  # Coords (0,0) used as pivot/starting-point
        stack_of_neighbors = [(iPtr, jPtr)]

        while (
            len(stack_of_neighbors) > 0 and iPtr < len(grid) and jPtr < len(grid[iPtr])
        ):
            currPos = stack_of_neighbors.pop()
            rowPtr, colPtr = currPos
            stack_of_neighbors.extend(
                self.getAdjacentNeighbors(grid, rowPtr, colPtr, seen_coords)
            )
            seen_coords.add((rowPtr, colPtr))
            # print(currPos, stack_of_neighbors, seen_coords)
            if len(stack_of_neighbors) == 0:
                number_of_islands += 1
                iPtr, jPtr = self.getNextStartPoint(grid, iPtr, jPtr, seen_coords)
                stack_of_neighbors = [(iPtr, jPtr)]
            # print(f'iPtr: {iPtr} | jPtr: {jPtr}')

        return number_of_islands

    def getAdjacentNeighbors(
        self,
        grid: List[List[str]],
        rowPtr: int,
        colPtr: int,
        seen_coords: List[Tuple[int, int]],
    ) -> List[int]:
        neighbors = []
        if grid[rowPtr][colPtr] == _WATER:
            return neighbors

        up = rowPtr - 1
        down = rowPtr + 1
        right = colPtr + 1
        left = colPtr - 1

        if up >= 0 and (up, colPtr) not in seen_coords:
            neighbors.append((up, colPtr))

        if down < len(grid) and (down, colPtr) not in seen_coords:
            neighbors.append((down, colPtr))

        if right < len(grid[rowPtr]) and (rowPtr, right) not in seen_coords:
            neighbors.append((rowPtr, right))

        if left >= 0 and (rowPtr, left) not in seen_coords:
            neighbors.append((rowPtr, left))

        return neighbors

    def getNextStartPoint(
        self, grid: List[List[str]], i: int, j: int, seen_coords: List[Tuple[int, int]]
    ) -> Tuple[int, int]:
        targetRowPtr, targetColPtr = i, j
        currCoord = grid[targetRowPtr][targetColPtr]
        # print(f'i: {i} | j: {j} | currCoord: {currCoord}')
        while currCoord == _WATER or (targetRowPtr, targetColPtr) in seen_coords:
            targetColPtr += 1
            if targetColPtr >= len(grid[targetRowPtr]):
                targetRowPtr += 1
                targetColPtr = 0
            if targetRowPtr >= len(grid):
                break
            currCoord = grid[targetRowPtr][targetColPtr]
        # print(f'targetRowPtr: {targetRowPtr} | targetColPtr: {targetColPtr}')
        return targetRowPtr, targetColPtr
