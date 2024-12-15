import requests                          # pip install requests
from bs4 import BeautifulSoup as Bs             # pip install beautifulsoup # pip install lxml
import csv                                      

# date=input("Enter The date eg. 'MM/dd/yyyy' : -> ")
date="12/14/2024"
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")

def main(page):
    src = page.content
    soup=Bs(src,"lxml")
    matches_details = []
    championShips = soup.find_all("div",{'class':'matchCard'} )  
    # (str tag, dict filter) here we git the main div to championships 
    # print (championShips)
    
    def get_match_info(championShip):
        championShip_title = championShip.contents[1].find('h2').text.strip() # this is equal the one below.
        # championShip_title = championShip.find('h2').text.strip()
        all_matches = championShip.contents[3]
        print(all_matches)
        ...
        # print (championShip_title)
    get_match_info(championShips[0])
    ...
    
    
if __name__=="__main__":
    main(page)