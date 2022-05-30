import requests
from bs4 import BeautifulSoup
import time

def main():
    while(True):

        # Making a GET request
        r = requests.get('https://in.bookmyshow.com/buytickets/vikram-chennai/movie-chen-ET00138591-MT/20220603')
        
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
            requests.get('https://api.telegram.org/bot1405308860:AAHdylsTGBk5IZXFitPgriwIfpP8XbWas5o/sendMessage?chat_id=928275224&text=Ticket%20Open%20Aiduchu%20da%20Body%20Soda')
        
        time.sleep(10 * 60)


if __name__ == "__main__":
    main()