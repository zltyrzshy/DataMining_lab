# Report_association rule

学号:3020244350
姓名:张文浩
班级:软件工程2班

概要：使用python实现，并且有调用efficient_apriori库和不调用库两种方法。自己实现的极慢，调用库要快很多。

## 目标

练习使用关联规则Apriori算法。完成以下两个任务，并与作业里手动计算的结果进行对比分析。

## 数据

课堂收集的选课的真实数据和DBLP数据集

## 任务1

选择以下数据进行关联规则的抽取

| 食物1 | 食物2  | 食物3 | 食物4    | 食物5  | 食物6 |
| ----- | ------ | ----- | -------- | ------ | ----- |
| 泡面  | 面包   | 饮料  | 银耳羹   | 水     |       |
| 泡面  | 水     | 蛋糕  | 蔬菜水果 |        |       |
| 泡面  | 巧克力 | 面包  | 水       | 肉制品 | 辣条  |
| 泡面  | 水     | 面包  | 巧克力   | 牛奶   |       |
| 泡面  | 水     | 面包  |          |        |       |

执行Apriori算法，记录算法设置和结果，要求：

### 1 算法过程

给出算法过程，记录参数设置。

#### 1.1 查询频繁项集

##### 1.1.1 产生c1

```python
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
```

##### 1.1.2 产生ck

```python
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
```

##### 1.1.3 产生lk

```python
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
```

#### 1.2 查询关联规则

```python
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
```

### 2 分析结果

分析结果，找出不同频繁项数量（2-4）的关联规则结果。并给出相应的算法设置。

```python
min_sup: 0.4, min_conf: 0.6

item_sets of 15:		support
{'巧克力'}	0.4
{'面包'}	0.8
{'水'}	1.0
{'泡面'}	1.0
{'水', '泡面'}	1.0
{'面包', '巧克力'}	0.4
{'水', '面包'}	0.8
{'泡面', '巧克力'}	0.4
{'面包', '泡面'}	0.8
{'水', '巧克力'}	0.4
{'面包', '泡面', '巧克力'}	0.4
{'水', '泡面', '巧克力'}	0.4
{'水', '面包', '泡面'}	0.8
{'水', '面包', '巧克力'}	0.4
{'水', '面包', '泡面', '巧克力'}	0.4

Big Rules of 31:
{'泡面'}=>{'水'}	conf:	1.0
{'水'}=>{'泡面'}	conf:	1.0
{'巧克力'}=>{'面包'}	conf:	1.0
{'水'}=>{'面包'}	conf:	0.8
{'面包'}=>{'水'}	conf:	1.0
{'巧克力'}=>{'泡面'}	conf:	1.0
{'泡面'}=>{'面包'}	conf:	0.8
{'面包'}=>{'泡面'}	conf:	1.0
{'巧克力'}=>{'水'}	conf:	1.0
{'泡面', '巧克力'}=>{'面包'}	conf:	1.0
{'面包', '巧克力'}=>{'泡面'}	conf:	1.0
{'巧克力'}=>{'面包', '泡面'}	conf:	1.0
{'泡面', '巧克力'}=>{'水'}	conf:	1.0
{'水', '巧克力'}=>{'泡面'}	conf:	1.0
{'巧克力'}=>{'水', '泡面'}	conf:	1.0
{'水', '泡面'}=>{'面包'}	conf:	0.8
{'面包', '泡面'}=>{'水'}	conf:	1.0
{'水', '面包'}=>{'泡面'}	conf:	1.0
{'面包'}=>{'水', '泡面'}	conf:	1.0
{'泡面'}=>{'水', '面包'}	conf:	0.8
{'水'}=>{'面包', '泡面'}	conf:	0.8
{'水', '巧克力'}=>{'面包'}	conf:	1.0
{'面包', '巧克力'}=>{'水'}	conf:	1.0
{'巧克力'}=>{'水', '面包'}	conf:	1.0
{'水', '泡面', '巧克力'}=>{'面包'}	conf:	1.0
{'面包', '泡面', '巧克力'}=>{'水'}	conf:	1.0
{'水', '面包', '巧克力'}=>{'泡面'}	conf:	1.0
{'面包', '巧克力'}=>{'水', '泡面'}	conf:	1.0
{'泡面', '巧克力'}=>{'水', '面包'}	conf:	1.0
{'水', '巧克力'}=>{'面包', '泡面'}	conf:	1.0
{'巧克力'}=>{'水', '面包', '泡面'}	conf:	1.0
```

