from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt
from data import API_KEY

ts = TimeSeries(key='API_KEY',output_format='pandas', indexing_type='date')
# Get json object with the intraday data and another with  the call's metadata
# data, meta_data = ts.get_intraday('GOOGL',interval='1min',outputsize='full')
# print(data.head(2))
cc = CryptoCurrencies(key='API_KEY', output_format='pandas')

