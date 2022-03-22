# NOTE: you may have to use the 'pip install' command for the yahoofinancials package
import pandas as pd
from yahoofinancials import YahooFinancials


def grab_index_data(index_list):
    data_list = []
    for index in index_list:
        yahoo_financials = YahooFinancials(index)
        data = yahoo_financials.get_historical_price_data(start_date='2019-10-01',
                                                          end_date='2022-03-18',
                                                          time_interval='daily')
        df = pd.DataFrame(data[index]['prices'])
        df = df.drop('date', axis=1).set_index('formatted_date')
        data_list.append(df)
    return data_list


def main():
    # Indices: S&P 500 (^GSPC), Volatility Index (^VIX), Japanese Nikkei (^N225),
    # Shanghai SSE (000001.SS), Korean KOSPI (^KS11), Eurozone STOXX50E (^STOXX50E)
    index_list = ['^GSPC', '^VIX', '^N225', '000001.SS', '^KS11', '^STOXX50E']
    data_list = grab_index_data(index_list)
    for data in data_list:
        print(data.head())


if __name__ == "__main__":
    main()
