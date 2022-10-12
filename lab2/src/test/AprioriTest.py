import unittest
from datetime import datetime

import util
from apriori import Apriori

data_set = [['l1', 'l2', 'l5'], ['l2', 'l4'], ['l2', 'l3'],
            ['l1', 'l2', 'l4'], ['l1', 'l3'], ['l2', 'l3'],
            ['l1', 'l3'], ['l1', 'l2', 'l3', 'l5'], ['l1', 'l2', 'l3']]


class AprioriTest(unittest.TestCase):

    def test_generate_big_rules(self):
        apriori = Apriori(data_set)

        apriori.generate_l(min_sup=0.4)
        apriori.print_freq_item_sets()

        apriori.generate_big_rule(min_conf=0.6)
        apriori.str_big_rule_list()

        self.assertTrue(True)

    def test_generate_l(self):
        apriori = Apriori(util.load_data_set())

        apriori.generate_l(min_sup=0.05)

        apriori.print_freq_item_sets()
        self.assertTrue(True)
