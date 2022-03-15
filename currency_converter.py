from argparse import ONE_OR_MORE
from ast import If, While
from asyncore import loop
from operator import truediv
from socket import if_indextoname
from tkinter import ON
from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter

test = CurrencyCodes()

EUR_symbol = test.get_symbol('EUR')
EUR_name = test.get_currency_name('EUR')


BTC_symbol = test.get_symbol('BTC')
BTC_name = test.get_currency_name('BTC')


while True:
    one_or_two = input("\n"'Type 1 or 2'"\n""\n"'Convert Bitcoin to Euros: 1'"\n"'Convert Euros to Bitcoin: 2'"\n""\n")
    if one_or_two == '1':
        break
    if one_or_two == '2':
        break
    

bitcoin = BtcConverter()
BTC_price = bitcoin.get_latest_price('EUR')

while one_or_two == '2':
    try:
        EUR_input = int(input("\n"'Write the number of '+ EUR_name +' that you would like to convert in ' + str(BTC_symbol) + 'itcoin:'"\n""\n"))
        EURtoBTC_converted = int(EUR_input)/int(BTC_price)
        print("\n" + str(EUR_input) + str(EUR_symbol) + ' would be ' + str(EURtoBTC_converted) + ' ' + str(BTC_symbol) + 'itcoins')
        break
    except ValueError: 
        loop


while one_or_two == '1':
    try:
        BTC_input = int(input("\n"'Write the number of '+ BTC_name +' that you would like to convert in ' + str(EUR_symbol) + 'uropean Euros:'"\n""\n"))
        BTCtoEUR_converted = int(BTC_input * BTC_price)
        print("\n" + str(BTC_input) +' '+ str(BTC_symbol) + 'itcoin would be ' + str(BTCtoEUR_converted) + ' ' + str(EUR_symbol) + 'uropean Euros')
        break
    except ValueError:
        loop

input()