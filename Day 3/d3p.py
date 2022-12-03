"""_summary_
"""




def back_pack(item):

    first_half = item[:len(item)//2]
    second_half = item[len(item)//2:]

    common_letter = "".join(set(first_half).intersection(second_half))

    return common_letter

with open("F:\AoC_2022\Day 3\input.txt", "r", encoding="utf-8") as items:

    priority_list_lower = []
    priority_list_upper = []


    for item in items.readlines():
        LETTER = back_pack(item)
        if LETTER.islower():
            priority_list_lower.append(ord(LETTER)-96)
        else:
            priority_list_upper.append(ord(LETTER)-38)

    print(sum(priority_list_upper)+sum(priority_list_lower))
