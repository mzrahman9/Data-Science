import bs4
import requests
from bs4 import BeautifulSoup

   

r= requests.get('https://finance.yahoo.com/trending-tickers')
soup = bs4.BeautifulSoup(r.text,'lxml')
table = soup.find_all('table', class_ = 'yfinlist-table W(100%) BdB Bdc($tableBorderGray)')[0]


with open ('Trending_tickers.txt', 'w') as r:
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            r.write(cell.text.ljust(37))
        r.write('\n')