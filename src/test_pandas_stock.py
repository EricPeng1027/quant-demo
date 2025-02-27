import  matplotlib.pyplot as plt
import pandas as pd
from unittest import TestCase

class TestPandasStock(TestCase):
    def test_read_file(self):
        file_name = 'data.csv'
        df = pd.read_csv(file_name)

        # 数据属性
        print(df.info())
        print("------------------------------------------------------------------------")
        # 数据统计值
        print(df.describe())

    # 获取时间信息
    def test_time(self):
        file_name = 'data.csv'
        df = pd.read_csv(file_name)
        df.columns = ['date', 'open', 'close', 'high', 'low', 'volume', 'money']
        df["date"] = pd.to_datetime(df["date"])
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month

        print(df)

    # 最低收盘价
    def test_close_min(self):
        file_name = 'data.csv'
        df = pd.read_csv(file_name)
        df.columns = ['date', 'open', 'close', 'high', 'low', 'volume', 'money']

        print("""close min: {}""".format(df['close'].min()))
        print("""close min index: {}""".format(df['close'].idxmin()))
        print("""close min frame: {}""".format(df.loc[df['close'].idxmin()]))

    # 每月平均收盘价与开盘价
    def test_mean(self):
        file_name = 'data.csv'
        df = pd.read_csv(file_name)
        df.columns = ['date', 'open', 'close', 'high', 'low', 'volume', 'money']

        df["date"] = pd.to_datetime(df["date"])
        df["month"] = df["date"].dt.month

        print("""month close mean: {}""".format(df.groupby('month')['close'].mean()))
        print("""month open mean: {}""".format(df.groupby('month')['open'].mean()))

    # 计算涨跌幅（今日收盘价 - 昨日收盘价）
    def test_ripples_ratio(self):
        file_name = 'data.csv'
        df = pd.read_csv(file_name)
        df.columns = ['date', 'open', 'close', 'high', 'low', 'volume', 'money']

        df["date"] = pd.to_datetime(df["date"])
        df["rise"] = df["close"].diff()
        df["rise_ratio"] = df["rise"] / df["close"].shift(1)

        print(df)