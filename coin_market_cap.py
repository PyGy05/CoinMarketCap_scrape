from scrape import lst, row, length, crypto_lst, price_lst, market_cap_lst, volume_lst, supply_lst, change_lst

import csv
from prettytable import PrettyTable
import re
from colorama import Fore, Back, Style
from operator import itemgetter

# print("this is price list --> ", price_lst)



#
# def change_color(crypto, price, marketcap, volume, csupply, change):
#     cl = []
#     v = 0
#     name_c = crypto_lst[v]
#     price_c = price_lst[v]
#     if int(price_c) > 0:
#         price_c = Fore.GREEN + Style.RESET_ALL
#     else:
#         price_c = Fore.RED + Style.RESET_ALL
#     market_c = market_cap_lst[v]
#     if market_c > 0:
#         market_c = Fore.GREEN + Style.RESET_ALL
#     else:
#         market_c = Fore.RED + Style.RESET_ALL
#
#     volume_c = volume_lst[v]
#     if volume_c > 0:
#         volume_c = Fore.GREEN + Style.RESET_ALL
#     else:
#         volume_c = Fore.RED + Style.RESET_ALL
#
#     supply_c = supply_lst[v]
#     change_c = change_lst[v]
#     if change_c > 0:
#         change_c = Fore.GREEN + Style.RESET_ALL
#     else:
#         change_c = Fore.RED + Style.RESET_ALL
#
#     cl.append(name_c)
#     cl.append(price_c)
#     cl.append(market_c)
#     cl.append(volume_c)
#     cl.append(supply_c)
#     cl.append(change_c)
#     return cl

# print(change_color(crypto_lst, price_lst, market_cap_lst, volume_lst, supply_lst, change_lst))



x = PrettyTable()

x.field_names = ["Name", "Price", "Market Cap", "Volume(24h)", "Circulating Supply", "Change(24h)"]
x.align["Name"] = "l"
x.align["Price"] = "l"
x.align["Market Cap"] = "l"
x.align["Volume(24h)"] = "l"
x.align["Circulating Supply"] = "l"
x.align["Change(24h)"] = "r"

def add_row(data):
    i = 0
    while i < len(data):
        x.add_row(data[i])
        i += 1


# current top 20 on coin market cap
def top20(row):
    t20 = []
    i = 0
    while i < 20:
        r = [item[i] for item in row]
        t20.append(r)
        # print(r)
        i += 1
    return t20


# scrape top 40 on coin market cap
def top40(row):
    t40 = []
    i = 0
    while i < 40:
        r = [item[i] for item in row]
        t40.append(r)
        # print(r)
        i += 1
    return t40


# scrape top 100 on coin market cap
def top100(row):
    t100 = []
    i = 0
    while i < 100:
        r = [item[i] for item in row]
        t100.append(r)
        # print(r)
        i += 1
    return t100


top20 = top20(row)
add_row(top20)
print(Fore.BLUE + "List of top 20 Cryptocurrencies on Coin Market Cap: " + Style.RESET_ALL, x)
print("\n\n")



top40 = top40(row)
add_row(top40)
print(Fore.BLUE + "List of top 40 Cryptocurrencies on Coin Market Cap: " + Style.RESET_ALL, x)
print("\n\n")

top100 = top100(row)
add_row(top100)
print(Fore.BLUE + "List of top 100 Cryptocurrencies on Coin Market Cap: " + Style.RESET_ALL, x)
print("\n\n")

day_change = x.get_string(fields=["Change(24h)"])
price_change = x.get_string(fields=["Price"])
# print(price_change)
# remove the '$' to convert str into float
ns = []
s = str(day_change)
remove_s = s.replace('%', '')
ns.append(remove_s)
# `print(remove_s)`


# if change24 < 0 GREEN else RED
# rp = []
# t = top20[0][:]
# t1 = t[1]
# print(type(t1))
# print(t1)
# r_t1 = t1.replace('$', '')
# rp.append(r_t1)
# x = rp[0]
# print(Fore.GREEN + t1 + Style.RESET_ALL)

# x2 = PrettyTable()
#
# x2.field_names = ["Name", "Price", "Market Cap", "Volume(24h)", "Circulating Supply", "Change(24h)"]
# x2.align["Name"] = "l"
# x2.align["Price"] = "l"
# x2.align["Market Cap"] = "l"
# x2.align["Volume(24h)"] = "l"
# x2.align["Circulating Supply"] = "l"
# x2.align["Change(24h)"] = "r"


#TODO: Fix table to change colors on %change

# def color_code():
#     r = 0
#     c = 0
#     new_color_table = []
#



# # ['Bitcoin', '$10,688.74', '$197,624,834,483', '$38,888,703,636', '18,489,068 BTC', '3.74%']
#     while r < 20:
#         # first row in table
#         t = top20[r][:]
#         # print(t)
#         # t = Fore.BLUE + t + Style.RESET_ALL
#         # print(t)
#         # 6 columns in eack row
#         if True:
#             t0 = t[0]
#             # t0 = Fore.BLUE + t0 + Style.RESET_ALL
#
#             t1 = t[1]
#             # t1 = Fore.BLUE + t1 + Style.RESET_ALL
#
#             t2 = t[2]
#             # t2 = Fore.BLUE + t2 + Style.RESET_ALL
#
#
#             t3 = t[3]
#             # t3 = Fore.BLUE + t3 + Style.RESET_ALL
#
#
#             t4 = t[4]
#             # t4 = Fore.BLUE + t4 + Style.RESET_ALL
#
#
#             t5 = t[5]
#             r_c = t5.replace('%', '')
#             r_c = float(r_c)
#             # check if number is > 0 if so print in green
#             if r_c > 0:
#                 t5 = Fore.GREEN + t5 + Style.RESET_ALL
#
#
#
#
#             else:
#                 t5 = Fore.RED + t5 + Style.RESET_ALL
#
#                 # x2x= [t0, t1, t2, t3, t4, t5]
#                 # converted_list = [str(element) for element in x2x]
#                 # joined_string = ", ".join(converted_list)
#                 # # print(joined_string)
#                 # res = joined_string.strip('][').split(', ')
#
#
#
#
#
#             ncl = [[t0] + [t1] + [t2] + [t3] + [t4] + [t5]]
#             print(ncl)
#
#             r += 1
#
#
# color_code()
#








