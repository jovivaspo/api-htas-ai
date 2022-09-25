from cgitb import text
from transformers import pipeline

model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"

def analyze(text):
 new_text = []

 for t in text.split(" "):
       t = '@user' if t.startswith('@') and len(t) > 1 else t
       t = 'http' if t.startswith('http') else t
       new_text.append(t)

 text = " ".join(new_text)
 model_path = 'cardiffnlp/twitter-roberta-base-sentiment-latest'
 sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
 sentiment = sentiment_task(text)

 return sentiment
   

