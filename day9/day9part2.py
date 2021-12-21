from typing import List, Set
from collections import namedtuple
from math import prod
from operator import itemgetter
   
LowPoint = namedtuple("LowPoint", ["row", "col", "value"])

def lowPoints() -> set:
    
    f = open("input", "r")
    lines: list = [[],
             [int(c) for c in list(f.readline().strip())],
             [int(c) for c in list(f.readline().strip())]]
    # buffer for first row
    lines[0] = [10 for i in lines[1]]
    lows: set[LowPoint, ...] = set()
    lineNumber: int = 0
    
    # almost all lines
    for line in f:
        lowCheck(lines, lineNumber, lows)
            
        lines[0] = lines[1]
        lines[1] = lines[2]
        lines[2] = [int(c) for c in list(line.strip())]
        lineNumber += 1
    f.close()
    
    # second to last
    lowCheck(lines, lineNumber, lows)
    lineNumber += 1
    
    # last line
    lines[0] = lines[1]
    lines[1] = lines[2]
    lines[2] = [10 for i  in lines[1]]
        
    lowCheck(lines, lineNumber, lows)
    
    return lows
    
def lowCheck(lines: list, row: int, lows: set) -> None:
    for c in range(len(lines[1])):
        if isLow(lines, c):
            lows.add(LowPoint(row, c, lines[1][c]))
    
def isLow(lines: list, column: int) -> bool:
    current = lines[1][column]
    if column > 0 and lines[1][column-1] <= current: # left
        return False
    elif column < len(lines[1])-1 and lines[1][column+1] <= current: # right
        return False
    elif lines[2][column] <= current or lines[0][column] <= current: # top/bottom
        return False
    return True
    
def basins(startPoints: list) -> int:
    f = open("input", "r")
    array = [[int(c) for c in list(line.strip())] for line in f]
    currentBasin = set()
    basinSizes: list = []
    
    # for each start point
    for s in startPoints:
        basinSizes.append(len(exploreBasin(s, array)))
        
    print(basinSizes)    
    return prod(sorted(basinSizes, reverse=True)[0:3])

def getNeighbors(current: LowPoint, board: list) -> list[LowPoint, ...]:
    l = []
    if current.row > 0: # top neighbor
        l.append(LowPoint(row=current.row-1, col=current.col, value=board[current.row-1][current.col]))
    if current.row < len(board) - 1: # bottom neighbor
        l.append(LowPoint(row=current.row+1, col=current.col, value=board[current.row+1][current.col]))
    if current.col > 0: # left neighbor
        l.append(LowPoint(row=current.row, col=current.col-1, value=board[current.row][current.col-1]))
    if current.col < len(board[0]) - 1: # right neighbor
        l.append(LowPoint(row=current.row, col=current.col+1, value=board[current.row][current.col+1]))
    
    return l

def exploreBasin(startPoint: LowPoint, board: list) -> None:
    currentBasin = set()
    currentBasin.add(startPoint)
    #print("Basin: ", currentBasin)
    queue = []
    queue.append(startPoint)
    
    while queue:
        currentPoint = queue.pop(0)
        #print("Basin point: ", currentPoint)
        for n in getNeighbors(currentPoint, board):
            if n not in currentBasin and n.value < 9:
                queue.append(n)
                currentBasin.add(n)
                #print("Basin: ", currentBasin)
                
    return currentBasin
    # explore left, right, top, down until 9

    
if __name__ == "__main__":
    startPoints: list = list(lowPoints())
    startPoints.sort(key=lambda point: (point.row, point.col) )
    print("low points: ", startPoints)
    basinNum: int = basins(startPoints)
    print("Basins: ", basinNum)