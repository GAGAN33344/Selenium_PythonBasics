from Oops import Calculator


class ChildImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 3, 4)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


obj1 = ChildImp()
print(obj1.getCompleteData())
