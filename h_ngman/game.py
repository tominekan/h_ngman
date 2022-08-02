from algorithms import easy_guess
from current_move import Move
class Game:
    def __init__(self, mode: str, word_length: int, num_tries=6):
        self.mode = mode
        self.num_tries = num_tries
        self.word_length = word_length
        # History of moves played
        self.moves = []
        self.latest_index = 0

    def validate_guess(self, move: Move):
        print(f"Does Your Word Have A {move.guess}"})
        for i in range(self.word_length +1): 
            input(f"Letter {i+1}")
    
    def add_move(self, move: Move):
        self.moves.append(Move)
        self.latest_index += 1 

    def apply_algorithm(self):
        if self.mode == "EASY":
            return easy_guess()