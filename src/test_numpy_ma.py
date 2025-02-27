import numpy as np
import matplotlib.pyplot as plt
from unittest import TestCase

class TestNumpyMa(TestCase):
    def test_sma(self):
        filename = 'data.csv'
        end_price = np.loadtxt(
            fname=filename,
            skiprows=1,
            delimiter=',',
            usecols=(2),
            unpack=True
        )

        print("end_price： ", end_price)
        N = 5
        weights = np.ones(N) / N
        print("weights: ", weights)
        sma = np.convolve(weights, end_price)[N - 1: -N + 1]
        print("sma: ", sma)
        plt.plot(sma, linewidth=5)
        plt.show()

    def test_exp(self):
        x = np.arange(5)
        y = np.arange(10)
        print("x: ", x)
        print("y: ", y)
        print("""Exp x: {}""".format(np.exp(x)))
        print("""Exp y: {}""".format(np.exp(y)))
        print("""Linespace: {}""".format(np.linspace(-1, 0, 5)))

    def test_ema(self):
        filename = 'data.csv'
        end_price = np.loadtxt(
            fname=filename,
            skiprows=1,
            delimiter=',',
            usecols=(2),
            unpack=True
        )

        print("end_price： ", end_price)
        N = 5
        weights = np.exp(np.linspace(-1, 0, N))
        weights /= weights.sum()
        print("weights: ", weights)
        ema = np.convolve(weights, end_price)[N - 1: -N + 1]
        print("sma: ", ema)

        t = np.arange(N - 1, len(end_price))
        plt.plot(t, end_price[N - 1:], lw=1.0)
        plt.plot(t, ema, lw=2.0)
        plt.show()