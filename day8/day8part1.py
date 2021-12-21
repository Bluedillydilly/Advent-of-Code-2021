def main():
    one = 1
    four = 4
    seven = 3
    eight = 7
    
    outputValues = []
    candidates = []
    
    
    f = open("input", "r")
    for line in f:
        line = line.strip()
        line = line.split(" | ")
        outputValues += [ l for l in line[1].split() ]
        
    
    f.close()
    
if __name__ == "__main__":
    main()