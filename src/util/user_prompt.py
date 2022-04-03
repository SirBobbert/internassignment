def Welcome():
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
        DisplaySingleStockPrompt()
    elif question == 2:
        DisplayCompareStocksPrompt()
    elif question == 3:
        DisplaySingleRegressionPrompt()
    else:
        print('That\'s not an option!')


def DisplaySingleStockPrompt():
    print('You chose single stock')
    print('In order for you to watch a stock, you need to anwser the following questions')
    print('1. Which stock would you like to see?')
    print('2. Do you wish to see the graph in days, weeks or months?')
    print('3. How many of the following days, weeks or months do you wish the graph to display?')
    print('Example: ''Tesco, ''', '''days, ''', '''30''')
    print('List of companies:', )
    data1 = input('Company: ')
    data2 = input('Time period: ')
    data3 = input('Amount of period: ')

    print(data1, data2, data3)



def DisplayCompareStocksPrompt():
    print('You chose compare stocks')


def DisplaySingleRegressionPrompt():
    print('You chose stock regression')


Welcome()
