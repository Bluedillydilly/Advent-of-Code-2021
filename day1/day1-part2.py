def main():
    count: int = 0
    with open("input-part2", "r") as f:
        # set up first window
        num1: int = int(f.readline().strip())
        num2: int = int(f.readline().strip())
        num3: int = int(f.readline().strip())
        num4: int = int(f.readline().strip())
        if num1 < num4: # second window larger
            count += 1
        for line in f:
            num1 = num2
            num2 = num3
            num3 = num4
            num4: int = int(line.strip())
            if num1 < num4: # second window larger
                count += 1
    print(f"{count} larger successor windows")

if __name__ == "__main__":
    main()
