# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : test.py.py
# Time       ：2022/2/26 下午11:43
# Author     ：XXXXXX
# version    ：python 3.6
# Description：
"""

import os
import pandas as pd
import shutil
from itertools import islice

candidate = ['淀粉', '生猪', '棕榈', '大豆1号', '大豆2号', '鸡蛋', '焦炭', '焦煤', '豆油', '铁矿', '沥青', '原油', '苯乙烯', '热轧卷板', '聚氯乙烯', '短纤', '豆粕', '精对苯二甲酸', '菜籽粕', '锰硅', '硅铁',
             '线型低密度聚乙烯', '白砂糖', '花生', '玉米', '螺纹', '漂针浆', '甲醇', '玻璃', '纯碱', '燃料油', '尿素', '铅', '白银']


def filter_func(x):
    name, del_date = x['name'], x['delist_date']
    if del_date < '2022-04-01' or '主力' in name:
        return False
    for item in candidate:
        if item in name:
            break
    else:
        return False
    return True


def filter_futures():
    """
        过滤期货
        multiplier,trading_code,delist_date,price_tick_desc,exchange,list_date,product_code,price_tick,instrument,name,last_ddate
        minmov: price_tick*pricescale
        pricescale: 小数位数，10的倍数

    :return:
    """

    def pricescale(x):
        return int('1' + '0' * len(str(x).split('.')[1].rstrip('0')))

    df = pd.read_csv('../data/basic_info.csv')
    df['in'] = df[['name', 'delist_date']].apply(filter_func, axis=1)
    df = df[df['in'] == True]
    df['pricescale'] = df['price_tick'].apply(pricescale)
    df['minmov'] = df['pricescale'] * df['price_tick']
    df['minmov'] = df['minmov'].apply(int)
    df = df[['multiplier', 'trading_code', 'delist_date', 'price_tick_desc', 'exchange', 'list_date', 'product_code', 'price_tick', 'instrument', 'name',
             'last_ddate', 'minmov', 'pricescale']]
    df.to_csv('../conf/filtered_futures.csv', index=False)
    return df['trading_code'].values


def move_files(trading_codes):
    """
        将文件单独存储
    :param trading_codes:
    :return:
    """
    source_dir = os.path.join(os.environ['HOME'], 'learn/invest/data1')
    target_dir = os.path.join(os.environ['HOME'], 'learn/invest/fit_data1')
    for root, dirs, files in os.walk(source_dir):
        base_dir_name = os.path.basename(root)
        target_sub_dir = os.path.join(target_dir, base_dir_name)
        for file in files:
            if not file.endswith('csv'):
                continue
            if not os.path.exists(target_sub_dir):
                os.mkdir(target_sub_dir)
            temp = file.split('.')[0]
            if temp in trading_codes:
                shutil.copy(os.path.join(root, file), os.path.join(target_sub_dir, file))


def combine():
    target_dir = os.path.join(os.environ['HOME'], 'learn/invest/fit_data1')
    data = {'1m': 'FutAC_Min1_Std_202202', '5m': 'FutAC_Min5_Std_202202', '15m': 'FutAC_Min15_Std_202202', '30m': 'FutAC_Min30_Std_202202',
            '60m': 'FutAC_Min60_Std_202202', '1d': 'FutAC_DAY_20220228'}
    for k, v in data.items():
        print(k, v)
        with open(os.path.join(target_dir, k + '.csv'), 'w', encoding='utf-8') as fw:
            temp_dir = os.path.join(target_dir, v)
            for file in os.listdir(temp_dir):
                with open(os.path.join(temp_dir, file), 'r', encoding='gbk') as f:
                    for line in islice(f, 1, None):
                        temp = line.strip().split(',')[1:]
                        fw.write(','.join(temp) + '\n')


def test():
    target_file = os.path.join(os.environ['HOME'], 'learn/invest/fit_data/1d.csv')
    df = pd.read_csv(target_file)
    print(df.head())
    print(df.shape)


if __name__ == '__main__':
    trading_codes = filter_futures()
    # move_files(trading_codes)
    # combine()
    # test()

