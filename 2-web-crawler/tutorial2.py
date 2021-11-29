import csv
import requests
from bs4 import BeautifulSoup

url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'lxml')

info_items = soup.find_all('div', 'release_info')

with open('本週新片.csv', 'w', encoding='utf-8', newline='') as csv_file:
    
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['電影片名', '電影英文片名', '上映時間', '網友期待度'])

    for item in info_items:

        name = item.find('div', 'release_movie_name').a.text.strip()
        english_name = item.find('div', 'en').a.text.strip()
        release_time = item.find('div', 'release_movie_time').text.split('：')[-1].strip()
        level = item.find('div', 'leveltext').span.text.strip()
        
        csv_writer.writerow([name, english_name, release_time, level])
        print('{}({}) 上映日：{} 期待度：{}'.format(name, english_name, release_time, level))

