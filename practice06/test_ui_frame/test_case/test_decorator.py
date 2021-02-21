"""
装饰器的使用
"""


# 方法一：
# def a():
#     print("a")


# def a():
#     print("a")
#     print("a1")
#     print("a2")
#
# def test():
#     a()

# 方法二：
# 封装、继承、多态、抽象 <-> 面向过程
# def b(a):
#     print("a1")
#     a()
#     print("a2")


# def a():
#     print("a")
#


# def test():
#     b(a)


# 方法三：
def c(function_name_01):
    # fun = a
    # *args, **kwargs)：这两种可以代表一切的数据格式
    def function_name(*args, **kwargs):
        print("a1")
        function_name_01(*args, **kwargs)
        print("a2")

    return function_name


def d(function_name_01):
    # fun = a
    # *args, **kwargs)：这两种可以代表一切的数据格式
    def function_name(*args, **kwargs):
        print("d1")
        function_name_01(*args, **kwargs)
        print("d2")

    return function_name


@d
@c
def a():
    print("a")


def test():
    a()



