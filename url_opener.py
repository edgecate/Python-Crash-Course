# Import the webbrowser and math library
import webbrowser
import math

#Custom Function 1 - open 5 URLs in browser
def lookup_stocks():
    # URLs stored as variables
    url_list = ['AAPL',
                'FB',
                'TSLA',
                'AMD',
                'GME']

    # Open the following web pages
    for each_url in url_list:
        webbrowser.open(f'https://finance.yahoo.com/quote/{each_url}')

# Custom Function 2 - calculate number of units we can buy
def calc_units():
    capital = 1000
    amd_price = 110.11

    # How many units of AMD can we buy? 9
    amd_units = math.floor(capital / amd_price)
    print(amd_units)

    # But I want to buy 10 units!!!
    # Is amd_units 10 or more? False
    amd_check = amd_units >= 10
    if(amd_check==True):
        print(f'Yay! We can buy {amd_units} units of AMD!')
    else:
        print(f'Boo! We can only buy {amd_units} of AMD :(')

lookup_stocks()
calc_units()
