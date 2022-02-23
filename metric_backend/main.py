# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : main.py
# Time       ：2022/2/1 下午9:25
# Author     ：opengs7
# version    ：python 3.6
# Description：
"""
import pandas as pd
import time
import json
from flask import jsonify, request
import time
import pandas as pd
from flask import Flask, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')


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
    print(e, fsym, tsym, toTs, limit)
    with open('data/btc.json', 'r') as f:
        data = json.load(f)
    return data


@app.route('/config')
def config():
    with open('data/tv_config.json', 'r') as f:
        data = json.load(f)
    return data


@app.route('/symbols')
def symbol_info(symbol: str = 'BTC/USDT'):
    """
        /symbols?symbol=Bitfinex%3ABTC%2FUSD
    :param symbol:
    :return:
    """
    with open('data/symbol_info_btc.json', 'r') as f:
        data = json.load(f)
    return data


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
    print(request.args)
    params = request.args.to_dict()
    print('params:', params)
    type = params['type']
    exchange = params['exchange']
    limit = params['limit']
    with open('data/all_symbols.json', 'r') as f:
        data = json.load(f)
    data = list(filter(lambda x: type == '' or x['type'] == type, data))
    data = list(filter(lambda x: exchange == '' or x['exchange'] == exchange, data))
    print(data)
    return jsonify(data)


def load_future_data():
    df = pd.read_csv('data/FG2205.csv')
    df['time'] = df['date'].apply(lambda x: int(time.mktime(time.strptime(x, "%Y-%m-%d %H:%M:%S"))))
    time_to = df['time'].max()
    time_from = df['time'].min()
    result = {'FirstValueInArray': True, 'TimeTo': time_to, 'TimeFrom': time_from, 'Aggregated': False, 'Type': 100}
    df = df[['time', 'close', 'open', 'high', 'low', 'volume']]
    result = {
        's': 'ok',
        't': df['time'].tolist(),
        'o': df['open'].tolist(),
        'c': df['close'].tolist(),
        'h': df['high'].tolist(), 'l': df['low'].tolist(), 'v': df['volume'].tolist()}
    return result


@app.route('/history')
def history():
    params = request.args.to_dict()
    print('history:{}'.format(params))
    with open('data/btc.json', 'r') as f:
        data = json.load(f)
    t, o, c, h, l, v = [], [], [], [], [], []
    for item in data['Data']:
        t.append(item['time'])
        o.append(item['open'])
        c.append(item['close'])
        h.append(item['high'])
        l.append(item['low'])
        v.append(item['volumefrom'])
    start_timestamp = params['from']
    end_timestamp = params['to']
    if int(start_timestamp) > int(t[-1]) or int(end_timestamp) < int(t[0]):
        return {'nextTime': '1522108800', 's': 'no_data'}
    return {'s': 'ok', 't': t, 'o': o, 'c': c, 'h': h, 'l': l, 'v': v}
    # return load_future_data()


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()
