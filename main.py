import logging
logging.basicConfig(level=logging.INFO)
import os
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'data-analytics-project-234508-6786750ee54c.json'

from news_api_client import NewsApiCaller
from google_cloud_nlp import getSentiment

import pandas as pd

def main_logic(*args):
  logging.info(args)
  countries = {
    'us': ['economy', 'gs://chenfeiyu-data-source/stock_news/stock_news_us.csv'],
    'jp': ['経済', 'gs://chenfeiyu-data-source/stock_news/stock_news_jp.csv'],
    'cn': ['经济', 'gs://chenfeiyu-data-source/stock_news/stock_news_cn.csv'],
  }

  newsClient = NewsApiCaller()
  for key, value in countries.items():
    try:
      lambdafunc = lambda row: pd.Series(getSentiment(row['title']))
      
      logging.info('{}: {}'.format(key, value))
      df = newsClient.getMyHeadlines(query = value[0], country=key)
      if df.empty:
        logging.info('Empty.')
        continue
      else:
        logging.info(df)
      df['country'] = key
      df['type'] = 'headline'
      df[['sentiment_score', 'sentiment_magnitude']] = df.apply(lambdafunc, axis=1)
      df.to_csv(value[1])
    except Exception as e:
      logging.error(str(e))
      
if __name__ == '__main__':
  main_logic()