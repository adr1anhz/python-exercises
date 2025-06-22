import requests
from send_email import send_email

topic = "tesla"
api_key = "619a1e89c25e494cb45933ef77e16a7f"
url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}&language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
        + "\n" + body + article["title"] \
        + "\n" + article["description"] \
        + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)