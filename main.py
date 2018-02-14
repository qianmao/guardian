
import pandas as pd
import zipline

from zipline.api import order_target, record, symbol

import algos.test_algo as algo
import analyze.analyze_utils as analyze_utils

if __name__ == '__main__':
    start = pd.Timestamp('2010-01-01', tz='UTC')
    end = pd.Timestamp('2017-12-31', tz='UTC')
    capital_base = 10000

    perf = zipline.run_algorithm(
        start=start,
        end=end,
        initialize=algo.initialize,
        capital_base=capital_base,
        handle_data=algo.handle_data)

    analyze_utils.basic_analyze(perf)
