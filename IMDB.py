from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.imdb.com/chart/top/')
source.raise_for_status()

soup = BeautifulSoup(source.text,'html.parser')


movies = soup.find('tbody', class_="lister-list").find_all('tr')


for X in movies:
    Name = X.find('td',class_="titleColumn").a.text
    Rank = X.find('td',class_ = "titleColumn").get_text(strip = True).split('.')[0]
    Year = X.find('td',class_="titleColumn").span.text.strip('()')
    Rating = X.find('td',class_="ratingColumn imdbRating").strong.text
            

    print(Rank,Name,Year,Rating)
