import linecache

with open("F:\AoC_2022\Day 6\input.txt", "r") as sentence:

    for i in range(len(sentence.readline())):
        if len(set(linecache.getline("F:\AoC_2022\Day 6\input.txt", 1)[i-4:i])) == 4:
            print(f"First marker after {i} characters.")
            if len(set(linecache.getline("F:\AoC_2022\Day 6\input.txt", 1)[i-14:i])) == 14:
                print(f"14 unique found after {i} characters.")


            




