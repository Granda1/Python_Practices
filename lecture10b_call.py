# option premium
# This approach creating and using custom functions in Python will be useful
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
#  main
#############################
def main():
    S0 = 100.0  # current stock price
    sig = 0.237  # volatility
    r = 0.01  # risk-free rate
    K = 102.0  # strike price
    T = 31 / 365  # maturity
    n = 100  # n of stages
    # Note: sig, r, T are annualized

    premium = getOptionPremium(S0, sig, r, K, T, n)
    print('premium = %f' % (premium))


#############################
#  functions
#############################
def getOptionPremium(S0, sig, r, K, T, n):
    h = T / n
    u = np.exp(sig * np.sqrt(h))
    d = 1 / u
    R = (1 + r) ** (T / n)  # gross risk-free rate for one stage
    q = (R - d) / (u - d)  # risk-neutral prob of up

    allNum = np.arange(n + 1)
    sT = u ** (allNum) * d ** (n - allNum) * S0  # stock price at the final nodes
    payoffs = np.maximum(sT - K, 0)

    # computation by the formula
    riskNeutral = stats.binom.pmf(k=allNum, n=n, p=q)
    premiumFormula = (riskNeutral @ payoffs) / R ** n
    return premiumFormula


#############################
#  run
#############################
if __name__ == '__main__':
    main()