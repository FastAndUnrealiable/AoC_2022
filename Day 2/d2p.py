"""
Calculates the total SCORE_1 of the rock-paper-scissor tournament.
"""

HAND = {"X": "1", "Y": "2", "Z":"3"}

def score_calc_first_challenge(opponent, chad):
    """Returns points depending on win/loose condition.

    Args:
        opponent STR: Opponents hand.
        chad STR: Players hand.

    Returns:
        int: points
    """

    points = (1,2,3)

    if (opponent == "A" and chad == "3") or (opponent == "B" and chad == "1") or (opponent == "C" and chad == "2"): ## Loose condition.
        return points[int(chad)-1]

    elif (opponent == "A" and chad == "2") or (opponent == "B" and chad == "3") or (opponent == "C" and chad == "1"): ## Win condition.
        return points[int(chad)-1]+6

    else: ## Draw condition.
        return points[int(chad)-1]+3


def score_calc_second_challenge(opponent, chad):
    """Function for second part of Day 2 challenge.

    Args:
        opponent STR: Opponents hand.
        chad STR: Players hand.

    Returns:
        INT: Score of the round.
    """

    big_dic = {"WIN": {"A": 2 , "B":3, "C":1},
            "LOOSE" : {"A": 3, "B": 1, "C":2},
            "DRAW" : {"A": 1, "B":2, "C": 3}}

    if chad == "1": ## Loose Condition.
        return big_dic["LOOSE"][opponent]

    elif chad == "2": ## Draw Condition.
        return big_dic["DRAW"][opponent]+3

    elif chad == "3": ## Win Condition.
        return big_dic["WIN"][opponent]+6

with open(r"F:\AoC_2022\Day 2\input.txt", "r", encoding="utf-8") as SCORE_BOOK:
    SCORE_1 = 0

    for line in SCORE_BOOK.readlines():
        SCORE_1 += score_calc_first_challenge(line[0], HAND[line[2]])

    print(f"Score for the first challenge is {SCORE_1}!\n")

with open(r"F:\AoC_2022\Day 2\input.txt", "r", encoding="utf-8") as SCORE_BOOK:
    SCORE_2 = 0

    for line in SCORE_BOOK.readlines():
        SCORE_2 += score_calc_second_challenge(line[0], HAND[line[2]])


    print(f"Score for the second challenge is {SCORE_2}!\n")
