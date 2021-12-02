
def main():
    count: int = 0
    with open("input", "r") as f:
        prev: int = int(f.readline().strip())        
        for line in f:
            num: int = int(line.strip())
            if num > prev:
                count += 1
            prev = num
    print("Increases from previous measurement: ", count)

if __name__ == "__main__":
    main()
