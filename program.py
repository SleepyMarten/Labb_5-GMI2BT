import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


csv_path = 'datasets/bitcoin.csv'
#csv_path = 'datasets/coin_bitcoin.csv'
df = pd.read_csv(csv_path, delimiter = ';', encoding='utf-8-sig')

''' Show a line chart of bitcoins value per year from year 2013-2021.'''
def show_line():
    data = df[['High','Low',]] #Volume and price of bitcoin
    year = df['Date'] #Year
    plt.plot(year,data)
    plt.title('Bitcoin price comparison 2013-2021')
    plt.xlabel('Year')
    plt.ylabel('Bitcoin Highest and Lowest price')
    plt.legend(data, loc='upper left')
    plt.show()
    
    #what are the max and min of bitcoin prices.
    ''' Finding max and min of High and Low of Bitcoin'''
    max_high = np.max(df['High'])
    min_high = np.min(df['High'])
    
    max_low = np.max(df['Low'])
    min_low = np.min(df['Low'])
    print(f'Highest price of High : {max_high}')
    print(f'Lowest price of High : {min_high}')
    print(f'Highest price of Low : {max_low}')
    print(f'Lowest price of Low : {min_low}')
    print("\n")
    
def show_volume():
    data = df['Volume']
    year = df['Date']
    plt.plot(year,data)
    plt.xlabel('Year')
    plt.title('Bitcoin volume from 2013-2021')
    plt.ylabel('Volume of Bitcoin scale : 1 unit ≈ 100 million')
    plt.legend(df['Volume'], loc='upper left')
    plt.show()
    
    ''' Finding quantile of Bitcoin value, and min max of Prices (High and Low) of Bitcoin.'''
    vol25 = np.quantile(df['Volume'],0.25)
    vol50 = np.quantile(df['Volume'],0.50)
    vol75 = np.quantile(df['Volume'],0.75)
    vol_median = np.median(df['Volume'])
    
    print(f'Quantile of volume (25): {vol25}')
    print(f'Quantile of volume (50): {vol50}')
    print(f'Quantile of volume (75): {vol75}')
    print("\n")
    print(f'Median of volume : {vol_median}')
    
    #what is the highest volume of bitcoin?
    max_vol = np.max(df['Volume'])
    min_vol = np.min(df['Volume'])
    
    print(f'Highest volume : {max_vol}')
    print(f'Lowest volume : {min_vol}')
    print("\n")


    '''Showing a bar graph of the marketcap of Bitcoin per volume. '''
def show_bar():
    data = df[['Marketcap','Volume']]
    data.plot.bar( x = 'Volume')
    plt.title('Bitcoin Marketcap and Volume comparison and relation')
    plt.xlabel('Bitcoin Volume')
    plt.ylabel('Bitcoin Marketcap scale: 1 unit ≈ 10 Billion')
    plt.show()
    
    #what is the median of the marketcap for bitcoin.
    avg_marketcap = df['Marketcap'].median()
    print(f'Median of Marketprice : {avg_marketcap}')
    
    #print('How much has bitcoins marketprice risen since 2013?')
    max_market = np.max(df['Marketcap'])
    min_market = np.min(df['Marketcap'])
    risen_market = max_market - min_market
    increased_market = risen_market/min_market*100
    
    print(f'Since 2013 the marketprice has risen {risen_market}, which is an increase of {increased_market}%')

show_line()
show_volume()
show_bar()