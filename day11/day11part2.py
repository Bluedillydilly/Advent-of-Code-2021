def octopus():
    f = open("input", "r")
    
    matrix = [[int(c) for c in line.strip()] for line in f]
    f.close()
    
    step = 0
    while True:
        step += 1
        if octStep(matrix):
            return step
        
    
def octStep(array: list) -> bool:
    rowCount = len(array)
    colCount = len(array[0])
    for row in range(rowCount):
        for col in range(colCount):
            array[row][col] += 1
           
    flashUpdates = 1
    flashSet = set()
    while flashUpdates != 0:
        flashUpdates = octFlash(array, flashSet)
        
    if len(flashSet) == rowCount*colCount:
        octSleep(array, flashSet)
        print("Synchronized flash!")
        return True
    
    octSleep(array, flashSet)
    
    return False
          
          
def octFlash(array: list, flashSet: set) -> int:
    rowCount = len(array)
    colCount = len(array[0])
    flashCount = 0
    for row in range(rowCount):
        for col in range(colCount):
            if array[row][col] > 9 and (row, col) not in flashSet:
                flashCount += 1
                flashSet.add((row, col))
                if row > 0 and col > 0: #Top Left
                    array[row-1][col-1] += 1
                if row > 0: # Top Middle
                    array[row-1][col] += 1
                if row > 0 and col < colCount - 1: # Top Right
                    array[row-1][col+1] += 1
                if col > 0: # Middle Left
                    array[row][col-1] += 1
                if col < colCount - 1: # Middle Right
                    array[row][col+1] += 1
                if row < rowCount - 1 and col > 0: # Bottom Left
                    array[row+1][col-1] += 1
                if row < rowCount - 1: # Bottom Middle
                    array[row+1][col] += 1
                if row < rowCount - 1 and col < colCount - 1: # Bottom Right
                    array[row+1][col+1] += 1
    return flashCount
           
def octSleep(matrix: list, flashSet: set) -> None:
    for flashed in flashSet:
        matrix[flashed[0]][flashed[1]] = 0
    
if __name__ == "__main__":
    print( "First synchronized flash: ", octopus() )