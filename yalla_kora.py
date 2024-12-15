import requests                          # pip install requests
from bs4 import BeautifulSoup as Bs             # pip install beautifulsoup # pip install lxml
import csv                                      

date=input("Enter The date eg. 'MM/dd/yyyy' : -> ")
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")

def main(page):
    src = page.content
    soup=Bs(src,"lxml")
    # print (src)
    ...
    
    
if __name__=="__main__":
    main(page)