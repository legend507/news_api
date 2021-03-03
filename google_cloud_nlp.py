
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

googleNlpClient = language.LanguageServiceClient()

def getSentiment(text):
  document = {
    'content': text,
    'type': enums.Document.Type.PLAIN_TEXT,
  }
  encoding = enums.EncodingType.UTF8
  
  sentiment = googleNlpClient.analyze_sentiment(
    document=document, encoding_type=encoding)
  
  # score: [-1, 1], magnitude: [0, infinite]
  # explanation: https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values
  return [sentiment.document_sentiment.score, sentiment.document_sentiment.magnitude]
