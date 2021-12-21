def main():
    f = open("input.1", "r")
    values = [ int(v) for v in f.readline().strip().split(",") ]
    f.close()
    print(values)
    
    
    position = median(values)
    totalCost = distFrom(values, position)
    print(f"Starting position: {position}")
    print(f"Starting cost: {totalCost}")
    
    change = 0
    if distFrom(values, position+1) < totalCost:
        change = 1
    else:
        change = -1
        
    position += change
    currentCost = distFrom(values, position)
    print(f"\nposition: {position}")
    print(f"cost: {currentCost}")
    
    
    
    while currentCost < totalCost:
        totalCost = currentCost
        position += change
        currentCost = distFrom(values, position)
        print(f"\nposition: {position}")
        print(f"cost: {totalCost}")
    
    
    
def median(x) -> int:
    if len(x) % 2 == 1:
        return x[ int(len(x)/2) ]
    return int( ( x[ int(len(x)/2) ] + x[ int(len(x)/2) + 1 ]  ) / 2 )
    
def distFrom(xs, v) -> int:
    return sum([ abs(xi-v) for xi in xs])
    
if __name__ == "__main__":
    main()