import time
import random
import unittest


class TestCase(unittest.TestCase):
    """
    unittest 扩展类
    """

    @property
    def get_name(self) -> str:
        """
        随机返回一个英文名
        """
        name_list = ["Andy", "Bill", "Jack", "Robert", "Ada", "Jane", "Eva", "Anne"]
        choice_name = random.choice(name_list)
        return choice_name

    @staticmethod
    def sleep(sec: int = 1) -> None:
        """
        休眠时间
        sec: 秒
        """
        time.sleep(sec)

    def assert_in_text(self, string: str, text: str) -> None:
        """
        将字符串转为小写，断言包含
        :param string: 字符串
        :param text: 文本
        """
        self.assertIn(string.lower(), text.lower())


def run(verbosity=1):
    """
    调用 unittest.main() 方法
    """
    unittest.main(verbosity=verbosity)
