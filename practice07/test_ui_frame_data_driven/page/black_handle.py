import logging
import allure


logging.basicConfig(level=logging.DEBUG)


def black_wrapper(func):
    # func = BasePage类中的有装饰器@black_wrapper的find方法
    # run_func这个内置函数，发现func有值便会执行
    def run_func(*args, **kwargs):
        base_page = args[0]
        try:
            # 这样写完了之后，tesecase运行成功了，但是没有打印日志
            logging.info("start find: \nargs: " + str(args) + "kwargs: " + str(kwargs))
            # 此func就是传进来的函数：BasePage类中的有装饰器@black_wrapper的find方法
            return func(*args, **kwargs)
            # 捕获元素未找到的异常
        except Exception as e:
            base_page.screen_shot("error_picture.png")
            # 图片在本地，所以需要加载    这个图片会存储在allure里面
            with open("error_picture.png", "rb") as f:
                error_picture = f.read()
            allure.attach(error_picture, attachment_type=allure.attachment_type.PNG)

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
