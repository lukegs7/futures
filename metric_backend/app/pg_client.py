# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : PgClient.py
# Time       ：2022/2/27 上午10:51
# Author     ：XXXXXX
# version    ：python 3.6
# Description：
"""
import psycopg2


class PgConn:
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = super().__new__(cls)

        return cls.obj

    def __init__(self):
        try:
            self.db = psycopg2.connect(user="postgres", password="postgres", host="localhost",
                                       port="5432", database="finance")
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL %s" % error)
        self.cs = self.db.cursor()

    def query(self, sql):
        try:
            self.cs.execute(sql)
            rows = self.cs.fetchall()
            return rows
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL %s" % error)
        return list()

    def __del__(self):
        try:
            self.cs.close()
            self.db.close()
        except Exception as ex:
            print('failed to close connection: %s' % str(ex))
