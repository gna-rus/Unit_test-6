from unittest import TestCase
import pytest

from AverageValueInList import AverageValueInList

class TestAverageValueInList(TestCase):

    listTest = AverageValueInList([1, 2, 3], [5,7,9])

    def test_AverageList1(self):
        assert self.listTest.AverageList1() == 2

    def test_AverageList2(self):
        assert self.listTest.AverageList2() == 7