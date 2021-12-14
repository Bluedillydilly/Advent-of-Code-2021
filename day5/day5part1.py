def main() -> None:
    f = open("input.1", "r")
    
    coordCounts = {}
    count = 0
    
    
    for line in f:
        line = line.split(" -> ")
        splits =  [[int(e[0]), int(e[1])] for e in [end.split(",") for end in line]]
        x1, y1 = splits[0]
        x2, y2 = splits[1]
        if x1 == x2: # vertical line - same x, diff y
            diff = y1 - y2
            if diff < 0:
                start = (x1, y1)
            else:
                start = (x2, y2)
            for i in range(abs(diff)+1):
                coordCounts[(start[0], start[1]+i)] = coordCounts.get((start[0], start[1]+i), 0) + 1
                
        elif y1 == y2: # horizontal line - diff x, same y
            diff = x1 - x2
            if diff < 0:
                start = (x1, y1)
            else:
                start = (x2, y2)
            for i in range(abs(diff)+1):
                coordCounts[(start[0]+i, start[1])] = coordCounts.get((start[0]+i, start[1]), 0) + 1
            
    for k,v in coordCounts.items(): # danger point counts
        if v > 1:
            count += 1
    print(f"danger points: {count}")
    f.close()

def sign(a) -> int:
    return int(a/abs(a))

if __name__ == "__main__":
    main()                                      