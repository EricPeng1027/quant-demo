from jqdatasdk import *
import pandas as pd
import numpy as np

def test_read_file():
    filename = 'src/data.csv'
    end_price, volume = np.loadtxt(
        fname=filename,
        skiprows=1,
        delimiter=',',
        usecols=(2, 6),
        unpack=True
    )
    print("-------------------------------------------------------")
    print(end_price)
    print(volume)

def test_max_and_min():
    filename = 'src/data.csv'
    high_price, low_price = np.loadtxt(
        fname=filename,
        skiprows=1,
        delimiter=',',
        usecols=(4, 6),
        unpack=True
    )
    print("-------------------------------------------------------")
    print("max_price= {}".format(high_price.max()))
    print("low_price= {}".format(low_price.min()))

def test_ptp():
    filename = 'src/data.csv'
    high_price, low_price = np.loadtxt(
        fname=filename,
        skiprows=1,
        delimiter=',',
        usecols=(4, 5),
        unpack=True
    )
    print("-------------------------------------------------------")
    print("max - min of high price: {}".format(np.ptp(high_price)))
    print("max - min of low price: {}".format(np.ptp(low_price)))

def test_avg():
    filename = 'src/data.csv'
    end_price, volume = np.loadtxt(
        fname=filename,
        skiprows=1,
        delimiter=',',
        usecols=(2, 6),
        unpack=True
    )
    print("-------------------------------------------------------")
    print("avg_price = {}".format(np.average(end_price)))
    print("vwap = {}".format(np.average(end_price, weights=volume)))

def test_med():
    filename = 'src/data.csv'
    end_price, volume = np.loadtxt(
        fname=filename,
        skiprows=1,
        delimiter=',',
        usecols=(2, 6),
        unpack=True
    )
    print("-------------------------------------------------------")
    print("medium = {}".format(np.median(end_price)))

def test_var():
    filename = 'src/data.csv'
    end_price, volume = np.loadtxt(
        fname=filename,
        skiprows=1,
        delimiter=',',
        usecols=(2, 6),
        unpack=True
    )
    print("-------------------------------------------------------")
    print("var = {}".format(np.var(end_price)))
    print("var = {}".format(end_price.var()))

def test_volatility():
    filename = 'src/data.csv'
    end_price, volume = np.loadtxt(
        fname=filename,
        skiprows=1,
        delimiter=',',
        usecols=(2, 6),
        unpack=True
    )

    # 对数收益率
    log_return = np.diff(np.log(end_price))
    # 年度波动率
    annual_volatility = log_return.std() / log_return.mean() * np.sqrt(250) # 年交易日，通常取250
    # 月度波动率
    monthly_volatility = log_return.std() / log_return.mean() * np.sqrt(12)

    print("-------------------------------------------------------")
    print("log_return = {}".format(log_return))
    print("annual_volatility = {}".format(annual_volatility))
    print("monthly_volatility = {}".format(monthly_volatility))

if __name__ == '__main__':
    test_read_file()
    test_max_and_min()
    test_ptp()
    test_avg()
    test_med()
    test_var()
    test_volatility()
