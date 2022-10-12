# report_association rule_hand

3020244350_张文浩

## 囤货表：男生

| 食物1 | 食物2  | 食物3 | 食物4    | 食物5  | 食物6 |
| ----- | ------ | ----- | -------- | ------ | ----- |
| 泡面  | 面包   | 饮料  | 银耳羹   | 水     |       |
| 泡面  | 水     | 蛋糕  | 蔬菜水果 |        |       |
| 泡面  | 巧克力 | 面包  | 水       | 肉制品 | 辣条  |
| 泡面  | 水     | 面包  | 巧克力   | 牛奶   |       |
| 泡面  | 水     | 面包  |          |        |       |

## min_sup: 0.4 min_conf 0.6
### 查询平凡项集
#### k=1
{'巧克力'} 	 0.4
{'面包'} 	 0.8
{'水'} 	 1.0
{'泡面'} 	 1.0
#### k= 2
{'水', '巧克力'} 	 0.4
{'面包', '巧克力'} 	 0.4
{'水', '面包'} 	 0.8
{'水', '泡面'} 	 1.0
{'泡面', '面包'} 	 0.8
{'泡面', '巧克力'} 	 0.4
#### k= 3
{'水', '泡面', '巧克力'} 	 0.4
{'面包', '泡面', '巧克力'} 	 0.4
{'水', '泡面', '面包'} 	 0.8
{'面包', '水', '巧克力'} 	 0.4
#### k= 4
{'巧克力', '面包', '水', '泡面'} 	 0.4
### 获得关联规则
#####  {'水', '巧克力'}
no:		{'水', '巧克力'}=>{'巧克力'}	conf: 0.4	lift: 1.0
yes:	{'水', '巧克力'}=>{'水'}	conf: 1.0	lift: 1.0
#####  {'面包', '巧克力'}
no:		{'面包', '巧克力'}=>{'巧克力'}	conf: 0.5	lift: 1.25
yes:	{'面包', '巧克力'}=>{'面包'}	conf: 1.0	lift: 1.25
#####  {'水', '面包'}
yes:	{'水', '面包'}=>{'面包'}	conf: 0.8	lift: 1.0
yes:	{'水', '面包'}=>{'水'}	conf: 1.0	lift: 1.0
#####  {'水', '泡面'}
yes:	{'水', '泡面'}=>{'水'}	conf: 1.0	lift: 1.0
yes:	{'水', '泡面'}=>{'泡面'}	conf: 1.0	lift: 1.0
#####  {'泡面', '面包'}
yes:	{'泡面', '面包'}=>{'面包'}	conf: 0.8	lift: 1.0
yes:	{'泡面', '面包'}=>{'泡面'}	conf: 1.0	lift: 1.0
#####  {'泡面', '巧克力'}
no:		{'泡面', '巧克力'}=>{'巧克力'}	conf: 0.4	lift: 1.0
yes:	{'泡面', '巧克力'}=>{'泡面'}	conf: 1.0	lift: 1.0
#####  {'水', '泡面', '巧克力'}
no:		{'水', '泡面', '巧克力'}=>{'巧克力'}	conf: 0.4	lift: 1.0
yes:	{'水', '泡面', '巧克力'}=>{'水'}	conf: 1.0	lift: 1.0
yes:	{'水', '泡面', '巧克力'}=>{'泡面'}	conf: 1.0	lift: 1.0
no:		{'水', '泡面', '巧克力'}=>{'水', '巧克力'}	conf: 0.4	lift: 1.0
yes:	{'水', '泡面', '巧克力'}=>{'水', '泡面'}	conf: 1.0	lift: 1.0
no:		{'水', '泡面', '巧克力'}=>{'泡面', '巧克力'}	conf: 0.4	lift: 1.0
#####  {'面包', '泡面', '巧克力'}
no:		{'面包', '泡面', '巧克力'}=>{'巧克力'}	conf: 0.5	lift: 1.25
yes:	{'面包', '泡面', '巧克力'}=>{'面包'}	conf: 1.0	lift: 1.25
yes:	{'面包', '泡面', '巧克力'}=>{'泡面'}	conf: 1.0	lift: 1.0
no:		{'面包', '泡面', '巧克力'}=>{'面包', '巧克力'}	conf: 0.4	lift: 1.0
yes:	{'面包', '泡面', '巧克力'}=>{'泡面', '面包'}	conf: 1.0	lift: 1.25
no:		{'面包', '泡面', '巧克力'}=>{'泡面', '巧克力'}	conf: 0.5	lift: 1.25
#####  {'水', '泡面', '面包'}
yes:	{'水', '泡面', '面包'}=>{'面包'}	conf: 0.8	lift: 1.0
yes:	{'水', '泡面', '面包'}=>{'水'}	conf: 1.0	lift: 1.0
yes:	{'水', '泡面', '面包'}=>{'泡面'}	conf: 1.0	lift: 1.0
yes:	{'水', '泡面', '面包'}=>{'水', '面包'}	conf: 0.8	lift: 1.0
yes:	{'水', '泡面', '面包'}=>{'水', '泡面'}	conf: 1.0	lift: 1.0
yes:	{'水', '泡面', '面包'}=>{'泡面', '面包'}	conf: 0.8	lift: 1.0
#####  {'面包', '水', '巧克力'}
no:		{'面包', '水', '巧克力'}=>{'巧克力'}	conf: 0.5	lift: 1.25
yes:	{'面包', '水', '巧克力'}=>{'面包'}	conf: 1.0	lift: 1.25
yes:	{'面包', '水', '巧克力'}=>{'水'}	conf: 1.0	lift: 1.0
no:		{'面包', '水', '巧克力'}=>{'水', '巧克力'}	conf: 0.5	lift: 1.25
no:		{'面包', '水', '巧克力'}=>{'面包', '巧克力'}	conf: 0.4	lift: 1.0
yes:	{'面包', '水', '巧克力'}=>{'水', '面包'}	conf: 1.0	lift: 1.25
#####  {'巧克力', '面包', '水', '泡面'}
no:		{'巧克力', '面包', '水', '泡面'}=>{'巧克力'}	conf: 0.5	lift: 1.25
yes:	{'巧克力', '面包', '水', '泡面'}=>{'面包'}	conf: 1.0	lift: 1.25
yes:	{'巧克力', '面包', '水', '泡面'}=>{'水'}	conf: 1.0	lift: 1.0
yes:	{'巧克力', '面包', '水', '泡面'}=>{'泡面'}	conf: 1.0	lift: 1.0
no:		{'巧克力', '面包', '水', '泡面'}=>{'水', '巧克力'}	conf: 0.5	lift: 1.25
no:		{'巧克力', '面包', '水', '泡面'}=>{'面包', '巧克力'}	conf: 0.4	lift: 1.0
yes:	{'巧克力', '面包', '水', '泡面'}=>{'水', '面包'}	conf: 1.0	lift: 1.25
yes:	{'巧克力', '面包', '水', '泡面'}=>{'水', '泡面'}	conf: 1.0	lift: 1.0
yes:	{'巧克力', '面包', '水', '泡面'}=>{'泡面', '面包'}	conf: 1.0	lift: 1.25
no:		{'巧克力', '面包', '水', '泡面'}=>{'泡面', '巧克力'}	conf: 0.5	lift: 1.25
no:		{'巧克力', '面包', '水', '泡面'}=>{'水', '泡面', '巧克力'}	conf: 0.5	lift: 1.25
no:		{'巧克力', '面包', '水', '泡面'}=>{'面包', '泡面', '巧克力'}	conf: 0.4	lift: 1.0
yes:	{'巧克力', '面包', '水', '泡面'}=>{'水', '泡面', '面包'}	conf: 1.0	lift: 1.25
no:		{'巧克力', '面包', '水', '泡面'}=>{'面包', '水', '巧克力'}	conf: 0.4	lift: 1.0

