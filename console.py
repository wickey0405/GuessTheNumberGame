import sys
import random

class Console:
    def __init__(self):
        self.minNum = 0
        self.maxNum = 1
        self.answerNum = 0
        self.numList = []
        self.userChosenNumList = []
        self.gameLevel = 0
        self.maxCount = 0
        self.currCount = 1

    def startMessage(self):
        print('GUESS THE NUMBER GAME')

    def fromStdoutToNumber(self, s):
        temp = float(s)
        if temp % 1 == 0:
            return int(s)
        else:
            return temp 

    def isMinNumInteger(self):
        return type(self.minNum) is int
    
    def isMaxNumInteger(self):
        return type(self.maxNum) is int

    def isGameLevelIntegerAndAvailable(self):
        return type(self.gameLevel) is int and 0 <= self.gameLevel <= 2

    def setMinNum(self):
        sys.stdout.buffer.write(b'Input minimum number!\n')
        sys.stdout.flush()
        self.minNum = self.fromStdoutToNumber(sys.stdin.buffer.readline().decode())
        while(not self.isMinNumInteger()):
            sys.stdout.buffer.write(b'Input Integer Number as minimum number!\n')
            sys.stdout.flush()
            self.minNum = self.fromStdoutToNumber(sys.stdin.buffer.readline().decode())
        print(f'[OK!]-->The minimum number is {self.minNum}')

    def setMaxNum(self):
        sys.stdout.buffer.write(b'Input maximum number of the game!\n')
        sys.stdout.flush()
        self.maxNum = self.fromStdoutToNumber(sys.stdin.buffer.readline().decode())
        while(not self.isMaxNumBiggerThanMinNum() or not self.isMaxNumInteger()):
            sys.stdout.buffer.write(b'[NG]-->Input the Integer number which is bigger than minimum number!\n')
            sys.stdout.flush()
            self.maxNum = self.fromStdoutToNumber(sys.stdin.buffer.readline().decode())
        self.numList = range(self.minNum, self.maxNum+1)
        print(f'[OK]-->The maximum number is {self.maxNum}')

    def isMaxNumBiggerThanMinNum(self):
        return self.minNum < self.maxNum
    
    def createAnswerNum(self):
        self.answerNum = random.randint(self.minNum, self.maxNum)

    def setGameLevel(self):
        sys.stdout.buffer.write(b'Input game Level.[0...Easy, 1...Normal, 2...Hard]\n')
        sys.stdout.flush()
        self.gameLevel = self.fromStdoutToNumber(sys.stdin.buffer.readline().decode())

        while(not self.isGameLevelIntegerAndAvailable()):
            sys.stdout.buffer.write(b'[NG]-->Input 0 or 1 or 2!\n')
            sys.stdout.flush()
            self.gameLevel = self.fromStdoutToNumber(sys.stdin.buffer.readline().decode())

        print(f'[OK]-->The gameLevel is {self.gameLevel}')

        if self.gameLevel == 0:
            self.maxCount = len(self.numList)
        elif self.gameLevel == 1:
            self.maxCount = len(self.numList)//2
        else:
            self.maxCount = len(self.numList)//5 if len(self.numList)//5 != 0 else 1
    
    def viewGameProperty(self):
        print("----------GameModeDescription-----------------------------------")
        print(f"min: {self.minNum}, max: {self.maxNum}, level: {self.gameLevel}, challenge times: {self.maxCount}")

    def playGame(self):
        print("--------------------------------------------------------")
        while(self.currCount <= self.maxCount):
            print(f"Choose number in the list below! (your life is {self.maxCount-self.currCount+1})")
            print([num for num in self.numList if num not in self.userChosenNumList])
            sys.stdout.buffer.write(b'Input your guess number\n')
            sys.stdout.flush()
            tempNum = self.fromStdoutToNumber(sys.stdin.buffer.readline().decode())
            print("--------------------------------------------------------")
            if tempNum is self.answerNum:
                print(f"You Win! The answer is {self.answerNum}")
                break
            self.userChosenNumList.append(tempNum)
            self.currCount += 1
        if self.currCount > self.maxCount:
            print(f"You Lose! The answer is {self.answerNum}")