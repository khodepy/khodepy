#This python script will work through Coin Market Cap API platform
#To use this script, you should sign up cmc pro api.

import requests
import json
from datetime import datetime

base_url = 'https://pro-api.coinmarketcap.com'

print('\n','welcome to cmc data miner v1.0')
print ('''
[1] = latest currencies list
[2] = latest global metrics
[3] = get information about a coin
[4] = exit''')

cmc_api_key = input('Enter your CMC API Key: ')
headers = {'X-CMC_PRO_API_KEY': cmc_api_key}

month = str(datetime.today().month)
day = str(datetime.today().day)
year = str(datetime.today().year)
hour = str(datetime.today().hour)
minute = str(datetime.today().minute)

base_file_name =  year+ '.'+ day+ '.'+ month+ ' '+ hour+ ':'+ minute
choose = input('choose an option : ')

if choose == '1':
    r1 = requests.get(base_url+'/v1/cryptocurrency/listings/latest', headers=headers)
    rank = 0
    your_rank = input('from 1st to ... :')
    #It shows list from the first coin to your considering rank coin.
    for i in range(int(your_rank)):
        inc = r1.json()['data'][rank]
        
        print('Coin name', ' is ',inc['name'], '\n'
            'Coin rank is ', inc['cmc_rank'], '\n'
            'Price ', 'is ', inc['quote']['USD']['price'], '\n'
            'Percent change in the last 24h is', inc['quote']['USD']['percent_change_24h'] ,'\n'
            '#====#====#====#')
        rank += 1
    con = input('If you want a .txt log file, press y (unless print n): ')
    if con == 'y':
        with open(base_file_name+ ' latest list.txt', 'w') as n:
            n.write(str(r1.json()['data'][0:int(your_rank):1]))
#log files will be saved in current working directory.

if choose == '2':
    r2 = requests.get(base_url+ '/v1/global-metrics/quotes/latest', headers=headers)
    log = r2.json()
    log2 = r2.json()['data']

    print('Last Day BTC Dominance: ', log2['btc_dominance_yesterday'], '\n',
         'Today BTC Dominance: ', log2['btc_dominance'], '\n',
         'Last Day ETH Dominance: ', log2['eth_dominance_yesterday'], '\n',
         'Today ETH  dominance: ', log2['eth_dominance'], '\n',
         'Stable Coin Volume in 24h: ', log2['quote']['USD']['stablecoin_volume_24h'], '\n',
         'stable coin Market Cap: ', log2['quote']['USD']['stablecoin_market_cap'], '\n',
         '#====#====#====#')

    con2 = input('If you want a full .txt log file, press y (unless print n): ')
    if con2 == 'y':
        with open(base_file_name+ ' global.metrics.txt', 'w') as m:
            m.write(str(log))
#log files will be saved in current working directory.

if choose == '3':
    print('This part is going to complete in the next version.')
#This part is going to complete in the next version.

if choose == '4':
    print('thank you for using cmc data miner v1.0')