import requests  # alows us to download the html
# allows us to use the data we gathered to do whatever we want with it - to scrape it
from bs4 import BeautifulSoup
import pprint
from operator import itemgetter

res = requests.get('https://coinmarketcap.com')
res2 = requests.get('https://coinmarketcap.com/widget/')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.cmc-link')
links2 = soup.select('.css-xp4uvy cmc-select__single-value')

coin_abrv = soup.select ('cmc-static-icon cmc-static-icon-1027')

coin = soup.find_all(
    'div', {'class': 'sc-1kxikfi-0 fjclfm cmc-table__column-name'})
name = soup.find_all('td', {
                     'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name'})


price = soup.find_all('td', {
    'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'})

market_cap = soup.find_all(
    'td', {'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'})

volume24 = soup.find_all('td', {
                         'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h'})

circulating_supply = soup.find_all(
    'td', {'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply'})


change24 = soup.find_all(
    'td', {'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h'})

price_grapg7d = (
    'td', {'class': "cmc-table__cell cmc-table__cell--right"})

ticker = soup2.find_all(
    'div', {'class': 'css-xp4uvy cmc-select__single-value'})

menu = soup2.find_all(
    'div', {'class': 'css-15k cmc-select__menu'})

def coinMarketCap(data):
    cmc = []
    for idx, item in enumerate(data):
        info = item.getText()
        cmc.append(info)
    return cmc


crypto = coinMarketCap(name)
current_price = coinMarketCap(price)
current_market_cap = coinMarketCap(market_cap)
current_volume = coinMarketCap(volume24)
current_supply = coinMarketCap(circulating_supply)
percent_change = coinMarketCap(change24)
# ticker = crypto_ticker(ticker)
# menu = crypto_ticker(menu)
# print(ticker)
# print(menu)


lst = [[crypto] + [current_price] + [current_market_cap] +
       [current_volume] + [current_supply] + [percent_change]]

color_lst = []

row = lst[0]
crypto_lst = [item[0] for item in lst]
price_lst = [item[1] for item in lst]
market_cap_lst = [item[2] for item in lst]
volume_lst = [item[3] for item in lst]
supply_lst = [item[4] for item in lst]
change_lst = [item[5] for item in lst]

def list_to_float(list_obj):
    ltf = []
    for i in list_obj:
        f = float(i)
        ltf.append(f)

    return ltf


def Extract_row(lst):
    return list(zip(*lst))


# lst_price_floats = [float(item) for item in current_price]


# print(list_to_float(current_price))
length = len(crypto)

# remove the '$' to convert str into float
# ns = []
# s = str(current_price)
# remove_s = s.replace('$', '')
# ns.append(remove_s)

ns = []
s = str(price_lst[0])
rs = s.replace('$', '')
ns.append(rs)



# print(s)
# for i in s:
#     print(i)