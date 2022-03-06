# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : symbols.py
# Time       ：2022/2/27 下午3:10
# Author     ：XXXXXX
# version    ：python 3.6
# Description：
"""
import json
import pandas as pd
from copy import deepcopy

# 淀粉,生猪,棕榈,大豆1号,大豆2号,鸡蛋,豆油,
# 豆粕,精对苯二甲酸,菜籽粕,白砂糖,花生,玉米
#
# 原油,焦炭,焦煤,沥青,苯乙烯,热轧卷板,聚氯乙烯,短纤,锰硅,硅铁,螺纹,铁矿,
# 线型低密度聚乙烯,漂针浆,甲醇,玻璃,纯碱,燃料油
simplified_names = {'棕榈油': '棕榈', '黄大豆1号': '豆一', '黄大豆2号': '豆二', '精对苯二甲酸': 'PTC', '菜籽粕': '菜粕',
                    '白砂糖': '白糖', '冶金焦炭': '焦炭', '鲜鸡蛋': '鸡蛋', '热轧卷板': '热卷', '聚氯乙烯': 'PVC',
                    '螺纹钢': '螺纹', '线型低密度聚乙烯': '塑料', '漂针浆': '纸浆','石油沥青':'沥青','花生仁':'花生','黄玉米':'玉米','玉米淀粉':'淀粉'}

template = {
    "symbol": "ETHUSDT",
    "full_name": "BINANCE:ETHUSDT",
    "description": "BINANCE:ETHUSDT",
    "exchange": "Binance",
    "ticker": "ETH/USDT",
    "type": "crypto",
    "timezone": "Asia/Shanghai"
}
# multiplier,trading_code,delist_date,price_tick_desc,exchange,list_date,product_code,price_tick,instrument,name,last_ddate,minmov,pricescale
df = pd.read_csv('../conf/filtered_futures.csv')
# bigquant,ctp,name,exchange
all_symbols = []
for trading_code, name, exchange, instrument in df[['trading_code', 'name', 'exchange', 'instrument']].values:
    code = instrument.split('.')[0]
    code_name = name
    for k, v in simplified_names.items():
        if k in name:
            code_name = name.replace(k, v)
    temp = deepcopy(template)
    temp['symbol'] = code
    temp['full_name'] = code
    temp['description'] = code_name
    temp['exchange'] = exchange
    temp['ticker'] = code
    temp['type'] = 'futures'
    all_symbols.append(temp)
print(all_symbols)
with open('../conf/all_symbols.json', 'w', encoding='utf-8') as f:
    json.dump(all_symbols, f, indent=4, ensure_ascii=False)

codes = ['LH2205', 'P2205', 'B2204', 'JD2205', 'JM2205', 'J2205', 'Y2205', 'A2207', 'I2205', 'BU2206',
         'SC2204', 'EB2204', 'HC2205', 'V22205', 'PF2205', 'M2205', 'TA2205', 'RM2205', 'SM2205', 'SF2205', 'L2205',
         'SR2205', 'PK2204', 'C2205', 'CS2205', 'RB2205', 'SP2205', 'MA2205', 'FG2205', 'SA2205']
codes.reverse()
# 主力合约
with open('../conf/all_symbols.json', 'r') as f:
    data = json.load(f)
result = {}
for k in data:
    if k['symbol'] in codes:
        k['type']='main'
        result[k['symbol']] = k

t = [result[k] for k in codes if k in result]
with open('../conf/main_symbol.json', 'w') as f:
    json.dump(t, f, indent=4, ensure_ascii=False)
