import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class CompareStocks:

    # Default values for if there is no values parsed
    def __init__(self, company1, company2, period, n_time=30):

        self.company1 = company1
        self.company2 = company2

        self.period = period

        if type(n_time) is int:
            self.n_time = n_time
        else:
            raise TypeError('Only integers are allowed')

    # Get data that matches the chosen input
    def data1(self):

        period = self.period
        company = self.company1
        n_time = self.n_time

        url = 'https://www.alphavantage.co/query?function=' + period[0] + '&symbol=' + company[
            0] + '&outputsize=full&apikey=RNAMU4MD6H604GQL'
        r = requests.get(url)
        data = r.json()

        x1_values = []
        y1_values = []

        for key in data[period[1]]:
            x1_values.append(key)
            y1_values.append(data[period[1]][key]['4. close'])

        days = x1_values[0:n_time]
        values = y1_values[0:n_time]

        days.reverse()
        values.reverse()

        new_data = dict(zip(days, values))

        return new_data

    def data2(self):

        period = self.period
        company = self.company2
        n_time = self.n_time

        url = 'https://www.alphavantage.co/query?function=' + period[0] + '&symbol=' + company[
            0] + '&outputsize=full&apikey=RNAMU4MD6H604GQL'
        r = requests.get(url)
        data = r.json()

        x1_values = []
        y1_values = []

        for key in data[period[1]]:
            x1_values.append(key)
            y1_values.append(data[period[1]][key]['4. close'])

        days = x1_values[0:n_time]
        values = y1_values[0:n_time]

        days.reverse()
        values.reverse()

        new_data = dict(zip(days, values))

        return new_data

    def display_graph(self):

        dataset1 = self.data1()
        dataset2 = self.data2()

        y1 = np.sort([float(i) for i in dataset1.values()])
        y2 = np.sort([float(i) for i in dataset2.values()])

        plt.rcParams["figure.figsize"] = (15, 15)
        plt.plot(dataset1.keys(), y1, label=self.company1[1])
        plt.plot(dataset2.keys(), y2, label=self.company2[1])
        plt.xticks(rotation=60)
        plt.ylabel('Exchange rate')
        plt.grid()
        plt.legend()
        plt.show()
