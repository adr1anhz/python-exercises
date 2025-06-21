import requests
from send_email import send_email


api_key = "619a1e89c25e494cb45933ef77e16a7f"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=619a1e89c25e494cb45933ef77e16a7f"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
# 619a1e89c25e494cb45933ef77e16a7f