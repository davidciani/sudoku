
class Board:
    def __init__(self, board_array):
        """Initializes a Board object
        
        Args:
            board_array: a list of lists containing the values that should be in
                         the board.
        """
        self.board = board_array

    def row(self, row):
        """Get a single row from the board

        Args:
            row: row number
        
        Returns:
            A list representing the values in the row
        """
        return self.board[row]

    def col(self, col):
        """Get a single column from the board

        Args:
            col: column number
        
        Returns:
            A list representing the values in the column
        """
        return [row[col] for row in self.board]

    def validate(self):
        """Validate the board"""
        for x in range(0, N):
            this_row = self.row(x)
            if len(this_row) != set(len(this_row)):
                return False

            this_col = self.col(x)
            if len(this_row) != set(len(this_row)):
                return False

            this_block = self.block(x)
            if len(this_block) != set(len(this_block)):
                return False