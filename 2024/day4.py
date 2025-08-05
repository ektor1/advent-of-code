
# Part One
def dfs(grid: list[str], r: int, c: int, curr_path: str, r_incr: int, c_incr: int) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    target_word = 'XMAS'

    if curr_path == target_word:
        return 1

    if (min(r, c) < 0 or r == ROWS or c == COLS or curr_path not in target_word):
        return 0

    curr_path += grid[r][c]
    if dfs(grid, r + r_incr, c + c_incr, curr_path, r_incr, c_incr):
        return 1
    return 0

def solution(grid: list[str]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    
    xmas_count = 0
    curr_path = ''
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "X":
                for dr, dc in directions:
                    xmas_count += dfs(grid, r, c, curr_path, dr, dc)
    
    return xmas_count


# Part Two
def solution(grid: list[str]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])

    xmas_count = 0
    target_map = {"S": 1, "M": 1}
    directions1 = [[-1, -1], [1, 1]]
    directions2 = [[-1, 1], [1, -1]]

    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            if grid[r][c] == "A":
                dir1 = {"M": 0, "S": 0}
                dir2 = {"M": 0, "S": 0}

                for dr, dc in directions1:
                    diag_letter = grid[r + dr][c + dc]
                    if diag_letter in dir1:
                        dir1[diag_letter] += 1
                for dr, dc in directions2:
                    diag_letter = grid[r + dr][c + dc]
                    if diag_letter in dir2:
                        dir2[diag_letter] += 1

                if dir1 == target_map and dir2 == target_map:
                    xmas_count += 1
    return xmas_count
