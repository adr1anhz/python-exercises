import requests

API_key = "1d2491f3e10ae98bce335ef3a9c9743c"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?id={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__=="__main__":
    print(get_data(place="Tokyo"))