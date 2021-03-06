# Imports
from company import show_company_names as show_names
import display_single_stock
import compare_stocks
import display_regression


# Asks the user which function he/she would like to use
def menu():
    print('Please choose one of the following options')
    print('1. Display stock')
    print('2. Display multiple stocks and compare')
    print('3. Display stock regression')

    while True:
        try:
            question = int(input())
            break
        except:
            print("That's not a valid option!")

    if question == 1:
        display_single_stock_prompt()
    elif question == 2:
        display_compare_stocks_prompt()
    elif question == 3:
        display_single_regression_prompt()
    else:
        print('That\'s not an option!')


# Displays a single stock with chosen parameters
def display_single_stock_prompt():
    print('1. Which stock would you like to see?')
    print('List of companies:')
    print(show_names())
    data1 = input('Enter company: ').lower()

    if data1 == 'tesco':
        d1 = ['TSCO.LON', 'Tesco']
    elif data1 == 'shopify':
        d1 = ['SHOP.TRT', 'Shopify Inc']
    elif data1 == 'greenpower':
        d1 = ['GPV.TRV', 'GreenPower Motor Company Inc']
    elif data1 == "daimler":
        d1 = ['DAI.DEX', 'Daimler AG']

    print('2. Do you wish to see the graph in daily, weekly or monthly changes?')
    data2 = input('Enter time period: ').lower()

    if data2 == 'daily':
        d2 = ['TIME_SERIES_DAILY', 'Time Series (Daily)', 'Daily Changes']
    elif data2 == 'weekly':
        d2 = ['TIME_SERIES_WEEKLY', 'Weekly Time Series', "Weekly Changes"]
    elif data2 == 'monthly':
        d2 = ['TIME_SERIES_MONTHLY', 'Monthly Time Series', 'Monthly Changes']

    print('3. How many of the following days, weeks or months do you wish the graph to display?')
    d3 = int(input())

    display_single_stock.DisplaySingleStock(d1, d2, d3).display_graph()


# Displays two comparable stocks with chosen parameters
def display_compare_stocks_prompt():
    print('1. Which stocks would you like to compare?')
    print('List of companies:')
    print(show_names())

    data1 = input('Enter first company: ').lower()

    if data1 == 'tesco':
        d1 = ['TSCO.LON', 'Tesco']
    elif data1 == 'shopify':
        d1 = ['SHOP.TRT', 'Shopify Inc']
    elif data1 == 'greenpower':
        d1 = ['GPV.TRV', 'GreenPower Motor Company Inc']
    elif data1 == "daimler":
        d1 = ['DAI.DEX', 'Daimler AG']

    data2 = input('Enter second company: ').lower()

    if data2 == 'tesco':
        d2 = ['TSCO.LON', 'Tesco']
    elif data2 == 'shopify':
        d2 = ['SHOP.TRT', 'Shopify Inc']
    elif data2 == 'greenpower':
        d2 = ['GPV.TRV', 'GreenPower Motor Company Inc']
    elif data2 == "daimler":
        d2 = ['DAI.DEX', 'Daimler AG']

    print('2. Do you wish to see the graph in daily, weekly or monthly changes?')
    data3 = input('Enter time period: ').lower()

    if data3 == 'daily':
        d3 = ['TIME_SERIES_DAILY', 'Time Series (Daily)', 'Daily Changes']
    elif data3 == 'weekly':
        d3 = ['TIME_SERIES_WEEKLY', 'Weekly Time Series', "Weekly Changes"]
    elif data3 == 'monthly':
        d3 = ['TIME_SERIES_MONTHLY', 'Monthly Time Series', 'Monthly Changes']

    print('3. How many of the following days, weeks or months do you wish the graph to display?')
    d4 = int(input())

    compare_stocks.CompareStocks(d1, d2, d3, d4).display_graph()


# Displays a single stocks regression with chosen parameters
def display_single_regression_prompt():
    print('1. Which stock would you like to see?')
    print('List of companies:')
    print(show_names())
    data1 = input('Enter company: ').lower()

    if data1 == 'tesco':
        d1 = ['TSCO.LON', 'Tesco']
    elif data1 == 'shopify':
        d1 = ['SHOP.TRT', 'Shopify Inc']
    elif data1 == 'greenpower':
        d1 = ['GPV.TRV', 'GreenPower Motor Company Inc']
    elif data1 == "daimler":
        d1 = ['DAI.DEX', 'Daimler AG']

    print('2. Do you wish to see the graph in daily, weekly or monthly changes?')
    data2 = input('Enter time period: ').lower()

    if data2 == 'daily':
        d2 = ['TIME_SERIES_DAILY', 'Time Series (Daily)', 'Daily Changes']
    elif data2 == 'weekly':
        d2 = ['TIME_SERIES_WEEKLY', 'Weekly Time Series', "Weekly Changes"]
    elif data2 == 'monthly':
        d2 = ['TIME_SERIES_MONTHLY', 'Monthly Time Series', 'Monthly Changes']

    print('3. How many of the following days, weeks or months do you wish the graph to display?')
    d3 = int(input())

    display_regression.DisplayRegression(d1, d2, d3).display_graph()
