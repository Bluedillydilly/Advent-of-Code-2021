from dataclasses import dataclass
from typing import Dict, List

def main() -> None:
    with open("input1", "r") as f:
        picks = list( map( lambda x: int(x, 10), f.readline().strip().split(',') ) )
        boards = []
        
        for line in f:
            current = []
            for i in range(5):
                l = f.readline().strip().split()
                current.append( list( map( lambda x: int(x, 10), l ) ) )
            boards.append(Board(current))
        
    for i in range(4):
        for b in boards:
            b.mark(picks[i])
            
    for pick in picks[4:]:
        losers = []
        for b in boards:
            b.mark(pick)
            if b.winner() and len(boards) == 1:
                print(f"Last board: marked nums: {b.markedNums}, final score: {b.score()}")
                exit()
            elif not b.winner():
                losers.append(b)
        boards = losers
    
    
@dataclass
class Board:
    board: Dict[int,tuple[int,int]]
    markedRows: Dict[int,int]
    markedCols: Dict[int,int]
    markedNums: List
    
    def __init__(self, b) -> None:
        self.board = {b[row][col]:(row,col) for col in range(5) for row in range(5)}
        self.markedRows = {n:0 for n in range(5)}
        self.markedCols = {n:0 for n in range(5)}
        self.markedNums = []
        
    def mark(self, number) -> None:
        if number in self.board.keys():
            row, col = self.board[number]
            self.markedRows[row] += 1
            self.markedCols[col] += 1
            self.markedNums.append(number)
    
    def winner(self) -> bool:
        return len(self.markedNums) >= 5 and (5 in self.markedRows.values() or 5 in self.markedCols.values())
        
    def score(self) -> int:
        return sum( [k for k,v in self.board.items() if k not in self.markedNums] ) * self.markedNums[-1]
    
if __name__ == "__main__":
    main()