# zc-cris
import unittest

from func_name import name_handle


class NamesTestCase(unittest.TestCase):
    '''单元测试'''

    def test_first_last_name(self):
        full_name = name_handle('lebron', 'james')
        self.assertEqual(full_name, 'Lebron James')

    def test_first_middle_last_name(self):
        full_name = name_handle("james", 'cris', 'harden')
        self.assertEqual(full_name, 'James Harden Cris')
