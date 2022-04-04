# Imports
import pandas as pd


# Creates a company dataframe from lists.
# Used for the user and for the API
def companies_list():
    # TESCO PLC (London Stock Exchange)
    tesco = ['TSCO.LON', 'Tesco']

    # Shopify Inc (Canada - Toronto Stock Exchange)
    shopify = ['SHOP.TRT', 'Shopify Inc']

    # GreenPower Motor Company Inc (Canada - Toronto Venture Exchange)
    greenpower = ['GPV.TRV', 'GreenPower Motor Company Inc']

    # Daimler AG (Germany - XETRA)
    daimler = ['DAI.DEX', 'Daimler AG']

    combined_list = pd.DataFrame({'Tesco': tesco, 'Shopify': shopify, 'Greenpower': greenpower, 'Daimler': daimler})

    return combined_list


# Prints every company name
def show_company_names():
    company_names = []
    data = companies_list()

    for x in data:
        company_names.append(x)

    return company_names
