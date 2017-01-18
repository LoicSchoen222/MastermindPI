import unittest


class MMRow:
    def __init__(self, row=('', '', '', '')):
        """

        :type row: tuple with 4 elements
        """
        self.row = row

    def show(self):
        print(self.row)

    def compare(self, row):
        red = 0
        white = 0
        for j in range(4):
            for i in range(4):
                if self.row[i] == row[j]:
                    if i == j:
                        red += 1
                    else:
                        white += 1

        return red, white

    def validate(self):
        #validate unicity
        for j in range(4):
            numberofiteration = 0
            for i in range(4):
                if self.row[i] == self.row[j]:
                    numberofiteration += 1
            if numberofiteration != 1 :
                return False

        return True


class TestMMRow(unittest.TestCase):
    def test_compare(self):
        row1 = MMRow(('R', 'G', 'B', 'W'))
        self.assertEquals((0, 0), row1.compare(('', '', '', '')))
        self.assertEquals((1, 0), row1.compare(('R', '', '', '')))
        self.assertEquals((2, 0), row1.compare(('R', '', 'B', '')))
        self.assertEquals((2, 2), row1.compare(('R', 'W', 'B', 'G')))
        self.assertEquals((0, 4), row1.compare(('B', 'W', 'R', 'G')))
        self.assertEquals((4, 0), row1.compare(('R', 'G', 'B', 'W')))

    def test_validate(self):
        row1 = MMRow(('R', 'G', 'B', 'W'))
        self.assertTrue(row1.validate())

if __name__ == '__main__':
    unittest.main()
