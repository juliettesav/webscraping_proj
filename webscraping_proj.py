from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests 
print()

url = 'https://coinmarketcap.com/' 
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, 'html.parser')


title = soup.title

print(title.text)
print()

tablerows = soup.findAll('tr')

for row in tablerows[1:6]:
    td = row.findAll("td")
    num = td[1].text.replace("\n","")
    name = td[2].p.text
    symbol = ((td[9].p.text).split()[1])
    price = td[3].text.replace("\n","")
    price2 = str((price).replace(",",""))
    price3 = float((price2).replace("$",""))
    change = td[5].text.replace("%\n","")
    change2 = float((change).replace("%",""))
    calc_change = round((price3 + (price3 * change2)),2)

    print(f"{num}\nName: {name}\nSymbol: {symbol}\nCurrent Price: {price}\n% Change in 24 hrs: {change2}%\nCorresponding Price: ${calc_change}\n")

    if symbol == 'BTC':
        if price3 < 40000: 
            BTCalert = 'The value of BTC is below $40,000.'
        else: 
            BTCalert = ''

    if symbol == 'ETH':
        if price3 < 3000: 
            ETHalert = 'The value of ETH is below $3,000.'
        else: 
            ETHalert = ''

print(BTCalert)
print(ETHalert)
print()


import keys 
from twilio.rest import Client 

client = Client(keys.accountSID, keys.authToken)

TwilioNumber = "+12107504781"
myCellphone= '+17146045116'

if BTCalert != '':
    textmsg = client.messages.create(to=myCellphone,from_=TwilioNumber,body=BTCalert)
    print(textmsg.status)

if ETHalert != '':
    textmsg2 = client.messages.create(to=myCellphone,from_=TwilioNumber,body=ETHalert)
    print(textmsg2.status)