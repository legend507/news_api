import logging

from newsapi import NewsApiClient

from pandas.io.json import json_normalize
import pandas as pd


class NewsApiCaller(NewsApiClient):
  def __init__(self, 
               API_KEY='a0cad01458cc46cf96419b1e0cfc0c8c'):
    self.client = NewsApiClient(api_key=API_KEY)
    
  def getMySource(self):
    sources = self.client.get_sources()
    df = pd.DataFrame.from_dict(
      json_normalize(sources['sources']), orient='columns')
    return df
  
  def getMyHeadlines(self, 
                   query='stock market', 
                   category='business', 
                   country='us'):
    headlines = self.client.get_top_headlines(
      q=query,
      category=category,
      country=country,
      page_size=100,
    )
    logging.info('{}: {}'.format(country, headlines))
    df = pd.DataFrame.from_dict(json_normalize(
      headlines['articles']), orient='columns')
    return df
  
  def getMyEverything(self,
                      query,
                      start_date,
                      end_date):
    everything = self.client.get_everything(
      q=query,
      from_param=start_date,
      to=end_date,
      sort_by='relevancy',
      page_size=100
    )
    df = pd.DataFrame.from_dict(json_normalize(
      everything['articles']), orient='columns')
    return df