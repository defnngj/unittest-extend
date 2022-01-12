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


class MyTest(xtest.TestCase):

    def test_case(self):
        self.say_hello(self.get_name, 3)


if __name__ == '__main__':
    xtest.run()
```

## 运行:

直接通过python 运行测试文件。

```shell
> pytest test_sample.py

Hello Andy
Hello Andy
Hello Andy
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```
