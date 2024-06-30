import requests
url = "https://countriesnow.space/api/v0.1/countries/population/cities"
test = {
    "city":"delhi"
}
r = requests.post(url=url, data=test)
print(r.status_code)
print(r.json())