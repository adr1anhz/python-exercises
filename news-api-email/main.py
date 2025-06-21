import requests


api_key = "619a1e89c25e494cb45933ef77e16a7f"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=619a1e89c25e494cb45933ef77e16a7f"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])


# 619a1e89c25e494cb45933ef77e16a7f