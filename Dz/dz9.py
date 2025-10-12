from bs4 import BeautifulSoup
import  requests

response = requests.get("https://bank.gov.ua/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "value index-page"})
    elem_number = 0
    for elem in soup_list:
        if elem_number == 3:
            print(f"Курс долара Національного Банку України: {str(elem)[155:-27]},{str(elem)[165:-15]}")
        elem_number += 1