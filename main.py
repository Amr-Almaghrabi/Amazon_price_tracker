import requests
from bs4 import BeautifulSoup
import lxml

import smtplib

URL = #Enter the amazon link to the prodyct you want to track

HEADERS = {
    "User-Agent": "Defined",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,km;q=0.5,zh-TW;q=0.4",
}

#if this response fails add the parameter headers with the value HEADERS ^
response = requests.get(url=URL)
html = response.text
soup = BeautifulSoup(html, 'lxml')

price = float(soup.find("span", class_="a-price-whole").text.strip('.')) + (
            float(soup.find("span", class_="a-price-fraction").text) / 100)

if price < #Enter price target you want :
    fromaddress = #email address to send from
    toaddrs = #Email address you want to email
    msg = f"The product your looking for is cheaper than the target price, get it now at: {URL}"
    username = #enter your email username
    password = #create an app password in your email and send it here
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr=fromaddress, to_addrs=toaddrs, msg=msg)
    server.quit()
