import requests
import numpy as np
import matplotlib.pyplot as plt


class CompareStocks:

    # Constructor
    # Example: tesco, shopify, monthly, 30
    # Default values for if there is no values parsed
    def __init__(self, company1=['TSCO.LON', 'Tesco'], company2=['TSCO.LON', 'Tesco'],
                 period=['TIME_SERIES_DAILY', 'Time Series (Daily)', 'Daily Changes'], n_time=30):

        self.company1 = company1
        self.company2 = company2
        self.period = period
        self.n_time = n_time

    # Get first dataset from the API
    def data1(self):

        # Refereres to this objects values
        period = self.period
        company = self.company1
        n_time = self.n_time

        # API call
        url = 'https://www.alphavantage.co/query?function=' + period[0] + '&symbol=' + company[
            0] + '&outputsize=full&apikey=RNAMU4MD6H604GQL'
        r = requests.get(url)
        data = r.json()

        # Creates 2 arrays that later will contain dataset1's plotting values
        x1_values = []
        y1_values = []

        # Appends x and y values to x1 and y1 arrays
        for key in data[period[1]]:
            x1_values.append(key)
            y1_values.append(data[period[1]][key]['4. close'])

        # Slices the data so that we take current date and n_time days/weeks/months prior
        days = x1_values[0:n_time]
        values = y1_values[0:n_time]

        # Reverses the arrays so it will be displayed correctly
        days.reverse()
        values.reverse()

        # Zips the data into a dict
        new_data = dict(zip(days, values))

        return new_data

    def data2(self):

        # Initialize class variables
        period = self.period
        company = self.company2
        n_time = self.n_time

        # API call
        url = 'https://www.alphavantage.co/query?function=' + period[0] + '&symbol=' + company[
            0] + '&outputsize=full&apikey=RNAMU4MD6H604GQL'
        r = requests.get(url)
        data = r.json()

        # Creates 2 arrays that later will contain dataset1's plotting values
        x2_values = []
        y2_values = []

        # Appends x and y values to x1 and y1 arrays
        for key in data[period[1]]:
            x2_values.append(key)
            y2_values.append(data[period[1]][key]['4. close'])

        # Slices the array, so it only shows from current date to n_time prior
        days = x2_values[0:n_time]
        values = y2_values[0:n_time]

        # Reverses the arrays, so it will be displayed correctly in the plots
        days.reverse()
        values.reverse()

        # Zips the data into a dict
        new_data = dict(zip(days, values))

        return new_data

    def display_graph(self):

        # Initialize both datasets
        dataset1 = self.data1()
        dataset2 = self.data2()

        # Converts the y_values to floats and sorts to the data to prevent errors
        y1 = np.sort([float(i) for i in dataset1.values()])
        y2 = np.sort([float(i) for i in dataset2.values()])

        # Graph size
        plt.rcParams["figure.figsize"] = (15, 15)

        # Plots the data and labels itself
        plt.plot(dataset1.keys(), y1, label=self.company1[1])
        plt.plot(dataset2.keys(), y2, label=self.company2[1])

        # Rotates the x-value labels
        plt.xticks(rotation=60)

        # Y-value labels
        plt.ylabel('Exchange rate')

        # Eye candy
        plt.grid()
        plt.legend()

        # Prints graph
        plt.show()
