def syntaxErrorScore() -> int:
    f = open("input", "r")
    
    errorScore = 0
    scores = {')': 3, ']':57, '}':1197, '>':25137}
    pair = {')': '(', ']':'[', '}':'{', '>':'<'}
    
    for line in f:
        l = line.strip()
        stack: list = []
        
        for char in l:
            if char in pair.values(): # opening
                stack.append(char)
            else: # closing
                if stack[-1] == pair[char]: # valid closer
                    stack.pop(-1)
                else: # misplaced closer
                    errorScore += scores[char]
                    break
    f.close()
                
    return errorScore
    
if __name__ == "__main__":
    print( "Total error score: ", syntaxErrorScore())
    