```python
min_sup: 0.6, min_conf: 0.8

item_sets of 7:		support
{'面包'}	0.8
{'水'}	1.0
{'泡面'}	1.0
{'面包', '水'}	0.8
{'泡面', '水'}	1.0
{'泡面', '面包'}	0.8
{'泡面', '面包', '水'}	0.8

Big Rules of 12:
{'水'}=>{'面包'}	conf:	0.8
{'面包'}=>{'水'}	conf:	1.0
{'泡面'}=>{'水'}	conf:	1.0
{'水'}=>{'泡面'}	conf:	1.0
{'泡面'}=>{'面包'}	conf:	0.8
{'面包'}=>{'泡面'}	conf:	1.0
{'泡面', '水'}=>{'面包'}	conf:	0.8
{'泡面', '面包'}=>{'水'}	conf:	1.0
{'面包', '水'}=>{'泡面'}	conf:	1.0
{'泡面'}=>{'面包', '水'}	conf:	0.8
{'面包'}=>{'泡面', '水'}	conf:	1.0
{'水'}=>{'泡面', '面包'}	conf:	0.8
```

### 3 分析

要求给出重要的算法，过程截图，和必要的文字分析。

采用了迭代的方法，先搜索出候选1项集及对应的支持度，剪枝去掉低于支持度的1项集，得到频繁1项集。然后对剩下的频繁1项集进行连接，得到候选的频繁2项集，筛选去掉低于支持度的候选频繁2项集，得到真正的频繁二项集。以此类推，迭代下去，直到无法找到频繁k+1项集为止，对应的频繁k项集的集合即为算法的输出结果。

## 任务2

使用DBLP数据集，提出一种方法，挖掘密切相关的（即经常一起合写文章）合著者关系。

```python
min_sup=0.001, min_conf=0.02
item_sets: 
1 #省略

2
('AlexanderKaplan', 'RainerTichatschke')
('AlfredMenezes', 'DarrelHankerson')
('AnnaSlobodov', 'ChristophMeinel')
('ChristophMeinel', 'HaraldSack')
('HenryLin', 'XiaoboZhou')
('JianFeng', 'Kwok-TungLo')
('JiaweiHan0001', 'XinJin0001')
('MarkS.Drew', 'RajeevRamanath')
('PeterGritzmann', 'VictorKlee')


rules of 18: 
{RainerTichatschke} -> {AlexanderKaplan} (conf: 0.846, supp: 0.001, lift: 769.231, conv: 6.493)
{AlexanderKaplan} -> {RainerTichatschke} (conf: 1.000, supp: 0.001, lift: 769.231, conv: 998700000.000)
{DarrelHankerson} -> {AlfredMenezes} (conf: 1.000, supp: 0.002, lift: 454.545, conv: 997800000.000)
{AlfredMenezes} -> {DarrelHankerson} (conf: 1.000, supp: 0.002, lift: 454.545, conv: 997800000.000)
{ChristophMeinel} -> {AnnaSlobodov} (conf: 0.204, supp: 0.001, lift: 185.185, conv: 1.254)
{AnnaSlobodov} -> {ChristophMeinel} (conf: 1.000, supp: 0.001, lift: 185.185, conv: 994600000.000)
{HaraldSack} -> {ChristophMeinel} (conf: 0.909, supp: 0.001, lift: 168.350, conv: 10.941)
{ChristophMeinel} -> {HaraldSack} (conf: 0.185, supp: 0.001, lift: 168.350, conv: 1.226)
{XiaoboZhou} -> {HenryLin} (conf: 1.000, supp: 0.002, lift: 625.000, conv: 998400000.000)
{HenryLin} -> {XiaoboZhou} (conf: 1.000, supp: 0.002, lift: 625.000, conv: 998400000.000)
{Kwok-TungLo} -> {JianFeng} (conf: 1.000, supp: 0.001, lift: 1000.000, conv: 999000000.000)
{JianFeng} -> {Kwok-TungLo} (conf: 1.000, supp: 0.001, lift: 1000.000, conv: 999000000.000)
{XinJin0001} -> {JiaweiHan0001} (conf: 1.000, supp: 0.002, lift: 526.316, conv: 998100000.000)
{JiaweiHan0001} -> {XinJin0001} (conf: 0.842, supp: 0.002, lift: 526.316, conv: 6.323)
{RajeevRamanath} -> {MarkS.Drew} (conf: 1.000, supp: 0.001, lift: 1000.000, conv: 999000000.000)
{MarkS.Drew} -> {RajeevRamanath} (conf: 1.000, supp: 0.001, lift: 1000.000, conv: 999000000.000)
{VictorKlee} -> {PeterGritzmann} (conf: 1.000, supp: 0.001, lift: 555.556, conv: 998200000.000)
{PeterGritzmann} -> {VictorKlee} (conf: 0.611, supp: 0.001, lift: 555.556, conv: 2.569)
```

##  与手写作业对比

 任务1与手写作业相同