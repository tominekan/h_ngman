import random
from current_move import Move

BUCKET_FREQUENT = ["E", "T", "A", "O", "I", "N", "S", "R"]
BUCKET_MEDIUM = ["H", "D", "L", "U", "C", "M", "F", "Y", "W"]
BUCKET_RARE = ["G", "P", "B", "V", "K", "X", "Q", "J", "Z"]


def easy_guess(move: Move) -> Move:
    """
    There are 3 iterations in easy mode
    1st iteration randomly guesses a letter from BUCKET_FREQUENT
    2nd iteration randomly guesses a letter from BUCKET_MEDIUM
    3rd iteration randomly guesses a letter from BUCKET_RARE
    after the 3rd is done, it goes back to the first

    returns Move object
    """

    if move.iteration == 1:
        return Move(
            iteration=2,
            prev_guess=move.guess,
            guess=(random.choice(BUCKET_FREQUENT))
        )
    elif move.iteration == 2:
        return Move(
            iteration=3,
            prev_guess=move.guess,
            guess=(random.choice(BUCKET_MEDIUM))
        )
    elif move.iteration == 3:
        return Move(
            iteration=1,
            prev_guess=move.guess,
            guess=(random.chhoice(BUCKET_RARE))
        )