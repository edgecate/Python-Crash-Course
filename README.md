# Python-Crash-Course
> In this Python tutorial, we automate the day to day task of opening web browsers and webpages. 

Watch the full YT tutorial:

[![IMAGE ALT TEXT](http://img.youtube.com/vi/kkitbPJHGpk/0.jpg)](http://www.youtube.com/watch?v=kkitbPJHGpk "New To Python? Start This 30 Minute Crash Course Now!")

Welcome to this Python For Beginners Crash Course! 😀 

In this Python tutorial, we automate the day to day task of opening web browsers and webpages. 

Problem Statement:
Imagine you're a stock trader and you have 5 hot stocks on your radar. 
Everytime you check these stocks on Yahoo Finance or an exchange, you have to open 5 browser tabs, and manually type in the URLs each time which is tedious!

Solution:
Our Python code will automatically open 5 browser tabs and automatically open the 5 URLs with one click of a button!

By the end of this Python Crash Course, you'll have learnt about:
- 00:24 How To Install Python
- 02:25 Open & Use The Code Editor (IDLE)
- 05:40 Python Libraries
- 08:56 Variables
- 11:21 Lists
- 14:55 For Loops
- 19:48 F-String
- 21:23 Arithmetic Operators
- 23:45 Comparison Operators
- 25:34 If Statements
- 28:20 Custom Functions

I've tried to make this a "Python For Everybody" course by skipping the technical jargon and focusing on solving the problem at hand making this one of the most easiest to understand tutorials on how to learn Python.

```python
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
```
