# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : probe.py
# Time       ：2022/3/5 上午1:07
# Author     ：XXXXXX
# version    ：python 3.7
# Description：
"""
import requests
import pandas as pd
import time

url5min = 'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine5m?symbol={}'
url15min = 'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine15m?symbol={}'
url30min = 'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine30m?symbol={}'
url60min = 'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine60m?symbol={}'
url1d = 'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol={}'
# '5m': url5min,
url_dict = {'15m': url15min, '30m': url30min, '60m': url60min, '1d': url1d}
df = pd.read_csv('../conf/filtered_futures.csv')
instruments = df['instrument'].values
error_data = []
for period, url in url_dict.items():
    with open('{}.csv'.format(period), 'w') as f:
        for instrument in instruments:
            try:
                print('{}, {}, {}'.format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),period, instrument))
                res = requests.get(url)
                data = res.json()
                if len(data) == 0:
                    error_data.append([period, instrument])
                for item in data:
                    f.write(','.join([instrument] + data) + '\n')
            except:
                print(res)
                print(res.content)
                break
            time.sleep(4)
df1 = pd.DataFrame(data=error_data, columns=['period', 'instrument'])
df1.to_csv('error.csv', index=False)
