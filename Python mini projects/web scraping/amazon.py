# importing libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import datetime
import smtplib
import pandas as pd

# putting all together
def price_check():
    URL = 'https://www.amazon.com/Harbor-Bay-Crewneck-T-Shirts-5XLTall/dp/B00A3HLF9A/ref=sr_1_2?crid=1F8GL99I6D9VX&keywords=data+tshirt+men&qid=1645994016&rnid=2941120011&s=apparel&sprefix=data+tshirt%2Caps%2C585&sr=1-2'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)   

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id='productTitle').get_text()
    review = soup2.find("span", {"class":"a-icon-alt"}).get_text()
    price = soup2.find("span", {"class":"a-offscreen"}).get_text()
    total_reviews= soup2.find(id="acrCustomerReviewText").get_text()

    print("the title of product is : " ,title)
    print("the rating of product is : " ,review)
    print("the price of product is : " ,price)
    print("the total reviews of product are : " ,total_reviews)

    today = datetime.date.today()
    title = title.strip()
    price = price.strip()
    review = review.strip()

    head = ['Title', 'Price','Rating','Date']
    data = [title,price,review,today]

    with open('amazon.csv','a+', newline='', encoding= 'UTF8') as f:
        

        wr = csv.writer(f)
        wr.writerow(data)
price_check()