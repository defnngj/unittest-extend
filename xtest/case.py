import unittest
import random


class TestCase(unittest.TestCase):
    """
    扩展unittest 的方法
    """

    @staticmethod
    def say_hello(name: str, times: int = 1) -> None:
        """
        打招呼
        :param name: 名字
        :param times: 次数
        :return:
        """
        if times < 1:
            return
        for _ in range(times):
            print(f'Hello {name}')

    @property
    def get_name(self) -> str:
        """
        随机返回一个名字
        :return:
        """
        name_list = ["Andy", "Bill", "Jack", "Robert", "Ada", "Jane", "Eva", "Anne"]
        choice_name = random.choice(name_list)
        return choice_name


def run(verbosity=1):
    """
    运行用例方法
    """
    unittest.main(verbosity=verbosity)
