class AverageValueInList:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def AverageList1(self):
        try:
            value = 0
            for i in self.list1:
                value += i
            return value / len(self.list1)
        except:
            return AssertionError

    def AverageList2(self):
        try:
            value = 0
            for i in self.list2:
                value += i
            return value / len(self.list2)
        except:
            return AssertionError

    def CompareTwoList(self):
        if (self.AverageList1() > self.AverageList2()):
            return "Первый список имеет большее среднее значение"
        elif (self.AverageList1() < self.AverageList2()):
            return "Второй список имеет большее среднее значение"
        elif (self.AverageList1() == self.AverageList2()):
            return "Средние значения равны"

