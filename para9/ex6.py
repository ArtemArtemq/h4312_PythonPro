from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text,
                         features="html.parser")
    soup_list = soup.find_all("div", {"class": "sc-fa25c04c-0 eAphWs"})
    for elem in soup_list:
        result = elem.find("span")
        print(str(result)[6:-7])

