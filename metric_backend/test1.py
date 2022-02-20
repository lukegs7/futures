# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : test1.py
# Time       ：2022/2/13 下午5:35
# Author     ：opengs7
# version    ：python 3.6
# Description：
"""
data=[]
with open('/Users/opengs7/learn/invest/tradingview/TradingView-example-master/symbolinfo','r') as f:
    for line in f:
       data.append(line)
with open('/Users/opengs7/learn/invest/tradingview/TradingView-example-master/symbolinfo','w') as f:
    for k in data:
        f.write(k.lower())