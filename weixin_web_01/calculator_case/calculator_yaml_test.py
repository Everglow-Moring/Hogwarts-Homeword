"""
使用 试数据的数据驱动 方法完成加减乘除测试
"""
import pytest
import yaml
from pythoncode.calculator import Calculator


def get_datas():
    with open("calculator_data.yml") as f:
        datas = yaml.safe_load(f)
        return datas


class TestCal:
    def setup_class(self):
        self.calc = Calculator()
        print("开始测试：加、减、乘、除")

    def teardown_class(self):
        print("加、减、乘、除 的测试结束")

    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("计算结束\n")

    @pytest.mark.parametrize("a,b,expect", get_datas()["add_datas"], ids=get_datas()["my_addid"])
    def test_add(self, a, b, expect):
        print(f"加运算：{a} + {b} = {expect}")
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", get_datas()["sub_datas"], ids=get_datas()["my_subid"])
    def test_sub(self, a, b, expect):
        print(f"减运算：{a} - {b} = {expect}")
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", get_datas()["mul_datas"], ids=get_datas()["my_mulid"])
    def test_mul(self, a, b, expect):
        print(f"乘运算：{a} * {b} = {expect}")
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", get_datas()["div_datas"], ids=get_datas()["my_divid"])
    def test_div(self, a, b, expect):
        print(f"除运算：{a} / {b} = {expect}")
        if b != 0:
            assert expect == self.calc.div(a, b)
        else:
            print("除数不能为0")
