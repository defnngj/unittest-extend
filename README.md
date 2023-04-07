# unittest-extend

## 安装

* 下载安装

```shell script
> git clone https://github.com/defnngj/unittest-extend
> cd unittest-extend
> python setup.py install
```

* pip在线安装

```shell
> pip install -U https://github.com/defnngj/unittest-extend.git@master
```


## 用法

`test_sample.py` 用例：

```python
import xtest
from selenium import webdriver


class MyTest(xtest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.name = self.get_name

    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        self.driver.get("https://www.baidu.com/")
        search_input = self.driver.find_element("id", "kw")
        search_input.send_keys(self.name)
        search_input.submit()
        self.sleep(2)
        result_title = self.driver.find_elements("css selector", "div > h3.c-title > a")
        for title in result_title:
            self.assert_in_text(self.name, title.text)


if __name__ == '__main__':
    xtest.run()
```

## 运行:

直接通过python 运行测试文件。

```shell
> pytest test_sample.py

.
----------------------------------------------------------------------
Ran 1 test in 10.281s

OK
```
