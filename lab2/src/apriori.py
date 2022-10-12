import logging
import util

logging.basicConfig(filename='../log/apriori.log', encoding='utf-8', filemode='w',
                    level=logging.INFO, format='%(levelname)s:\t%(asctime)s %(message)s', datefmt='%I:%M:%S')


class Apriori:

    def __init__(self, data_set: list[list]):
        """
        :param data_set:;
        Args:
            data_set: A list of transactions. Each transaction contains several items.
            support_data: A dictionary. The key is frequent item_set and the value is support.
            big_rule_list:A list which contains all big rules. Each big rule is represented as a 3-tuple.
        """
        self.data_set = data_set
        self.support_data = {}
        self.freq_item_sets = []
        self.big_rule_list = []
        self.t_num = float(len(self.data_set))

    def __create_c1(self) -> set:
        """
        Create frequent candidate 1-item_set C1 by scanning data set.
        Returns:
            c1: A set which contains all frequent candidate 1-item_sets
        """
        c1 = set()
        for t in self.data_set:  # 遍历每一行
            for item in t:  # 遍历每一个值
                item_set = frozenset([item])  # frozenset返回一个冻结集合
                c1.add(item_set)

        logging.info('create_c1 over\n')
        return c1

    @classmethod
    def __is_apriori(cls, ck_item, lk_sub1):
        """
        Judge whether a frequent candidate k-item_set satisfy Apriori property.
        Args:
            ck_item: a frequent candidate k-item_set in Ck which contains all frequent candidate k-item_sets.
            lk_sub1: Lk-1, a set which contains all frequent candidate (k-1)-item_sets.
        Returns:
            True: satisfying Apriori property.
            False: Not satisfying Apriori property.
        """
        for item in ck_item:
            sub_ck = ck_item - frozenset([item])
            if sub_ck not in lk_sub1:
                return False
        return True

    def __create_ck(self, lk_sub1, k):
        """
        Create ck, a set which contains all frequent candidate k-item_sets
        by Lk-1's own connection operation.
        Args:
            lk_sub1: Lk-1, a set which contains all frequent candidate (k-1)-item_sets.
            k: the item number of a frequent item_set.
        Return:
            ck: a set which contains all frequent candidate k-item_sets.
        """
        ck = set()
        len_lk_sub1 = len(lk_sub1)
        list_lk_sub1 = list(lk_sub1)
        for i in range(len_lk_sub1):
            for j in range(1, len_lk_sub1):
                l1 = list(list_lk_sub1[i])
                l2 = list(list_lk_sub1[j])
                l1.sort()
                l2.sort()
                if l1[0:k - 2] == l2[0:k - 2]:
                    ck_item = list_lk_sub1[i] | list_lk_sub1[j]
                    if self.__is_apriori(ck_item, lk_sub1):
                        ck.add(ck_item)

        logging.info('create_c{} over\n'.format(k))
        return ck

    def __generate_lk_by_ck(self, ck, min_sup):
        """
        Generate lk by executing a delete-policy from ck.
        Args:
            ck: A set which contains all frequent candidate k-item_sets.
            min_sup: The minimum support.
        Returns:
            lk: A set which contains all frequent k-item_sets.
        """
        logging.info('generate_lk_by_ck start\n')

        lk = set()
        item_count = {}
        for i, t in enumerate(self.data_set, 1):
            if i % 1000 == 0:
                logging.debug('scan {}data_set over'.format(i))
            for item in ck:
                if item.issubset(t):
                    if item not in item_count:
                        item_count[item] = 1
                    else:
                        item_count[item] += 1

        logging.info('generate_lk_by_ck item_count over\n')

        for item in item_count:
            item_support = item_count[item] / self.t_num  # 计算support
            if item_support >= min_sup:
                lk.add(item)
                self.support_data[item] = item_support
                logging.debug('{}\t{}'.format(util.str_frozenset(item), item_support))

        logging.info('generate_lk_by_ck over\n')
        return lk

    def generate_l(self, min_sup):
        """
        Generate all frequent item_sets.
        Args:
            self.data_set: A list of transactions. Each transaction contains several items.
            k: Maximum number of items for all frequent item_sets.
            min_sup: The minimum support.
        Returns:
            L: The list of Lk.
            support_data: A dictionary. The key is frequent item_set and the value is support.
        """
        c1 = self.__create_c1()
        l1 = self.__generate_lk_by_ck(c1, min_sup)

        ld_sub1 = l1.copy()
        for lk_i in ld_sub1:
            self.freq_item_sets.append(lk_i)
        i = 2

        logging.info('k=1 over\n')

        while True:
            ci = self.__create_ck(ld_sub1, i)
            li = self.__generate_lk_by_ck(ci, min_sup)
            ld_sub1 = li.copy()

            if len(ld_sub1) == 0:
                break
            for lk_i in ld_sub1:
                self.freq_item_sets.append(lk_i)

            logging.info('k=%d over\n', i)
            i += 1

        logging.info('generate_l over\n')

    def generate_big_rule(self, min_conf):
        """
        Generate big rules from frequent item_sets.
        :param min_conf: Minimal confidence.
        """
        sub_set_list = []
        for freq_set in self.freq_item_sets:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    conf = self.support_data[freq_set] / self.support_data[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= min_conf and big_rule not in self.big_rule_list:
                        self.big_rule_list.append(big_rule)

            sub_set_list.append(freq_set)

        logging.info('generate_big_rule over\n')

        logging.info(self.str_freq_item_sets())
        logging.info(self.str_big_rule_list())

    def str_freq_item_sets(self) -> str:
        res = "item_sets of {}:\t\tsupport\n".format(len(self.freq_item_sets))
        for freq_set in self.freq_item_sets:
            res += '{}\t{}\n'.format(util.str_frozenset(freq_set), self.support_data[freq_set])
        return res

    def str_big_rule_list(self) -> str:
        res = "Big Rules of {}:\n".format(len(self.big_rule_list))
        for item in self.big_rule_list:
            res += '{}=>{}\tconf:\t{}\n'.format(util.str_frozenset(item[0]), util.str_frozenset(item[1]), item[2])
        return res
