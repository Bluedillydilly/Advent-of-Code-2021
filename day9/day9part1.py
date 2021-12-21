def main():
    
    f = open("input", "r")
    lows = []
    lines = [[],
             [int(c) for c in list(f.readline().strip())],
             [int(c) for c in list(f.readline().strip())]]
    # buffer for first row
    lines[0] = [10 for i in lines[1]]
    
    # almost all lines
    for line in f:
        
        neighborCheck(lines, lows)
            
        lines[0] = lines[1]
        lines[1] = lines[2]
        lines[2] = [int(c) for c in list(line.strip())]
    f.close()
    
    # second to last
    neighborCheck(lines, lows)
    
    # last line
    lines[0] = lines[1]
    lines[1] = lines[2]
    lines[2] = [10 for i  in lines[1]]
        
    neighborCheck(lines, lows)
    
    return sum(lows)
    
def neighborCheck(lines, lows):
    for i in range(len(lines[1])):
        current = lines[1][i]
        if i > 0 and lines[1][i-1] <= current: # left
            continue
        elif i < len(lines[1])-1 and lines[1][i+1] <= current: # right
            continue
        elif lines[2][i] <= current or lines[0][i] <= current: # top/bottom
            continue
        lows.append(current+1)
    
if __name__ == "__main__":
    print("Sum of lows:", main())