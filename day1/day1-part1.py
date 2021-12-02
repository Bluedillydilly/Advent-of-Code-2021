
def main():
    count = 0
    prev = 0
    with open("input", "r") as f:
        f.readline()
        for line in f:
            num = int(line.strip())
            if num > prev:
                count += 1
            prev = num
    print("Increases from previous measurement: ", count)

if __name__ == "__main__":
    main()
