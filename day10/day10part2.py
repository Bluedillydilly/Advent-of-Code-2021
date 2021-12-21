from typing import NamedTuple

class Symbol(NamedTuple):
    start: str
    end: str
    score: int

def syntaxErrorScore() -> int:
    f = open("input", "r")
    
    errors = []
    scores = {')': 1, ']':2, '}':3, '>':4}
    opener = {')': '(', ']':'[', '}':'{', '>':'<'}
    closer = {v:k for k,v in opener.items()}
    
    
    for line in f:
        l = line.strip()
        stack: list = []
        corruptLine = False
        
        for char in l:
            if char in closer.keys(): # opening
                stack.append(char)
            else: # closing
                if stack[-1] == opener[char]: # valid closer
                    stack.pop(-1)
                else: # misplaced closer
                    corruptLine = True
                    break
        if not corruptLine: # add missing
            currentError = 0
            while stack:
                currentError *= 5
                currentError += scores[ closer[ stack.pop(-1) ] ]
            errors.append(currentError)
                
    f.close()
           
    errors.sort()     
    return errors[int(len(errors)/2)]
    
if __name__ == "__main__":
    print( "Total error score: ", syntaxErrorScore())