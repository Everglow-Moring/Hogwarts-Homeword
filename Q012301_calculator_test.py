import pytest
from pythoncode.calculator import Calculator

class TestCal:
    def setup_class(self):
        self.calc = Calculator()
        print("开始测试计算：加、减、乘、除")

    def teardown_class(self):
        print("结束所有测试（加、减、乘、除）计算")

    def setup_method(self):
        print("开始一次测试")

    def teardown_method(self):
        print("结束一次测试\n")

    @pytest.mark.parametrize("a,b,expect",
                             [(0, 1, 1), (3, 5, 8), (-1, -1, -2), (1000, 1000, 2000)],
                             ids=["zero", "int", "mius", "bigint"])
    def test_add(self, a, b, expect):
        print(f"加运算：{a} + {b} = {expect}")
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             [(5, 0, 5), (2, 1, 1), (-5, -1, -4), (20000, 9999, 10001)],
                             ids=["zero", "int", "mius", "bigint"])
    def test_sub(self, a, b, expect):
        print(f"减运算：{a} - {b} = {expect}")
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             [(1, 0, 0), (1, 1, 1), (-1, -1, 1), (2021, 2000, 4042000)],
                             ids=["zero", "int", "mius", "bigint"])
    def test_mul(self, a, b, expect):
        print(f"乘运算：{a} * {b} = {expect}")
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             [(1, 0, 0), (0, 9, 0), (1, 1, 1), (-100, -2, 50), (10000, 100, 100)],
                             ids=["zero", "zero1", "int", "mius", "bigint"])
    def test_div(self, a, b, expect):
        print(f"除运算：{a} / {b} = {expect}")
        if b != 0:
            assert expect == self.calc.div(a, b)
        else:
            print("除数不能为0")
