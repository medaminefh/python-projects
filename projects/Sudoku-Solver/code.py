# N is the size of the grid i.e., 2D matrix   N*N
N = 9

# A utility function to print grid
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()
 
# A utility function thatChecks whether it will be
# legal to assign num to the given row, col
def isSafe(grid, row, col, num):
   
    # Check if we find the same num in the similar row
    for x in range(9):
        if grid[row][x] == num:
            return False
 
    # Check if we find the same num in the similar column
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    # Check if we find the same num in the particular 3*3 matrix
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
# A utility function to Take a partially filled-in grid and attempts
# to assign values to all unassigned locations in
# such a way to meet the requirements for
# Sudoku solution (non-duplication across rows,
# columns, and boxes) */
def solveSudoku(grid, row, col):
   
    # return True if reached the end i.e., 8th row and 9th col
    if(row==N-1 and col==N):
        return True

    # if reached end of the row (i.e., col==9) then set col to 0 and increment row by 1
    if col==N:
        row+=1
        col=0

    # Check if the current position is already filled, we iterate for the next col
    if grid[row][col]>0:
        return solveSudoku(grid,row,col+1)
    for num in range(1, N+1,1):
        # Check if it is safe to fill the position with num else move to next col
        if isSafe(grid,row,col,num):
            # Assigning num to the current pos and assuming num is in the correct pos
            grid[row][col]=num

            # Checking for next col's possibility
            if solveSudoku(grid,row,col+1):
                return True

        # We reach here as our assumption is wrong. So, go for next assumption
        #with different num value
        grid[row][col]=0
    return False

# Driver code
# 0 means unassigned cells
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
 
if(solveSudoku(grid,0,0)):
    printing(grid)
else:
    print("No solution exists")
