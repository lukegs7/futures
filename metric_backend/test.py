# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : test.py.py
# Time       ：2022/2/1 下午9:47
# Author     ：opengs7
# version    ：python 3.6
# Description：
"""
import time
import pandas as pd
import json

columns = ['1m', '5m', '15m', '30m', '60m', 'day']
for item in columns:
    df = pd.read_csv('data/FG2205_{}.csv'.format(item))
    df = df[['instrument', 'high', 'volume', 'low', 'close', 'product_code', 'date', 'open_intl', 'open']]
    df.to_csv('data/FG2205_{}.csv'.format(item), index=False)
