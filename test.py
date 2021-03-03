from newsapi import NewsApiClient
from pandas.io.json import json_normalize
import pandas as pd
# Init
newsapi = NewsApiClient(api_key='a0cad01458cc46cf96419b1e0cfc0c8c')

# /v2/everything
all_articles = newsapi.get_everything(q='株式',
                                      from_param='2020-08-20',
                                      to='2020-09-02',
                                      sort_by='relevancy',
                                      page_size=100)

df = pd.DataFrame.from_dict(json_normalize(
      all_articles['articles']), orient='columns')

df.to_csv('test.csv')