import requests                          # pip install requests
from bs4 import BeautifulSoup as Bs             # pip install beautifulsoup # pip install lxml
import csv                                      

date=input("Enter The date eg. 'MM/dd/yyyy' : -> ")
# date="12/14/2024"
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
        all_matches = championShip.contents[3].find_all("div",{'class':'liItem'})
        number_of_matches = len(all_matches)
        for i in range(number_of_matches):
            # Get Teams Name
            teamA=all_matches[i].find('div',{'class':'teamA'}).text.strip()
            teamB=all_matches[i].find('div',{'class':'teamB'}).text.strip()
            
            # Get Score
            match_result = all_matches[i].find("div",{'class':'MResult'}).find_all('span',{'class':'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            
            # Ger Match time 
            match_time = all_matches[i].find('div',{'class':'MResult'}).find('span','time').text.strip()
            
            # print(teamA)
            # Add Matches Info to matches_details
            matches_details.append({
                'Champion Type':championShip_title,
                'First Team':teamA,
                'Second Team':teamB,
                'Match Time':match_time,
                'RESULT':score,
                })
            
            
        
        
    
    for i in range(len(championShips)):
        get_match_info(championShips[i])    
    
    # Save to CSV File
    keys=matches_details[0].keys()
    
    with open('yallaCora/champion_details.csv', 'w' , encoding='utf-8', newline="") as output_file:
        dict_writer   = csv.DictWriter(output_file, keys) 
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print(" file Created: ")
        
    
    
    # "C:\Users\Mohamed\Desktop"
if __name__=="__main__":
    main(page)