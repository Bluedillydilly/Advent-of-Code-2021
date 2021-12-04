from functools import reduce

def main():
    with open("input1", "r") as f:
        candidates0 = []
        candidates1 = []
        
        for line in f:
            lineBits = list(line.strip())
            if lineBits[0] == '0':
                candidates0.append(lineBits)
            elif lineBits[0] == '1':
                candidates1.append(lineBits)
        oxy, co2 = 0, 0
        if len(candidates0) > len(candidates1):
            oxy = oxyRating(candidates0)
            co2 = co2Rating(candidates1)
        else:
            oxy = oxyRating(candidates1)
            c02 = co2Rating(candidates0)
        print(f"oxygen: {oxy}, co2: {co2}, life supprot: {oxy*co2}")

def oxyRating(candidates):
    bitLength = len(candidates[0])
    for i in range(1, bitLength):
        c0, c1 = fork(candidates, i)
        if len(c0) > len(c1):
            candidates = c0
        else:
            candidates = c1
        if len(candidates) == 1:
            return int( "".join(candidates[0]), 2 )

def co2Rating(candidates):
    bitLength = len(candidates[0])
    for i in range(1, bitLength):
        c0, c1 = fork(candidates, i)
        if len(c0) > len(c1):
            candidates = c1
        else:
            candidates = c0
        if len(candidates) == 1:
            return int( "".join(candidates[0]), 2 )

def fork(candidates, i):
    c1 = []
    c0 = []
    
    for c in candidates:
        if c[i] == '0':
            c0.append(c)
        elif c[i] == '1':
            c1.append(c)
    
    return (c0, c1)
    

if __name__ == "__main__":
    main()