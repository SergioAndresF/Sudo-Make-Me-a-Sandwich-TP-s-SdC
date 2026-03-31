import requests
response = requests.get('https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22')
if response:
    print("OK")
else:
    print("not OK")

data = response.json()
not_metadata = data[1]

for i in not_metadata:
    if i["country"]["value"] == "Argentina":
        print("Gini index from Argentina in", i["date"], "is:", i["value"])