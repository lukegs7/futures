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
    temp = deepcopy(template)
    temp['symbol'] = code
    temp['full_name'] = code
    temp['description'] = name
    temp['exchange'] = exchange
    temp['ticker'] = code
    temp['type'] = 'futures'
    all_symbols.append(temp)
print(all_symbols)
with open('../conf/all_symbols.json', 'w', encoding='utf-8') as f:
    json.dump(all_symbols, f, indent=4, ensure_ascii=False)
