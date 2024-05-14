###### INPUTS ######

sym = 'ETH-USD'
close_under = 1823 # bot will auto close under this number
lowest_bal_allowed = 3000 # bot will auto close if we fall under this number
timeframe = '15MINS'
pos_size = 32
target_pnl = 4
max_loss = -1

#######

price = '23827'
limit = 30
sma = 20
fundrate_max = 0.000046
daily_max_loss_perc = 1.1
time_between_trades = 10

import pytz

import pandas as pd
import schedule, requests, os, sys
from datetime import datetime, timedelta
import dontshareconfig as ds
from dydx3 import Client
from web3 import Web3
from pprint import pprint
import time, logging
import warnings

warnings.filterwarnings('ignore')
from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
net = API_HOST_MAINNET


alvhemy = ds.almchemy
