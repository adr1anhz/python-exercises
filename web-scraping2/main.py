import requests
import selectorlib
import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%d-%m-%Y-%H:%M:%S")

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value

def store(extracted):
     with open("logs.txt", "a") as file:
          file.write(extracted + "\n")



if __name__ == "__main__":
        scraped = scrape(URL)
        extracted = extract(scraped)
        data_to_store = formatted_time + "," + extracted
        store(data_to_store)