import pandas as pd

from util import display_single_stock, compare_stocks

# LIST OF COMPANIES ['Company code', 'Name']
# TESCO PLC (London Stock Exchange)
tesco = ['TSCO.LON', 'Tesco']
# Shopify Inc (Canada - Toronto Stock Exchange)
shopify = ['SHOP.TRT', 'Shopify Inc']
# GreenPower Motor Company Inc (Canada - Toronto Venture Exchange)
greenpower = ['GPV.TRV', 'GreenPower Motor Company Inc']
# Daimler AG (Germany - XETRA)
daimler = ['DAI.DEX', 'Daimler AG']

# Daily, weekly or monthly
daily = ['TIME_SERIES_DAILY', 'Time Series (Daily)', 'Daily Changes']
weekly = ['TIME_SERIES_WEEKLY', 'Weekly Time Series', "Weekly Changes"]
monthly = ['TIME_SERIES_MONTHLY', 'Monthly Time Series', 'Monthly Changes']

# Company, period, n_time
#display_single_stock.DisplaySingleStock(tesco, daily, 55).display_graph()

# Company1, company2, period, n_time
#compare_stocks.CompareStocks(daimler, tesco, daily, 55).display_graph()

