# https://leetcode.com/problems/design-spreadsheet/?envType=daily-question&envId=2025-09-19
# Design Spreadsheet

class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26
        self.grid = {}

    def _parse_cell(self, cell: str):
       
        col_char = cell[0]
        col = ord(col_char) - ord('A')
        row = int(cell[1:]) - 1
        return (row, col)

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._parse_cell(cell)
        self.grid[(row, col)] = value

    def resetCell(self, cell: str) -> None:
        row, col = self._parse_cell(cell)
        if (row, col) in self.grid:
            del self.grid[(row, col)]

    def _get_cell_value(self, cell: str) -> int:
        row, col = self._parse_cell(cell)
        return self.grid.get((row, col), 0)

    def getValue(self, formula: str) -> int:
       
        assert formula.startswith("=")
        parts = formula[1:].split("+")
        total = 0
        for part in parts:
            if part[0].isalpha():
                # it's a cell reference
                total += self._get_cell_value(part)
            else:
                # it's an integer
                total += int(part)
        return total

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)