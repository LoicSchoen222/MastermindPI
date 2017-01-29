import unittest
from MMRow import MMRow


class MMBoard:
    def __init__(self):
        self.numberOfRows = 8
        self.currentRow = 0
        self.rows = []
        self.finalRow = None
        for i in range(self.numberOfRows):
            self.rows += ('', '', '', '')

    def addRow(self, row=('', '', '', '')):
        if self.currentRow == self.numberOfRows:
            print("MMBoard: number of maximum rows (%d) reached" % self.numberOfRows)
            return None

        if not MMRow(row).validate():
            print("MMBoard: invalid row. All colors must be differents")
            return None

        self.rows[self.currentRow] = row
        self.currentRow += 1
        result = self.finalRow.compare(row)
        if result != None:
            stringResult = []
            for i in range(result[0]):
                stringResult.append("red")
            for i in range(result[1]):
                stringResult.append("white")
            return stringResult
        else:
            return result



    def getcurrentrow(self):
        return self.currentRow

    def setFinalRow(self, row):
        self.finalRow = MMRow(row)

    def show(self):
        print("Board: number of rows (%d), current row (%d)" % (self.numberOfRows, self.currentRow))
        for i in range(self.currentRow):
            print(self.rows[i])


class TestMMBoard(unittest.TestCase):
    def test_initRow(self):
        board1 = MMBoard()
        self.assertEquals(board1.currentRow, 0)
        self.assertIsNone(board1.finalRow)

    def test_setFinalRow(self):
        row1 = MMRow(('R', 'G', 'B', 'W'))
        board1 = MMBoard()
        board1.setFinalRow(row1)
        self.assertIsNotNone(board1.finalRow)

    def test_addRow(self):
        board1 = MMBoard()
        board1.addRow(('R', 'G', 'B', 'W'))
        self.assertEquals(board1.currentRow, 1)


if __name__ == '__main__':
    unittest.main()
