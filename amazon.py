import urllib
import urllib2
import string
import sys
from bs4 import BeautifulSoup
import sqlite3
import csv
from datetime import date
from time import sleep
import sys
import argparse

#parser = argparse.ArgumentParser(description='Process some integers.')
#parser.add_argument('product', metavar='product', type=str, nargs=1,
#                   help='URL of product')
#parser.add_argument('target', metavar='target',type=float , nargs=1,
#                   help='target price')

#args = parser.parse_args()

reader = csv.reader(open("TestFile.csv","rb"))

for row in reader:
    product = row[0]
    target = float(row[1])

    #product = args.product[0]
    #target = args.target[0]
    csvfile = r'D:\GIST\Personal\Dropbox\amazon.csv'

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:13.0) Gecko/20100101 Firefox/13.0'
    headers = { 'User-Agent' : user_agent }
    request=urllib2.Request(product,None ,headers)
    response = urllib2.urlopen(request)
    the_page = response.read()

    soup= BeautifulSoup(the_page)

    title = soup.find("h1",{"id":"title"})
    con = title.contents

    title = con[0]
    if len(title)>50:
        title = title[0:50]+"..."
 
    price = unicode(soup.find("span",{"id":"priceblock_ourprice"}).string).strip()

    #get rid of dollar sign
    price_dec = float(price[1:])

    today = date.today().strftime("%x")
    f= open(csvfile,"a")
    f.write("\""+today+"\",\""+title+"\",\""+price+"\"\n")
    f.close()

    print price_dec
    print price
    print target
	
    if price_dec <= target:
        print title +" Current Price: "+ price + " Beats target price " + str(target) +" Buy Now!"
        #message =  title + " is on sale for " + price + "\n "+product
        #send_text(message)
		# message sending link: #http://iqjar.com/jar/sending-emails-from-the-raspberry-pi/

    else:
        print title +"Current Price: "+ price + " Does not meet target price. " + str(    target) + " Don't Buy :("

