from dataclasses import dataclass
from typing import Dict, List

marked: int = -1

def main():
    with open("input1", "r") as f:
        picks = list( map( lambda x: int(x, 10), f.readline().strip().split(',') ) )
        boards = []
        
        for line in f:
            current = []
            for i in range(5):
                l = f.readline().strip().split()
                current.append( list( map( lambda x: int(x, 10), l ) ) )
            boards.append(Board(current))
    # winner not possible in first 4 picks
    for i in range(4):
        for b in boards:
            b.mark(picks[i])
            
    
    for i in range(4, len(picks)):
        for b in boards:
            b.mark(picks[i])
            if b.winner():
                print(f"marked nums: {b.markedNums}, final score: {b.score()}\nboard: {b}")
                exit()
    
@dataclass
class Board:
    board: Dict
    markedRows: Dict
    markedCols: Dict
    markedNums: List
    
    def __init__(self, b):
        self.board = {b[row][col]:(row,col) for row in range(5) for col in range(5)}
        self.markedRows = {n:0 for n in range(5)}
        self.markedCols = {n:0 for n in range(5)}
        self.markedNums = []
        
    def mark(self, number):
        if number in self.board.keys():
            row, col = self.board[number]
            self.markedRows[row] += 1
            self.markedCols[col] += 1
            self.markedNums.append(number)
    
    def winner(self) -> bool:
        if len(self.markedNums) < 5:
            return False
        if 5 in self.markedRows.values() or 5 in self.markedCols.values():
            return True
        
    def score(self) -> int:
        return sum( [k for k,v in self.board.items() if k not in self.markedNums] ) * self.markedNums[-1]
    
if __name__ == "__main__":
    main()