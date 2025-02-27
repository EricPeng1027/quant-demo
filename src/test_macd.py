import  matplotlib.pyplot as plt
import pandas as pd
from matplotlib import colors as mycolors
from matplotlib.collections import LineCollection, PolyCollection
from unittest import TestCase

class TestMACD(TestCase):
    def cal_macd(self, df, fastperiod=12, slowperiod=26, signalperiod=9):
        # 短期移动均线
        ewma12 = df['close'].ewm(span=fastperiod, adjust=False).mean()
        # 长期移动均线
        ewma26 = df['close'].ewm(span=slowperiod, adjust=False).mean()
        df['dif'] = ewma12 - ewma26
        df['dea'] = df['dif'].ewm(span=signalperiod, adjust=False).mean()
        df['bar'] = 2 * (df['dif'] - df['dea'])
        return df

    def test_MACD(self):
        file_name = 'data.csv'
        df = pd.read_csv(file_name)
        df.columns = ['date', 'open', 'close', 'high', 'low', 'volume', 'money']
        df = df[["date", "close", "open", "high", "low", "volume"]]
        df["date"] = pd.to_datetime(df["date"])

        df_macd = self.cal_macd(df)
        print(df_macd)

        plt.figure()
        df_macd['dea'].plot(color='red', label='dea')
        df_macd['dif'].plot(color='blue', label='dif')
        plt.legend(loc='best')

        pos_bar = []
        pos_index = []
        neg_bar = []
        neg_index = []

        for index, row in df_macd.iterrows():
            if row['bar'] > 0:
                pos_bar.append(row['bar'])
                pos_index.append(index)
            else:
                neg_bar.append(row['bar'])
                neg_index.append(index)

        # 大于0用红色表示多头
        plt.bar(pos_index, pos_bar, color='red', width=0.5)
        # 小于0用绿色表示空头
        plt.bar(neg_index, neg_bar, color='green', width=0.5)

        major_index = df_macd.index[df_macd.index]
        major_xticks = df_macd['date'][df_macd.index]
        plt.xticks(major_index, major_xticks)
        plt.setp(plt.gca().get_xticklabels(), rotation=30)
        plt.grid(linestyle='-.')
        plt.title('平安银行MACD图')
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.show()