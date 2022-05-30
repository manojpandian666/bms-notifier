import requests
from bs4 import BeautifulSoup
import time
import os

def main():
    while(True):

        # Making a GET request
        mov_url = os.environ.get('mov_url')
        r = requests.get(mov_url)
        
        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')
        
        # Finding all venue list
        s = soup.find('ul', id= 'venuelist')

        # Getting all the title
        title = s.find_all('a', class_='__venue-name')

        cinema_theatres = []

        for name in title:
            #print("Name : ", name.find("strong").text)
            cinema_theatres.append(name.find("strong").text)

        # print(cinema_theatres)
        your_theatre = 'PVR: SKLS Galaxy Mall, Red Hills Chennai'
        if your_theatre in cinema_theatres:
            req_url = 'https://api.telegram.org/bot' + os.environ.get('bot_id') +'/sendMessage?chat_id=' + os.environ.get('chat_id') + '&text=Ticket%20Open%20Aiduchu%20da%20Body%20Soda'
            requests.get(req_url)
        
        time.sleep(10 * 60)


if __name__ == "__main__":
    main()