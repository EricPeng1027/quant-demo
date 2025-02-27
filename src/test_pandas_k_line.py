import  matplotlib.pyplot as plt
from mpl_finance import candlestick2_ochl
import mplfinance as mpf
import pandas as pd
from unittest import TestCase

class TestPandasKLine(TestCase):
    # 画k线图
    def test_pandas_k_line(self):
        file_name = 'data.csv'
        df = pd.read_csv(file_name)
        df.columns = ['date', 'open', 'close', 'high', 'low', 'volume', 'money']

        fig = plt.figure()
        axis = fig.add_subplot(111)
        candlestick2_ochl(axis, opens=df['open'].values, closes=df['close'].values, highs=df['high'].values,
                          lows=df['low'].values, width=0.75, colorup='r', colordown='g')
        plt.xticks(range(len(df.index.values)), df.index.values, rotation=30)
        axis.grid(True)
        plt.title('K-Line')
        plt.show()

    # K线图带交易量
    def test_k_line_with_volume(self):
        file_name = 'data.csv'
        df = pd.read_csv(file_name)
        df.columns = ['date', 'open', 'close', 'high', 'low', 'volume', 'money']
        df = df[["date", "close", "open", "high", "low", "volume"]]
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index("date")

        my_color = mpf.make_marketcolors(
            up="r",
            down="g",
            wick='i',
            volume={'up': 'r', 'down': 'g'},
            ohlc='i'
        )

        my_style = mpf.make_mpf_style(
            marketcolors=my_color,
            gridaxis='both',
            gridstyle='-.',
            rc={'font.family':'STSong'}
        )

        mpf.plot(df,
                 type='candle',
                 volume=True,
                 style=my_style,
                 title='K-Line-with-volume',
                 ylabel='price',
                 show_nontrading=False,
                 ylabel_lower='volume',
                 datetime_format='%Y-%m-%d',
                 xrotation=45,
                 linecolor='#00ff00',
                 tight_layout=False)

    # 带均线的k线图
    def test_k_line_with_ma(self):
        file_name = 'data.csv'
        df = pd.read_csv(file_name)
        df.columns = ['date', 'open', 'close', 'high', 'low', 'volume', 'money']
        df = df[["date", "close", "open", "high", "low", "volume"]]
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index("date")

        my_color = mpf.make_marketcolors(
            up="r",
            down="g",
            wick='i',
            volume={'up': 'r', 'down': 'g'},
            ohlc='i'
        )

        my_style = mpf.make_mpf_style(
            marketcolors=my_color,
            gridaxis='both',
            gridstyle='-.',
            rc={'font.family': 'STSong'}
        )

        mpf.plot(df,
                 type='candle',
                 volume=True,
                 style=my_style,
                 title='K-Line-with-volume',
                 ylabel='price',
                 show_nontrading=False,
                 ylabel_lower='volume',
                 datetime_format='%Y-%m-%d',
                 xrotation=45,
                 linecolor='#00ff00',
                 tight_layout=False,
                 mav=[5, 10])