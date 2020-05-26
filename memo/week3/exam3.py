import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a_tag = movie.select_one('td.title > div > a')
    print(type(a_tag))
    # if a_tag is not None:
    # a_tag.select_one('a'))
        # print(a_tag)
    # if a_tag is not None:
    #     print (a_tag.text)


