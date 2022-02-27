# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : main.py
# Time       ：2022/2/1 下午9:25
# Author     ：XXXXXX
# version    ：python 3.6
# Description：
"""

import os
import json
import time
import copy
import pandas as pd
from flask import jsonify, request
from flask import Flask
from flask_cors import CORS
from pg_client import PgConn

BASE_DIR = os.path.dirname(__file__)

app = Flask(__name__)
CORS(app, resources=r'/*')

CANDIDATE_SYMBOL_INFOS = dict()


def init_conf():
    with open(os.path.join(BASE_DIR, 'conf/symbol_info_template.json'), 'r', encoding='utf-8') as f:
        symbol_info = json.load(f)
    df = pd.read_csv(os.path.join(BASE_DIR, 'conf/filtered_futures.csv'))
    for trading_code, exchange, name, minmov, price_scale in df[['trading_code', 'exchange', 'name', 'minmov', 'pricescale']].values:
        temp = copy.deepcopy(symbol_info)
        temp['name'] = trading_code
        temp['exchange-traded'] = exchange
        temp['exchange-listed'] = exchange
        temp['minmov'] = int(minmov)
        temp['pricescale'] = int(price_scale)
        temp['description'] = name
        CANDIDATE_SYMBOL_INFOS[trading_code] = temp


@app.route('/')
def index():
    return 'Hello World'


@app.route('/config')
def config():
    with open(os.path.join(BASE_DIR, 'conf/tv_config.json'), 'r') as f:
        data = json.load(f)
    return data


@app.route('/symbols')
def symbol_info():
    """
        获取商品期货信息
    :param symbol:
    :return:
    """
    params = request.args.to_dict()
    symbol = params['symbol']
    return CANDIDATE_SYMBOL_INFOS.get(symbol, {})


@app.route('/time')
def current_time():
    """
        获取系统时间
    :param symbol:
    :return:
    """
    return str(int(time.time()))


@app.route('/search')
def search():
    """
        查询商品期货
        No symbols matched your criteria
    :param symbol:
    :return:
    """
    params = request.args.to_dict()
    query = params['query']
    type = params['type']
    exchange = params['exchange']
    with open(os.path.join(BASE_DIR, 'conf/all_symbols.json'), 'r') as f:
        data = json.load(f)
    data = list(filter(lambda x: query == '' or query.upper() in x['symbol'].upper(), data))
    data = list(filter(lambda x: type == '' or x['type'].upper() == type.upper(), data))
    data = list(filter(lambda x: exchange == '' or x['exchange'].upper() == exchange.upper(), data))
    return jsonify(data)


def load_data(instrument, resolution, start_time, end_time):
    """
        从数据库数据库获取数据
    :param instrument: 商品编码
    :param start_time: 开始时间
    :param end_time: 结束时间
    :return:
    """
    client = PgConn()
    table_config = {'1': 'bar1m', '5': 'bar5m', '15': 'bar15m', '30': 'bar30m', '60': 'bar60m', '1D': 'bar1d'}
    cur_table_name = table_config.get(resolution, 'bar60m')
    sql = "select timestamp,open,high,low,close,volume from ods.{} " \
          "where instrument='{}' and timestamp>={} and timestamp<={} order by timestamp".format(cur_table_name, instrument, int(start_time), int(end_time))
    data = client.query(sql)
    t, o, c, h, l, v = [], [], [], [], [], []
    for item in data:
        t.append(item[0])
        o.append(item[1])
        h.append(item[2])
        l.append(item[3])
        c.append(item[4])
        v.append(item[5])
    return {'s': 'ok', 't': t, 'o': o, 'c': c, 'h': h, 'l': l, 'v': v}


@app.route('/history')
def history():
    """
        获取历史数据
    :return:
    """
    params = request.args.to_dict()
    end_time = int(params['to'])
    if time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)) < '2020-01-01' or end_time < 0:
        return {'s': 'no_data'}
    return load_data(params['symbol'], params['resolution'], params['from'], params['to'])


if __name__ == '__main__':
    init_conf()
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()