## min_sup: 0.6 min_conf 0.8
### 查询平凡项集
#### k=1
{'水'} 	 1.0
{'巧克力'} 	 0.4
{'面包'} 	 0.8
{'泡面'} 	 1.0
#### k= 2
{'巧克力', '水'} 	 0.4
{'泡面', '水'} 	 1.0
{'面包', '巧克力'} 	 0.4
{'面包', '泡面'} 	 0.8
{'面包', '水'} 	 0.8
{'泡面', '巧克力'} 	 0.4
#### k= 3
{'面包', '泡面', '巧克力'} 	 0.4
{'面包', '巧克力', '水'} 	 0.4
{'面包', '泡面', '水'} 	 0.8
{'泡面', '巧克力', '水'} 	 0.4
#### k= 4
{'面包', '泡面', '水', '巧克力'} 	 0.4
### 获得关联规则
#####  {'巧克力', '水'}
yes:	{'巧克力', '水'}=>{'水'}	conf: 1.0	lift: 1.0
no:		{'巧克力', '水'}=>{'巧克力'}	conf: 0.4	lift: 1.0
#####  {'泡面', '水'}
yes:	{'泡面', '水'}=>{'水'}	conf: 1.0	lift: 1.0
yes:	{'泡面', '水'}=>{'泡面'}	conf: 1.0	lift: 1.0
#####  {'面包', '巧克力'}
no:		{'面包', '巧克力'}=>{'巧克力'}	conf: 0.5	lift: 1.25
yes:	{'面包', '巧克力'}=>{'面包'}	conf: 1.0	lift: 1.25
#####  {'面包', '泡面'}
yes:	{'面包', '泡面'}=>{'面包'}	conf: 0.8	lift: 1.0
yes:	{'面包', '泡面'}=>{'泡面'}	conf: 1.0	lift: 1.0
#####  {'面包', '水'}
yes:	{'面包', '水'}=>{'水'}	conf: 1.0	lift: 1.0
yes:	{'面包', '水'}=>{'面包'}	conf: 0.8	lift: 1.0
#####  {'泡面', '巧克力'}
no:		{'泡面', '巧克力'}=>{'巧克力'}	conf: 0.4	lift: 1.0
yes:	{'泡面', '巧克力'}=>{'泡面'}	conf: 1.0	lift: 1.0
#####  {'面包', '泡面', '巧克力'}
no:		{'面包', '泡面', '巧克力'}=>{'巧克力'}	conf: 0.5	lift: 1.25
yes:	{'面包', '泡面', '巧克力'}=>{'面包'}	conf: 1.0	lift: 1.25
yes:	{'面包', '泡面', '巧克力'}=>{'泡面'}	conf: 1.0	lift: 1.0
no:		{'面包', '泡面', '巧克力'}=>{'面包', '巧克力'}	conf: 0.4	lift: 1.0
yes:	{'面包', '泡面', '巧克力'}=>{'面包', '泡面'}	conf: 1.0	lift: 1.25
no:		{'面包', '泡面', '巧克力'}=>{'泡面', '巧克力'}	conf: 0.5	lift: 1.25
#####  {'面包', '巧克力', '水'}
yes:	{'面包', '巧克力', '水'}=>{'水'}	conf: 1.0	lift: 1.0
no:		{'面包', '巧克力', '水'}=>{'巧克力'}	conf: 0.5	lift: 1.25
yes:	{'面包', '巧克力', '水'}=>{'面包'}	conf: 1.0	lift: 1.25
no:		{'面包', '巧克力', '水'}=>{'巧克力', '水'}	conf: 0.5	lift: 1.25
no:		{'面包', '巧克力', '水'}=>{'面包', '巧克力'}	conf: 0.4	lift: 1.0
yes:	{'面包', '巧克力', '水'}=>{'面包', '水'}	conf: 1.0	lift: 1.25
#####  {'面包', '泡面', '水'}
yes:	{'面包', '泡面', '水'}=>{'水'}	conf: 1.0	lift: 1.0
yes:	{'面包', '泡面', '水'}=>{'面包'}	conf: 0.8	lift: 1.0
yes:	{'面包', '泡面', '水'}=>{'泡面'}	conf: 1.0	lift: 1.0
yes:	{'面包', '泡面', '水'}=>{'泡面', '水'}	conf: 1.0	lift: 1.0
yes:	{'面包', '泡面', '水'}=>{'面包', '泡面'}	conf: 0.8	lift: 1.0
yes:	{'面包', '泡面', '水'}=>{'面包', '水'}	conf: 0.8	lift: 1.0
#####  {'泡面', '巧克力', '水'}
yes:	{'泡面', '巧克力', '水'}=>{'水'}	conf: 1.0	lift: 1.0
no:		{'泡面', '巧克力', '水'}=>{'巧克力'}	conf: 0.4	lift: 1.0
yes:	{'泡面', '巧克力', '水'}=>{'泡面'}	conf: 1.0	lift: 1.0
no:		{'泡面', '巧克力', '水'}=>{'巧克力', '水'}	conf: 0.4	lift: 1.0
yes:	{'泡面', '巧克力', '水'}=>{'泡面', '水'}	conf: 1.0	lift: 1.0
no:		{'泡面', '巧克力', '水'}=>{'泡面', '巧克力'}	conf: 0.4	lift: 1.0
#####  {'面包', '泡面', '水', '巧克力'}
yes:	{'面包', '泡面', '水', '巧克力'}=>{'水'}	conf: 1.0	lift: 1.0
no:		{'面包', '泡面', '水', '巧克力'}=>{'巧克力'}	conf: 0.5	lift: 1.25
yes:	{'面包', '泡面', '水', '巧克力'}=>{'面包'}	conf: 1.0	lift: 1.25
yes:	{'面包', '泡面', '水', '巧克力'}=>{'泡面'}	conf: 1.0	lift: 1.0
no:		{'面包', '泡面', '水', '巧克力'}=>{'巧克力', '水'}	conf: 0.5	lift: 1.25
yes:	{'面包', '泡面', '水', '巧克力'}=>{'泡面', '水'}	conf: 1.0	lift: 1.0
no:		{'面包', '泡面', '水', '巧克力'}=>{'面包', '巧克力'}	conf: 0.4	lift: 1.0
yes:	{'面包', '泡面', '水', '巧克力'}=>{'面包', '泡面'}	conf: 1.0	lift: 1.25
yes:	{'面包', '泡面', '水', '巧克力'}=>{'面包', '水'}	conf: 1.0	lift: 1.25
no:		{'面包', '泡面', '水', '巧克力'}=>{'泡面', '巧克力'}	conf: 0.5	lift: 1.25
no:		{'面包', '泡面', '水', '巧克力'}=>{'面包', '泡面', '巧克力'}	conf: 0.4	lift: 1.0
no:		{'面包', '泡面', '水', '巧克力'}=>{'面包', '巧克力', '水'}	conf: 0.4	lift: 1.0
yes:	{'面包', '泡面', '水', '巧克力'}=>{'面包', '泡面', '水'}	conf: 1.0	lift: 1.25
no:		{'面包', '泡面', '水', '巧克力'}=>{'泡面', '巧克力', '水'}	conf: 0.5	lift: 1.25