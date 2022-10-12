import unittest
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

import util
from apriori import Apriori
from fpgrowth import FPGrowth


class Test(unittest.TestCase):

    def test_apriori(self):
        self.assertTrue(True)
        Test.run_apriori()

    @classmethod
    def run_apriori(cls, data_set=util.load_data_set(), min_sup=0.05):
        start = datetime.now()

        apriori = Apriori(data_set)
        apriori.generate_l(min_sup=min_sup)

        delta_time = datetime.now() - start
        print("Apriori over")
        return delta_time.seconds + delta_time.microseconds / 1000000
        # print("# of freq item_sets:", len(apriori.freq_item_sets))
        # print(apriori.freq_item_sets)

    @classmethod
    def run_generate_l(cls, data_set=util.load_data_set(), min_sup=0.05) -> Apriori:
        apriori = Apriori(data_set)
        apriori.generate_l(min_sup=min_sup)

        print('generate_l over')
        return apriori
        # print("# of freq item_sets:", len(apriori.freq_item_sets))
        # print(apriori.freq_item_sets)

    def test_fpgrowth(self):
        Test.run_apriori()
        self.assertTrue(True)

    @classmethod
    def run_fpgrowth(cls, data_set=util.load_data_set(), min_sup=0.05):
        start = datetime.now()

        fp = FPGrowth(data_set, min_sup=0.05)
        fp.build_fp_tree()

        delta_time = datetime.now() - start
        print("FP-Growth over")
        # print("# of freq item_sets:", len(fp.freq_item_sets))

        return delta_time.seconds + delta_time.microseconds / 1000000

    def test_ntrans(self):
        data_folder = "./data/ntrans/"
        ntrans_range = range(1, 21, 1)
        time_apriori = []
        time_fpgrowth = []

        for ntrans in ntrans_range:
            fname = str(ntrans) + ".data"
            print(fname)
            data_set = util.data_reader(data_folder + fname)

            time_apriori.append(self.run_apriori(data_set))

            time_fpgrowth.append(self.run_fpgrowth(data_set))

        print(time_apriori)
        print(time_fpgrowth)
        plt.plot(ntrans_range, time_apriori, label="Apriori")
        plt.plot(ntrans_range, time_fpgrowth, label="FP-Growth")
        plt.xlabel("ntrans (k)")
        plt.ylabel("time (s)")
        plt.legend()
        plt.show()

    def test_tlen(self):
        data_folder = "./data/tlen/"
        tlen_range = range(1, 21, 1)
        time_apriori = []
        time_fpgrowth = []

        for tlen in tlen_range:
            fname = str(tlen) + ".data"
            print(fname)
            data_set = util.data_reader(data_folder + fname)

            time_apriori.append(self.run_apriori(data_set))

            time_fpgrowth.append(self.run_fpgrowth(data_set))

        print(time_apriori)
        print(time_fpgrowth)
        plt.plot(tlen_range, time_apriori, label="Apriori")
        plt.plot(tlen_range, time_fpgrowth, label="FP-Growth")
        plt.xlabel("tlen")
        plt.ylabel("time (s)")
        plt.legend()
        plt.show()

    def test_nitems(self):
        data_folder = "./data/nitems/"
        nitems_range = list(np.arange(0.1, 2.1, 0.1))
        time_apriori = []
        time_fpgrowth = []

        for nitems in nitems_range:
            fname = str(nitems) + ".data"
            print(fname)
            data_set = util.data_reader(data_folder + fname)

            time_apriori.append(self.run_apriori(data_set))

            time_fpgrowth.append(self.run_fpgrowth(data_set))

        print(time_apriori)
        print(time_fpgrowth)
        plt.plot(nitems_range, time_apriori, label="Apriori")
        plt.plot(nitems_range, time_fpgrowth, label="FP-Growth")
        plt.xlabel("nitems (k)")
        plt.ylabel("time (s)")
        plt.legend()
        plt.show()

    def test_min_sup(self):
        data_file = "./data/base_set.data"
        data_set = util.data_reader(data_file)
        min_sup = list(np.arange(0.01, 0.21, 0.01))
        time_apriori = []
        time_fpgrowth = []

        for min_sup in min_sup:
            time_apriori.append(self.run_apriori(data_set, min_sup=min_sup))
            time_fpgrowth.append(self.run_fpgrowth(data_set, min_sup=min_sup))

        print(time_apriori)
        print(time_fpgrowth)
        plt.plot(min_sup, time_apriori, label="Apriori")
        plt.plot(min_sup, time_fpgrowth, label="FP-Growth")
        plt.xlabel("min_sup")
        plt.ylabel("time (s)")
        plt.legend()
        plt.show()

    def test_base(self):
        data_file = "./data/base_set.data"
        data_set = util.data_reader(data_file)
        # data_set = load_data_set()
        # print("Apriori-----------------------")
        # print("Time (s):", test_apriori(data_set))

        print("FP-Growth-----------------------")
        print("Time (s):", self.run_fpgrowth(data_set))


if __name__ == '__main__':
    unittest.main()
