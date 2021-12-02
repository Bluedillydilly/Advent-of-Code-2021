def main():
    x: int = 0
    depth: int = 0
    aim: int = 0
    with open("input2", "r") as f:
        for line in f:
            match line.strip().split():
                case ["forward", dist]:
                    x += int(dist) 
                    depth += aim * int(dist)
                case ["down", dist]:
                    aim += int(dist)
                case ["up", dist]:
                    aim -= int(dist)
    print(f"x: {x}, depth: {depth}")
    print(f"Number: {x*depth}")
    
if __name__ == "__main__":
    main()