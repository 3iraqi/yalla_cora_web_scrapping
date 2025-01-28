"""Web Scraping Task That get the match's data

    """

import csv
import requests  # pip install requests
from bs4 import BeautifulSoup as Bs  # pip install beautifulsoup # pip install lxml

date = input("Enter The date eg. 'MM/dd/yyyy' : -> ") # input date from user
# date="01/28/2024"
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}", timeout=20)


def main(page_):
    """_summary_

    Args:
        page_ (_type_): _description_
    """
    src = page_.content
    soup = Bs(src, "lxml")
    matches_details = []
    champion_ships = soup.find_all("div", {"class": "matchCard"})
    # (str tag, dict filter) here we git the main div to championships

    def get_match_info(champion_ship):
        champion_ship_title = champion_ship.contents[1].find("h2").text.strip() 
      
        all_matches = champion_ship.contents[3].find_all("div", {"class": "liItem"})
        
        number_of_matches = len(all_matches)
        
        for i in range(number_of_matches):
            # Get Teams Name
            team_a = all_matches[i].find("div", {"class": "teamA"}).text.strip()
            team_b = all_matches[i].find("div", {"class": "teamB"}).text.strip()

            # Get Score
            match_result = (
                all_matches[i]
                .find("div", {"class": "MResult"})
                .find_all("span", {"class": "score"})
            )
            score = f"({match_result[0].text.strip()} - {match_result[1].text.strip()})"

            # Ger Match time
            match_time = (
                all_matches[i]
                .find("div", {"class": "MResult"})
                .find("span", "time")
                .text.strip()
            )

            # print(teamA)
            # Add Matches Info to matches_details
            matches_details.append(
                {
                    "Champion Type": champion_ship_title,
                    "First Team": team_b,
                    "Second Team": team_a,
                    "Match Time": match_time,
                    "RESULT": score,
                }
            )

    

    # get data
    for champion_ship in champion_ships:
        get_match_info(champion_ship)



    # Save to CSV File
    keys = matches_details[0].keys()

    with open(
        "yallaCora/champion_details.csv", "w", encoding="utf-8-sig", newline=""
    ) as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print(" file Created: ")

    


if __name__ == "__main__":
    main(page)
