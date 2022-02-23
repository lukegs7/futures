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
    with open('data/symbol_info_fg2205.json', 'r') as f:
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
    print('search: {}'.format(data))
    return jsonify(data)


# 0900-1015,1030-1130,1330-1500,2100-2300
def load_future_data(file_name):
    print('file_name:', file_name)
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


# console.log(widget.activeChart().getTimezone());
@app.route('/history')
def history():
    params = request.args.to_dict()
    print('history:{}'.format(params))
    print('start:{}, end:{}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(params['from']))),
                                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(params['to'])))))
    if params['symbol'] != 'FG2205':
        return {'s': 'ok', 't': [], 'o': [], 'c': [], 'h': [], 'l': [], 'v': []}
    result = load_future_data('data/FG2205_1m.csv')
    t = result['t']
    start_timestamp = params['from']
    # end_timestamp = params['to']
    # if int(start_timestamp) > int(t[-1]) or int(end_timestamp) < int(t[0]):
    #     print('no data')
    #     return {'s': 'no_data'}
    if params['resolution'] == '60':
        return load_future_data('data/FG2205_60m.csv')
    elif params['resolution'] == '15':
        return load_future_data('data/FG2205_15m.csv')
    elif params['resolution'] == '1D':
        return load_future_data('data/FG2205_day.csv')
    elif params['resolution'] == '240':
        print('240')
        return load_future_data('data/FG2205_15m.csv')
    print(result)
    # with open('data/btc.json', 'r') as f:
    #     data = json.load(f)
    # t, o, c, h, l, v = [], [], [], [], [], []
    # for item in data['Data']:
    #     t.append(item['time'])
    #     o.append(item['open'])
    #     c.append(item['close'])
    #     h.append(item['high'])
    #     l.append(item['low'])
    #     v.append(item['volumefrom'])

    # if int(start_timestamp) > int(t[-1]) or int(end_timestamp) < int(t[0]):
    #     return {'nextTime': '1522108800', 's': 'no_data'}
    # return {'s': 'ok', 't': t, 'o': o, 'c': c, 'h': h, 'l': l, 'v': v}

    return result


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()
