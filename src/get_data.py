import jqdatasdk as jq
import pandas as pd


def get_data():
    jq.auth('18571461027', 'Pk#941027')
    data = jq.get_price('000001.XSHE',
                        start_date='2024-01-01',
                        end_date='2024-01-31',
                        frequency='daily')
    df = pd.DataFrame(data)
    df.to_csv('data.csv')

if __name__ == '__main__':
    get_data()