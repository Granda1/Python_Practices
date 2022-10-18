from pykrx import stock

import time
import pandas as pd
stock_code = stock.get_market_ticker_list() # 현재일자 기준 가장 가까운 영업일의 코스피 상장종목 리스트
res = pd.DataFrame()
for ticker in stock_code[:10]:
    df = stock.get_market_ohlcv_by_date(fromdate="20220901", todate="20220907", ticker=ticker)
    df = df.assign(종목코드=ticker, 종목명=stock.get_market_ticker_name(ticker))
    res = pd.concat([res, df], axis=0)
    time.sleep(1)
res = res.reset_index()
print(res[(res['종목명']=='CJ') & (res['종가']>=10000)])
