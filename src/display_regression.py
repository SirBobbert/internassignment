import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class DisplayRegression:

    # Constructor
    # Example: tesco, shopify, monthly, 30
    # Default values for if there is no values parsed
    def __init__(self, company=['TSCO.LON', 'Tesco'],
                 period=['TIME_SERIES_DAILY', 'Time Series (Daily)', 'Daily Changes'], n_time=30):

        self.company = company
        self.period = period
        self.n_time = n_time

    # Get dataset from the API
    def get_data(self):
        url = 'https://www.alphavantage.co/query?function=' + self.period[0] + '&symbol=' + self.company[
            0] + '&outputsize=full&apikey=RNAMU4MD6H604GQL'
        r = requests.get(url)
        data = r.json()

        return data

    def display_graph(self):

        # Initialize class variables
        data = self.get_data()
        period = self.period
        company = self.company
        n_time = self.n_time

        # Initializing arrays for plot
        x_values = []
        y_values = []

        # Appends the dates to the x_values array
        # Appends the stock changes values to the y_values array
        for key in data[period[1]]:
            x_values.append(key)
            y_values.append(data[period[1]][key]['4. close'])

        # Slices the array, so it only shows from current date to n_time prior
        days = x_values[0:n_time]
        values = y_values[0:n_time]

        # Reverses the arrays, so it will be displayed correctly in the plots
        days.reverse()
        values.reverse()

        # Converts the y_values to floats
        x = [float(i) for i in range(len(days))]
        y = [float(i) for i in values]

        # Create a dataframe containing days as x values and Exchange rate as y values
        df = pd.DataFrame({'Days': x, 'Exchange rate': y})

        # Slices the data so that x and y each contains the correct data
        x = df.iloc[:, 0].values.reshape(-1, 1)
        y = df.iloc[:, 1].values.reshape(-1, 1)

        # Regression calculation
        lr = LinearRegression()
        lr.fit(x,y)
        y_pred = lr.predict(x)

        # Graph size
        plt.rcParams["figure.figsize"] = (15, 15)

        # Scatter values on the graph
        plt.scatter(x, y, label=company[1])

        # Shows regression on the graph
        plt.plot(x, y_pred, color='red')

        # Rotates the x-value labels
        plt.xticks(rotation=60)

        # Y-value labels
        plt.ylabel('Exchange rate')

        # Eye candy
        plt.grid()

        # Prints the graph
        plt.show()