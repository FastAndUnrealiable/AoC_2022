"""
Calculates and prints max caloric values amongst the elfs and the top three values.
"""

with open(r"E:\AoC_2022\Day 1\input.txt", "r", encoding="utf-8") as CAL_VALUES:
    calories = []
    TMP_CAL_SUM = 0

    for line in CAL_VALUES:
        try:
            TMP_CAL_SUM += int(line.strip())
        except: # pylint: disable=W0702
            calories.append(TMP_CAL_SUM)
            TMP_CAL_SUM = 0

    print(max(calories), sum(sorted(calories)[-3:]))
