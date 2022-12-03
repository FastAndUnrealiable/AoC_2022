"""LMAO this shit is messy
"""
from pymongo import MongoClient
import linecache

CLIENT = MongoClient("mongodb://localhost:27017")
DB = CLIENT["AoC"]
COLLECTION = DB["Elf Groups"]

COLLECTION.delete_many({})


def backpack_first_challenge(item):
    """Determines the value of backpack items.

    Args:
        item STRING: One backpack

    Returns:
        common_letter STRING: One common letter that first and second slot in the backpack shares.
    """

    first_half = item[:len(item)//2]
    second_half = item[len(item)//2:]

    common_letter = "".join(set(first_half).intersection(second_half))

    return common_letter


def backpack_second_challenge(ELFS, GROUP):
    """Determines the value of one group backpack items.

    Args:
        ELFS LIST: The three ELFS.
        GROUP INT: Group Number.

    Returns:
        Card DICTIONARY: Returns a sorted DIC.
    """

    card = {
    "Group": GROUP,
    "First Elf": ELFS[0],
    "Second Elf": ELFS[1],
    "Third Elf": ELFS[2]
    }

    return card

with open("F:\AoC_2022\Day 3\input.txt", "r", encoding="utf-8") as items:

    priority_list_lower_1 = []
    priority_list_upper_1 = []

    for item in items.readlines():
        LETTER = backpack_first_challenge(item)
        if LETTER.islower():
            priority_list_lower_1.append(ord(LETTER)-96)
        else:
            priority_list_upper_1.append(ord(LETTER)-38)
    print(f"Value for first part is {sum(priority_list_upper_1)+sum(priority_list_lower_1)}")

with open("F:\AoC_2022\Day 3\input.txt", "r", encoding="utf-8") as items:

    priority_list_lower_2 = []
    priority_list_upper_2 = []

    GROUP = 0
    ELFS = []
    for num, item in enumerate(items):
        if num % 3 == 2:
            [ELFS.append(linecache.getline("input.txt", (num-1)+x).strip("\n")) for x in range(3)]
            GROUP += 1
            COLLECTION.insert_one(backpack_second_challenge(ELFS, GROUP))
            ELFS = []

DATABASE = COLLECTION.find({})

for DOCUMENT in DATABASE:
    INTERSECT_ONE = "".join(set(DOCUMENT["First Elf"]).intersection(DOCUMENT["Second Elf"]))
    CHARACTER = "".join(set(INTERSECT_ONE).intersection(DOCUMENT["Third Elf"]))

    if CHARACTER.islower():
        priority_list_lower_2.append(ord(CHARACTER)-96)
    else:
        priority_list_upper_2.append(ord(CHARACTER)-38)

print(f"Value for second part is {sum(priority_list_upper_2)+sum(priority_list_lower_2)}")
