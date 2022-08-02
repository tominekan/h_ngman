import uuid

class Move:
    def __init__(self, iteration: int, best_solution: list, prev_guess=None, guess=None, rejected_words=None):
        self.iteration = iteration
        self.prev_guess = prev_guess
        self.guess = guess
        self.best_solution = best_solution
        self.move_id = uuid.uuid4()
        self.rejected_words = rejected_words
    
    def logMove(self):
        print(f"Move #{self.move_id}")
        print(f"    Previous Guess: {self.prev_guess}")
        print(f"    Current Guess: {self.guess}")
        print(f"    Current Solution: {self.best_solution}")
        print(f"    Algorithm Iteration #: {self.iteration}")
