# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : demo.py
# Time       ：2022/2/25 上午12:06
# Author     ：opengs7
# version    ：python 3.6
# Description：
"""

import pandas as pd
df=pd.read_csv('instrument.csv',header=None)
df.columns=['index','instrument']
df['instrument']=df['instrument'].str.upper()
df[['instrument']].to_csv('instrument.csv',index=False)