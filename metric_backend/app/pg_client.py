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


class PgClient:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="postgres",
                                               host="localhost",
                                               port="5432",
                                               database="finance")

            print("Selecting rows from mobile table using cursor.fetchall")
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

    def close(self):
        try:
            if self.connection:
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")
        except Exception as ex:
            print(ex)

    def query(self, sql):
        """
            依据sql进行查询
        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
        return []
