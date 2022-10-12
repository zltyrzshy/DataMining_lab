import logging

import util
from efficient_apriori import apriori

logging.basicConfig(filename='../log/apriori2.log', encoding='utf-8', filemode='w',
                    level=logging.DEBUG, format='%(levelname)s: %(asctime)s %(message)s', datefmt='%I:%M:%S')

item_sets, rules = apriori(util.load_data_set('../resource/out1w.csv'), 0.001, 0.02)

logging.info('item_sets: \n{}'.format(util.str_dict_iter(item_sets)))
logging.info('rules of {}: \n{}'.format(len(rules), util.str_iter(rules)))
