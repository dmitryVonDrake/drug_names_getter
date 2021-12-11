from bs4 import BeautifulSoup
import requests
import time

URL = 'https://samson-pharma.ru/alphabet/'
LIST_OF_SYMBOLS = [
    'a/',
    'b/',
    'v/',
    'g/',
    'd/',
    'e/',
    'zh/',
    'z/',
    'i/',
    'k/',
    'l/',
    'm/',
    'n/',
    'o/',
    'p/',
    'r/',
    's/',
    't/',
    'u/',
    'f/',
    'kh/',
    'ts/',
    'ch/',
    'sh/',
    'eh/',
    'yu/',
    'ya/']


def get_all_drug_names(url, list_of_symbols):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    all_drugs = []
    for symbol in list_of_symbols:
        link = url + symbol
        page = (requests.get(link, headers=headers)).text
        print(link)
        data = ((BeautifulSoup(page, 'html.parser')).find_all('a', class_='alphabet__item'))
        for info in data:
            all_drugs += info
        time.sleep(60)
    return all_drugs
    
drugs = get_all_drug_names(URL, LIST_OF_SYMBOLS)
print(drugs)

with open('file', 'w') as f:
    for drug in drugs:
        f.write("%s\n" % drug)