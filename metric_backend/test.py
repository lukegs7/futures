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

df=pd.read_csv('data/FG2205.csv')
df['time']=df['date'].apply(lambda x:int(time.mktime(time.strptime(x, "%Y-%m-%d %H:%M:%S"))))
time_to=df['time'].max()
time_from=df['time'].min()
result={'FirstValueInArray':True,'TimeTo':time_to,'TimeFrom':time_from,'Aggregated':False,'Type':100}
df=df[['time','close','open','high','low','volume']]
print(df['close'].tolist())