from unittest import TestCase

from func_name import name_handle


# 利用 pycharm 提供的goto 快速进行单元测试
# zc-cris
class TestName_handle(TestCase):
    def test_name_handle(self):
        full_name = name_handle('lebron', 'james')
        self.assertEqual(full_name, 'Lebron James')
