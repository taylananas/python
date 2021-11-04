import requests
from bs4 import BeautifulSoup

url = "https://www.bloomberght.com/doviz/dolar"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

selection = soup.find("span", {"class": "downRed"})
selectionrate = soup.find("span", {"class": "bulk"})
selectiondate = soup.find("span", {"class": "date"})
print("USD/TRY: ",selection.text," Rate:",selectionrate.text, "Date: ", selectiondate.text)