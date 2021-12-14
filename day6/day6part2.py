def main():
    BIRTH = 0
    POST = 6
    BABY = 8
    SIM_DAYS = 256
    f = open("input.1")
    
    population = [0] * 9 # slot i is count of population on stage i
    
    for fish in f.readline().strip().split(","):
        population[ int(fish) ] += 1
    
    print("Initial:", population)
    
    for i in range(SIM_DAYS):
        mommaCount = population[BIRTH]   
        for t in range(0,BABY): # decrease timer
            population[t] = population[t+1]
        # move mommas to post
        population[POST] += mommaCount
        # new births
        population[BABY] = mommaCount
    
    f.close()
    print(f"Total pop: {sum(population)}")
    
if __name__ == "__main__":
    main()