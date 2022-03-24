# api key
# RNAMU4MD6H604GQL

# https://www.alphavantage.co/documentation/


import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# API to data
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey=RNAMU4MD6H604GQL'
r = requests.get(url)
data = r.json()

# Takes the API data and converts it into a dataframe
df = pd.DataFrame.from_dict(data['Time Series (Daily)'])

# Initializing arrays for plot
x_values = []
y_values = []

# Shows the opening value for each day
for key in data['Time Series (Daily)']:
    x_values.append(key)
    y_values.append(data['Time Series (Daily)'][key]['1. open'])

# Converts the y_values array to float
# Displays the plot
plt.plot([float(i) for i in y_values])
plt.ylabel('Exchange rate')
plt.xlabel('Days')
plt.grid()
plt.show()
