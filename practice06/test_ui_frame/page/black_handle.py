def black_wrapper(func):
    # func = BasePage类中的有装饰器@black_wrapper的find方法
    def run_func(*args, **kwargs):
        base_page = args[0]

        try:
            return func(*args, **kwargs)
            # 捕获元素未找到的异常
        except Exception as e:
            # 遍历黑名单中的元素，并进行处理：点击
            for black in base_page.black_list:
                # python 解包
                elements = base_page.finds(*black)
                # 如果在黑名单中找到元素，则对黑名单中的元素进行操作。然后继续查找元素
                if len(elements) > 0:
                    # 对黑名单元素进行点击，可以扩展
                    elements[0].click()
                    return func(*args, **kwargs)
            raise e

    return run_func
