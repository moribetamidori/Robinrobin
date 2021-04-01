# from data import API_KEY
import pandas as pd
import datetime 
import requests
from bs4 import BeautifulSoup
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style

def real_time_price(code):# work for both stock and crypto 
    url = ('https://finance.yahoo.com/quote/')+code
    r = requests.get(url)
    web_content = BeautifulSoup(r.text,'lxml')
    web_content = web_content.find('div', class_='D(ib) Mend(20px)' )
    web_content = web_content.find('span').text
    if web_content == []:
        web_content = np.nan
    return web_content
    # print(web_content)

# crypto, remember to have crypto-USD
# real_time_price('GOOG')
HSI = ['ETH-USD','GOOG','TSLA','BTC-USD']
for step in range(1,101):
    price = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    for stock in HSI:
        price.append(real_time_price(stock))
    col = [time_stamp]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('real time stock data.csv',mode='a',header=False)
    print(col)

