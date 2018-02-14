# Utils for analyzing perf.

import matplotlib
import matplotlib.pyplot as plt

def basic_analyze(perf):
    print(perf.describe())

    ax1 = plt.subplot(3, 1, 1)
    perf.portfolio_value.plot(ax=ax1)
    ax1.set_ylabel('portfolio value')
    ax2 = plt.subplot(3, 1, 2, sharex=ax1)
    perf.GOOGL.plot(ax=ax2)
    ax2.set_ylabel('GOOGL stock price')
    ax3 = plt.subplot(3, 1, 3, sharex=ax1)
    perf.treasury_period_return.plot(ax=ax3)
    ax3.set_ylabel('Treasury Period Return')
    plt.show()
