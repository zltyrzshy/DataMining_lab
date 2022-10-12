import util
from apriori import Apriori


def run_generate_big_rules(min_sup, min_conf):
    apriori = Apriori(util.load_data_set("../resource/out1w.csv"))

    apriori.generate_l(min_sup)

    apriori.generate_big_rule(min_conf)


run_generate_big_rules(0.001, 0.02)
