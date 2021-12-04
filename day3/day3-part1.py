from functools import reduce

def main():
    with open("input1", "r") as f:
        numLength = len(f.readline().strip())
        f.seek(0)
        counts = [0] * numLength
        for line in f:
            line = line.strip()
            c = [2*int(c)-1 for c in line]
            counts = [counts[i]+c[i] for i in range(numLength)]
        gamma = int(reduce(revert, counts, ""), 2)
        epsilon = int( invert(reduce(revert, counts, "")), 2)
        print(f"gamma: {gamma}, epsilon: {epsilon}")
        print(f"power: {gamma*epsilon}")

def revert(a, b):
    if b > 0:
        return a + '1'
    else:
        return a + '0'

def invert(a):
    c = list(a)
    for i in range(len(c)):
        if c[i] == '1':
            c[i] = '0'
        else:
            c[i] = '1'
    return ''.join(c)
            

if __name__ == "__main__":
    main()