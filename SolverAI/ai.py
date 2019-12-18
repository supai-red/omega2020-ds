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

        self._puzzle = puzzle
        self.technique = technique
        self._combined = lambda rows, columns: [each_letter + every_number for each_letter in rows for every_number in columns]
        self._boxes = self._combined(self.row_values, self.column_values)
        self._row_units = [self._combined(each_letter, self.column_values) for each_letter in self.row_values]
        self._column_units = [self._combined(self.row_values, every_number) for every_number in self.column_values]
        self._square_units = [self._combined(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")]
        self._unitlist = self._row_units + self._column_units + self._square_units
        self._units = dict((s, [u for u in self._unitlist if s in u]) for s in self._boxes)
        self._peers = dict((s, set(sum(self._units[s], [])) - set([s])) for s in self._boxes)
        self._values = dict(zip(self._boxes, ["123456789" if element == "." else element for element in self._puzzle]))

    def single_position(self):

        """
        Completes an iteration of the single_position technique and returns a
        dictionary.
        ----------------------------------------------------------------------

        Key = Sqaure coordinate (example: A1)
        Value = Solved squares or possible numbers that can be entered in a
                square (example: '569' or '1')
        """

        solved_values = [box for box in self._values.keys() if len(self._values[box]) == 1]
        for box in solved_values:
            digit = self._values[box]
            for peer in self._peers[box]:
                self._values[peer] = self._values[peer].replace(digit, "")
        return self._values

    def single_candidate(self):
        """
        Completes an iteration of the single_candidate technique and returns a
        dictionary.
        ----------------------------------------------------------------------

        Key = Sqaure coordinate (example: A1)
        Value = Solved squares or possible numbers that can be entered in a
                square (example: '569' or '1')
        """

        for unit in self._unitlist:
            for digit in "123456789":
                dplaces = [box for box in self._units if digit in self._values[box]]
                if len(dplaces) == 1:
                    self._values[dplaces[0]] = digit
        return self._values

    def solve(self):

        """
        Returns a tuple with three elements:
        1. string - "Solved" or "Not Solved"
        2. dictionary - Key = The squares coordinate (example: A1)
                        Value = Number that goes into the sqaure (example: 1)
        3. string - "Number of iterations made: 5" This is how many times the
                     algorithm had to iterate through the puzzle
        """

        if self.technique == "single_position":
            stalled = False
            start = 0
            while not stalled:
                start += 1
                solved_values_before = len([box for box in self._values.keys() if len(self._values[box]) == 1])
                self._values = self.single_position()
                solved_values_after = len([box for box in self._values.keys() if len(self._values[box]) == 1])
                stalled = solved_values_before == solved_values_after
                if len([box for box in self._values.keys() if len(self._values[box]) == 0]):
                    return False

            if solved_values_before == 81:
                return ("Solved", self._values, f"Number of iterations made: {start}")
            else:
                return ("Not solved", self._values, f"Number of iterations made: {start}")

        elif self.technique == "single_candidate":
            stalled = False
            start = 0
            while not stalled:
                start += 1
                solved_values_before = len([box for box in self._values.keys() if len(self._values[box]) == 1])
                self._values = self.single_position()
                self._values = self.single_candidate()
                solved_values_after = len([box for box in self._values.keys() if len(self._values[box]) == 1])
                stalled = solved_values_before == solved_values_after
                if len([box for box in self._values.keys() if len(self._values[box]) == 0]):
                    return False

            if solved_values_before == 81:
                return ("Solved", self._values, f"Number of iterations made: {start}")
            else:
                return ("Not solved", self._values, f"Number of iterations made: {start}")

        else:
            print("That is not an option")

    def show_puzzle(self):

        """
        Shows the puzzle as a 2-D string with a . (dot) as a placeholder for
        empty squares.
        """

        width = 1 + max(len(self._values[s]) for s in self._boxes)
        line = '+'.join(['-' * (width * 3)] * 3)
        for r in self.row_values:
            print(''.join(self._values[r + c].center(width) + ('|' if c in '36' else '') for c in self.column_values))
            if r in 'CF': print(line)

    def show_solved_attempt(self):

        """
        Shows the puzzle as a 2-D string, after attempting a Sudoku technique.
        If the puzzle cannot be solved, unsolved squares will be replaced by the
        possible numbers that can fill that square.
        """

        width = 1 + max(len(self.solve()[1][s]) for s in self._boxes)
        line = '+'.join(['-' * (width*3)] * 3)
        for r in self.row_values:
            print(''.join(self.solve()[1][r + c].center(width) + ('|' if c in '36' else '') for c in self.column_values))
            if r in 'CF': print(line)
