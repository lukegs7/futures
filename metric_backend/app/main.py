# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : main.py
# Time       ：2022/2/1 下午9:25
# Author     ：XXXXXX
# version    ：python 3.6
# Description：
"""
import json
from flask import jsonify, request
import time
import pandas as pd
import copy
from flask import Flask
from flask_cors import CORS
from pg_client import PgClient

app = Flask(__name__)
CORS(app, resources=r'/*')

CANDIDATE_SYMBOL_INFOS = dict()


def init_conf():
    with open('conf/symbol_info_template.json', 'r', encoding='utf-8') as f:
        symbol_info = json.load(f)
    df = pd.read_csv('conf/filtered_futures.csv')
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


@app.route('/data/v3/all/exchanges')
def exchanges():
    with open('data/exchanges.json', 'r') as f:
        data = json.load(f)
    return data


@app.route('/data/histoday')
def histoday(e: str = None, fsym: str = None, tsym: str = None, toTs: int = 1644730975, limit: int = 2000):
    with open('data/btc.json', 'r') as f:
        data = json.load(f)
    return data


@app.route('/config')
def config():
    with open('conf/tv_config.json', 'r') as f:
        data = json.load(f)
    return data


@app.route('/symbols')
def symbol_info():
    """
        /symbols?symbol=Bitfinex%3ABTC%2FUSD
    :param symbol:
    :return:
    """
    params = request.args.to_dict()
    symbol = params['symbol']
    print('symbol:', symbol)
    print(CANDIDATE_SYMBOL_INFOS)
    return CANDIDATE_SYMBOL_INFOS.get(symbol, {})


@app.route('/time')
def current_time():
    """
        /symbols?symbol=Bitfinex%3ABTC%2FUSD
    :param symbol:
    :return:
    """
    return str(int(time.time()))


@app.route('/search')
def search():
    """
        /symbols?symbol=Bitfinex%3ABTC%2FUSD
        No symbols matched your criteria
    :param symbol:
    :return:
    """
    params = request.args.to_dict()
    query = params['query']
    type = params['type']
    exchange = params['exchange']
    # limit = params['limit']
    with open('conf/all_symbols.json', 'r') as f:
        data = json.load(f)
    data = list(filter(lambda x: query == '' or query.upper() in x['symbol'].upper(), data))
    data = list(filter(lambda x: type == '' or x['type'].upper() == type.upper(), data))
    data = list(filter(lambda x: exchange == '' or x['exchange'].upper() == exchange.upper(), data))
    return jsonify(data)


# 0900-1015,1030-1130,1330-1500,2100-2300
def load_future_data(file_name):
    i = 0
    t, o, c, h, l, v = [], [], [], [], [], []
    with open(file_name, 'r') as f:
        for line in f:
            if i == 0:
                i += 1
                continue
            temp = line.strip().split(',')

            if len(temp[6]) == 19:
                t.append(int(time.mktime(time.strptime(temp[6], "%Y-%m-%d %H:%M:%S"))))
            else:
                t.append(int(time.mktime(time.strptime(temp[6], "%Y-%m-%d"))))
            o.append(int(float(temp[8])))
            c.append(int(float(temp[4])))
            h.append(int(float(temp[1])))
            l.append(int(float(temp[3])))
            v.append(int(float(temp[2])))
    return {'s': 'ok', 't': t, 'o': o, 'c': c, 'h': h, 'l': l, 'v': v}


def load_data(product_code, resolution, start_time, end_time):
    """
        从数据库数据库获取数据
    :param product_code:
    :param start_time:
    :param end_time:
    :return:
    """
    print('product_code:', product_code)
    client = PgClient()
    table_name = 'ods.bar1m'
    if resolution == '1':
        table_name = 'ods.bar1m'
    elif resolution == '5':
        table_name = 'ods.bar5m'
    elif resolution == '15':
        table_name = 'ods.bar15m'
    elif resolution == '30':
        table_name = 'ods.bar30m'
    elif resolution == '60':
        table_name = 'ods.bar60m'
    elif resolution == '1D':
        table_name = 'ods.bar1d'

    sql = "select timestamp,open,high,low,close,volume from {} " \
          "where instrument='{}' and timestamp>={} and timestamp<={} order by timestamp".format(table_name, product_code, int(start_time), int(end_time))
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


# console.log(widget.activeChart().getTimezone());
@app.route('/history')
def history():
    params = request.args.to_dict()
    print('history:{}'.format(params))
    print('start:{}, end:{}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(params['from']))),
                                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(params['to'])))))
    start_time = int(params['from'])
    end_time = int(params['to'])
    if time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)) < '2020-01-01' or end_time < 0:
        return {'s': 'no_data'}
    return load_data(params['symbol'], params['resolution'], params['from'], params['to'])


if __name__ == '__main__':
    init_conf()
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()
