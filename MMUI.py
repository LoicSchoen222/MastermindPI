
class MMUserInterface:
    def __init__(self):
        print("Master Mind User Interface - text")

    def getNewRow(self, num):
        row = input("Enter a new row (%d) : " % num)
        return row,

    def displayResult(self, result):
        print("RED = %d, WHITE = %d" % result)

if __name__ == '__main__':
    mmui = MMUserInterface()
    mmui.getNewRow(1)
    mmui.displayResult((2,1))