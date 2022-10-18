# option premium
#############################
#  modules
#############################
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from scipy import stats
from timeit import default_timer as timer
from datetime import datetime as dt

#############################
#  setting
#############################
setting = 0
# 0: simple
# 1: S&P 500 option. Verify with https://finance.yahoo.com/quote/%5EGSPC/options?p=%5EGSPC
# 2: S&P 500 option with historical volatility

if setting == 0:
    S0 = 100.0  # current stock price
    sig = 0.237  # volatility
    r = 0.01  # risk-free rate
    K = 102.0  # strike price
    T = 31 / 365  # maturity
    n = 2  # n of stages
    # Note: sig, r, T are annualized

if setting in [1, 2]:  # S&P 500 (dividend ignored)
    S0 = 4300.46  # S&P 500, https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC
    sig = 0.237  # implied volatility, https://finance.yahoo.com/quote/%5EGSPC/options?p=%5EGSPC
    r = 0.107 / 100  # short-term rate, https://www.wsj.com/market-data/bonds
    K = 4000.0
    n = 100

    expirationDay = dt(year=2021, month=12, day=17, hour=16, minute=0)  # close at 4 pm
    currentDay = dt(year=2021, month=10, day=4, hour=16, minute=0)
    diff = expirationDay - currentDay
    T = (diff.days + diff.seconds / 3600 / 24) / 365  # Calendar day counting. Trading day counting is also valid.

if setting == 2:  # estimate sig
    df = pd.read_csv('C:/Users/Daniel Hanjoo Rhee/Desktop/서울대학교/2-2/파생상품연구론/Lecture Note/lecture10a_SP500.csv')  # https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC
    df.info()
    df = df.rename(columns={'Adj Close**': 'price'})
    print(df.describe())
    df['day'] = pd.to_datetime(df.Date, format='%b %d, %Y')  # E.g., "Sep 24, 2021"
    df = df.sort_values(by='day')
    # Compare:
    # df['price'][0]  # label-based
    # df['price'][0:3]  # location-based
    df = df.reset_index(drop=True)  # index begins from 0, to avoid mistakes
    df.plot(x='day', y='price')
    df['logRet'] = np.log(df['price']) - np.log(df['price'].shift(1))
    # sig = df['logRet'].std() * np.sqrt(250)  # use all data
    sig = df['logRet'][-20:].std() * np.sqrt(252)  # use the last 20 days only. annualized.
    # No data on non-trading days, and thus trading days are counted. Calendar day counting is incorrect.

#############################
#  computation(총 3가지 방법이 있어용)
#############################
h = T / n
u = np.exp(sig * np.sqrt(h))
d = 1 / u
R = (1 + r) ** (T / n)  # gross risk-free rate for one stage
q = (R - d) / (u - d)  # risk-neutral prob of up

allNum = np.arange(n + 1)
sT = u ** (allNum) * d ** (n - allNum) * S0  # stock price at the final nodes
payoffs = np.maximum(sT - K, 0)


# computation by loops
tic = timer()
premiumTree = np.tile(np.nan, reps=(n + 1, n + 1))  # (t,i) element is the value at time t and event i
premiumTree[-1, :] = payoffs  # payoff at the final nodes

for t in range(n - 1, -1, -1):  # (start,stop,step): n-1, n-2, ..., 0
    for i in range(t + 1):
        premiumTree[t, i] = (q * premiumTree[t + 1, i + 1] + (1 - q) * premiumTree[t + 1, i]) / R

premiumLoops = premiumTree[0, 0]
print('premium by loops   = %f, time: %f' % (premiumLoops, timer() - tic))

# computation by vectorization
tic = timer()
premiumTree2 = np.tile(np.nan, reps=(n + 1, n + 1))  # (t,i) element is the value at time t and event i
premiumTree2[-1, :] = payoffs  # payoff at the final nodes

for t in range(n - 1, -1, -1):  # (start,stop,step): n-1, n-2, ..., 0
    premiumTree2[t, :t + 1] = (q * premiumTree2[t + 1, 1:t + 2] + (1 - q) * premiumTree2[t + 1, :t + 1]) / R

premiumVector = premiumTree2[0, 0]
print('premium by vector  = %f, time: %f' % (premiumVector, timer() - tic))

# computation by the formula
tic = timer()
riskNeutral = stats.binom.pmf(k=allNum, n=n, p=q)
premiumFormula = (riskNeutral @ payoffs) / R ** n
print('premium by formula = %f, time: %f' % (premiumFormula, timer() - tic))
