import requests
from bs4 import BeautifulSoup

def usdrate():
    urlusd = "https://www.bloomberght.com/doviz/dolar"
    r_usd = requests.get(urlusd)
    soup = BeautifulSoup(r_usd.content, "html.parser")
    selection = soup.find("span", {"class": "downRed"})
    selectionrate = soup.find("span", {"class": "bulk"})
    selectiondate = soup.find("span", {"class": "date"})
    print("USD/TRY: ",selection.text," Rate:",selectionrate.text, "Date: ", selectiondate.text)

def eurrate():
    urlusd = "https://www.bloomberght.com/doviz/euro"
    r_usd = requests.get(urlusd)
    soup = BeautifulSoup(r_usd.content, "html.parser")
    selection = soup.find("span", {"class": "downRed"})
    selectionrate = soup.find("span", {"class": "bulk"})
    selectiondate = soup.find("span", {"class": "date"})
    print("EUR/TRY: ",selection.text," Rate:",selectionrate.text, "Date: ", selectiondate.text)   

usdrate()
eurrate()