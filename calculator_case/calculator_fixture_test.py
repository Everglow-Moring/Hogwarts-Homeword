"""
使用 试数据的数据驱动 方法完成加减乘除测试
"""
import pytest
from read_yaml import get_datas


class TestCal:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect", get_datas()["add_datas"], ids=get_datas()["my_addid"])
    def test_add(self, a, b, expect, calculator_fixture):
        print(f"加运算：{a} + {b} = {expect}")
        assert expect == calculator_fixture.add(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", get_datas()["sub_datas"], ids=get_datas()["my_subid"])
    def test_sub(self, a, b, expect, calculator_fixture):
        print(f"减运算：{a} - {b} = {expect}")
        assert expect == calculator_fixture.sub(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", get_datas()["mul_datas"], ids=get_datas()["my_mulid"])
    def test_mul(self, a, b, expect, calculator_fixture):
        print(f"乘运算：{a} * {b} = {expect}")
        assert expect == calculator_fixture.mul(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect", get_datas()["div_datas"], ids=get_datas()["my_divid"])
    def test_div(self, a, b, expect, calculator_fixture):
        print(f"除运算：{a} / {b} = {expect}")
        if b != 0:
            assert expect == calculator_fixture.div(a, b)
        else:
            print("除数不能为0")
