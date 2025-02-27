import pandas as pd
import matplotlib.pyplot as plt
from unittest import TestCase

class TestKDJ(TestCase):
    def cal_kdj(self, df):
        low_list = df['low'].rolling(9, min_periods=9).min()
        low_list.fillna(value=df['low'].expanding().min(), inplace=True)
        high_list = df['high'].rolling(9, min_periods=9).max()
        high_list.fillna(value=df['high'].expanding().max(), inplace=True)
        rsv = (df['close'] - low_list) / (high_list - low_list) * 100
        df['k'] = pd.DataFrame(rsv).ewm(com=2).mean()
        df['d'] = df['k'].ewm(com=2).mean()
        df['j'] = 3 * df['k'] - 2 * df['d']
        return df

    def test_KDJ(self):
        file_name = 'data.csv'
        df = pd.read_csv(file_name)
        df.columns = ['date', 'open', 'close', 'high', 'low', 'volume', 'money']
        df = df[["date", "close", "open", "high", "low", "volume"]]
        df["date"] = pd.to_datetime(df["date"])

        df_kdj = self.cal_kdj(df)
        print(df_kdj)

        plt.figure()
        df_kdj['k'].plot(color='red', label='k')
        df_kdj['d'].plot(color='blue', label='d')
        df_kdj['j'].plot(color='green', label='j')
        plt.legend(loc='best')

        major_index = df_kdj.index[df_kdj.index]
        major_xtics = df_kdj['date'][df_kdj.index]
        plt.xticks(major_index, major_xtics)
        plt.setp(plt.gca().get_xticklabels(), rotation=30)

        plt.grid(linestyle='-.')
        plt.title('平安银行KDJ图')
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.show()