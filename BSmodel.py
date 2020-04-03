#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
import scipy.stats
import pandas


# (Source: https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)
# Input:
#   - S = sport price (40)
#   - K = the strike price of the option (35)
#   - t = time to maturity (212.91) [Annualized!]
#   - r = risk fee (0.0488)
#   - s = volatility (0.20)

class OptionsPricer(object):
  def __init__(self, spot_price, strike_price, time_to_maturity,
               risk_free_rate, volatility, option_type):
    assert option_type == 'put' or option_type == 'call'
    self.spot_price = spot_price
    self.strike_price = strike_price
    self.time_to_maturity = time_to_maturity
    self.risk_free_rate = risk_free_rate
    self.volatility = volatility
    self.option_type = option_type

  def price(self):
    # TODO: implement this!

    timeY = (self.time_to_maturity/365)

    # Defining Ds
    d1 = (np.log(self.spot_price/self.strike_price) + (self.risk_free_rate + 0.5 * self.volatility**2) * timeY)/(self.volatility * np.sqrt(timeY))
    d2 = (np.log(self.spot_price/self.strike_price) + (self.risk_free_rate - 0.5 * self.volatility**2) * timeY)/(self.volatility * np.sqrt(timeY))

    if self.option_type == 'call':
        result = (self.spot_price * scipy.stats.norm.cdf(d1, 0.0, 1.0) - self.strike_price * np.exp(-self.risk_free_rate * timeY)* scipy.stats.norm.cdf(d2, 0.0, 1.0))
    elif self.option_type == 'put':
        result = (self.strike_price*np.exp(-self.risk_free_rate*timeY) * scipy.stats.norm.cdf(-d2, 0.0, 1.0) - self.spot_price * scipy.stats.norm.cdf(-d1, 0.0, 1.0))
    else:
        return 'Error!'
        exit(1)

    #print(result)      #6.399084091326394
    return result


def main():