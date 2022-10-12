import unittest

import util


class UtilTest(unittest.TestCase):

    def test_print_frozenset(self):
        set_ = frozenset(['a', 'b', 'c', 'd','a'])
        util.str_frozenset(set_)
        self.assertTrue(True)
