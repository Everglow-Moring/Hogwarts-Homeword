import pytest
from pythoncode.calculator import Calculator


@pytest.fixture(scope="module")
def calculator_fixture():
    calc = Calculator()
    print("开始计算")
    yield calc
    print("计算结束")
