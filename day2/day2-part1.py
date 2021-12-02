def main():
    x: int = 0
    depth: int = 0
    with open("input1", "r") as f:
        for line in f:
            match line.strip().split():
                case ["forward", dist]:
                    x += int(dist) 
                case ["down", dist]:
                    depth += int(dist)
                case ["up", dist]:
                    depth -= int(dist)
    print(f"x: {x}, depth: {depth}")
    print(f"Number: {x*depth}")
    
if __name__ == "__main__":
    main()