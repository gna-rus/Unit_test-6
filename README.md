# Unit_test-6
## Отчет покрытия тестами


============================= test session starts =============================
collecting ... collected 8 items

test.py::TestAverageValueInList::test_AverageList1 PASSED                [ 12%]
test.py::TestAverageValueInList::test_AverageList1Null PASSED            [ 25%]
test.py::TestAverageValueInList::test_AverageList1STR PASSED             [ 37%]
test.py::TestAverageValueInList::test_AverageList2 PASSED                [ 50%]
test.py::TestAverageValueInList::test_AverageList2Float PASSED           [ 62%]
test.py::TestAverageValueInList::test_AverageListMore1 PASSED            [ 75%]
test.py::TestAverageValueInList::test_AverageListMore2 PASSED            [ 87%]
test.py::TestAverageValueInList::test_AverageListsSame PASSED            [100%]

============================== 8 passed in 0.06s ==============================


## После написания команды "pylint AverageValueInList.py" в терминале был получен следующий отчет:

AverageValueInList.py:1:0: C0114: Missing module docstring (missing-module-docstring)
AverageValueInList.py:1:0: C0103: Module name "AverageValueInList" doesn't conform to snake_case naming style (invalid-name)
AverageValueInList.py:1:0: C0115: Missing class docstring (missing-class-docstring)
AverageValueInList.py:6:4: C0116: Missing function or method docstring (missing-function-docstring)
AverageValueInList.py:6:4: C0103: Method name "AverageList1" doesn't conform to snake_case naming style (invalid-name)
AverageValueInList.py:13:12: W0702: No exception type(s) specified (bare-except)
AverageValueInList.py:18:4: C0116: Missing function or method docstring (missing-function-docstring)
AverageValueInList.py:18:4: C0103: Method name "AverageList2" doesn't conform to snake_case naming style (invalid-name)
AverageValueInList.py:25:12: W0702: No exception type(s) specified (bare-except)
AverageValueInList.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
AverageValueInList.py:30:4: C0103: Method name "CompareTwoList" doesn't conform to snake_case naming style (invalid-name)
AverageValueInList.py:31:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)


## Таже самое было проделано и по отношению к тестам. Была введена команды "pylint test.py" и в результате был сформирован отчет:

test.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test.py:7:0: C0115: Missing class docstring (missing-class-docstring)
test.py:15:4: C0116: Missing function or method docstring (missing-function-docstring)
test.py:15:4: C0103: Method name "test_AverageList1" doesn't conform to snake_case naming style (invalid-name)
test.py:19:4: C0116: Missing function or method docstring (missing-function-docstring)
test.py:19:4: C0103: Method name "test_AverageList2" doesn't conform to snake_case naming style (invalid-name)
test.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
test.py:23:4: C0103: Method name "test_AverageList1STR" doesn't conform to snake_case naming style (invalid-name)
test.py:28:4: C0116: Missing function or method docstring (missing-function-docstring)
test.py:28:4: C0103: Method name "test_AverageList2Float" doesn't conform to snake_case naming style (invalid-name)
test.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
test.py:32:4: C0103: Method name "test_AverageList1Null" doesn't conform to snake_case naming style (invalid-name)
test.py:37:4: C0116: Missing function or method docstring (missing-function-docstring)
test.py:37:4: C0103: Method name "test_AverageListMore2" doesn't conform to snake_case naming style (invalid-name)
test.py:41:4: C0116: Missing function or method docstring (missing-function-docstring)
test.py:41:4: C0103: Method name "test_AverageListMore1" doesn't conform to snake_case naming style (invalid-name)
test.py:45:4: C0116: Missing function or method docstring (missing-function-docstring)
test.py:45:4: C0103: Method name "test_AverageListsSame" doesn't conform to snake_case naming style (invalid-name)
