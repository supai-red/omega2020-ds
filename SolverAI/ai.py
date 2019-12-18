class Sudoku:

    """
    Sudoku class
    ------------
    Solves Sudoku puzzles using various techniques. Can display starting
    position and solved attempts as a 2-D string

    Parameters
    -----------
    puzzle(string): A sudoku puzzle in the format '8...74...1.........7.5.9.4.'
                    where the . (dot) represents an empty square
                    puzzle string must have length of 81
    technique(string): 'single_position' or 'single_candidate'
                        default = 'single_position'
                        all techniques use 'single_position'
    """

    row_values = "ABCDEFGHI"
    column_values = "123456789"

    def __init__(self, puzzle, technique='single_position'):
        self.puzzle = puzzle
        self.technique = technique
        self._combined = lambda rows, columns: [each_letter + every_number for each_letter in rows for every_number in columns]

    def single_position(self):
        pass

    def single_candidate(self):
        pass

    def solve(self):

        """
        Returns a tuple with three elements:
        1. string - "Solved" or "Not Solved"
        2. dictionary - Key = The squares coordinate (example: A1)
                        Value = Number that goes into the sqaure (example: 1)
        3. string - "Number of iterations made: 5" This is how many times the
                     algorithm had to iterate through the puzzle
        """
        pass

    def show_puzzle(self):

        """
        Shows the puzzle as a 2-D string with a . (dot) as a placeholder for
        empty squares.
        """
        pass

    def show_solved_attempt(self):

        """
        Shows the puzzle as a 2-D string, after attempting a Sudoku technique.
        If the puzzle cannot be solved, unsolved squares will be replaced by the
        possible numbers that can fill that square.
        """
        pass
