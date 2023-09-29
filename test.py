from unittest import TestCase
import pytest

from AverageValueInList import AverageValueInList


class TestAverageValueInList(TestCase):
    listTest1 = AverageValueInList([1, 2, 3], [5, 7, 9])
    listTest2 = AverageValueInList("[1, 2, 3]", [1.2, 3.4, 5.6])
    listTestNull = AverageValueInList([], [])
    listTestMore2 = AverageValueInList([5, 7, 9], [1, 2, 3])
    listTestSame = AverageValueInList([5, 7, 9,11,13], [5, 7, 9,11,13])

    # тест на поиск среднего в 1 списке
    def test_AverageList1(self):
        assert self.listTest1.AverageList1() == 2

    # тест на поиск среднего в 2 списке
    def test_AverageList2(self):
        assert self.listTest1.AverageList2() == 7

    # негативный тест на ввод коллекции string
    def test_AverageList1STR(self):
        with pytest.raises(AssertionError):
            assert self.listTest2.AverageList1() == 2

    # тест на поиск среднего значения среди переменных типа float
    def test_AverageList2Float(self):
        assert self.listTest2.AverageList2() == 3.4

    #негативный тест на ввод пустого списка
    def test_AverageList1Null(self):
        with pytest.raises(AssertionError):
            assert self.listTestNull.AverageList1() == 0

    # Тест на корректный вывод когда среднее во втором спискее больше
    def test_AverageListMore2(self):
        assert self.listTest1.CompareTwoList() == "Второй список имеет большее среднее значение"

    # Тест на корректный вывод когда среднее в первом спискее больше
    def test_AverageListMore1(self):
        assert self.listTestMore2.CompareTwoList() == "Первый список имеет большее среднее значение"

    # Тест на корректный вывод когда средние значения равны
    def test_AverageListsSame(self):
        assert self.listTestSame.CompareTwoList() == "Средние значения равны"

 









