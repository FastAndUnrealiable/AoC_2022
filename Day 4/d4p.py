"""See if there is any overlaping in the pairs.
"""


def double_one(pair):

    PAIR_ONE = []
    PAIR_TWO = []

    start, end = pair.split(",")
    for i in range(int(start.split("-")[0]),int(start.split("-")[1])+1):
        PAIR_ONE.append(i)

    for i in range(int(end.split("-")[0]),int(end.split("-")[1])+1):
        PAIR_TWO.append(i)

    return set(PAIR_ONE).issubset(PAIR_TWO) or set(PAIR_TWO).issubset(PAIR_ONE)

def double_two(pair):

    PAIR_ONE = []
    PAIR_TWO = []

    start, end = pair.split(",")

    for i in range(int(start.split("-")[0]),int(start.split("-")[1])+1):
        PAIR_ONE.append(i)

    for i in range(int(end.split("-")[0]),int(end.split("-")[1])+1):
        PAIR_TWO.append(i)

    return len(set(PAIR_ONE).intersection(PAIR_TWO))


with open("F:\AoC_2022\Day 4\input.txt", "r", encoding="utf-8") as pairs:

    DOUBLE_PAIRS = 0
    PAIR_AT_ALLT = 0

    for pair in pairs.readlines():

        if double_one(pair):
            DOUBLE_PAIRS += 1

        if double_two(pair) > 0:
            PAIR_AT_ALLT += 1


    print(

f"""First puzzle {DOUBLE_PAIRS}
Second puzzle {PAIR_AT_ALLT}
""")
