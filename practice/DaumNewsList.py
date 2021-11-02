# 다음뉴스 목록을 for문 돌며 제목과 본문 수집

import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

url_list = doc.select('ul.list_news2 a.link_txt')
print(len(url_list))

for i, href in enumerate(url_list):
    new_url = href['href']

    result = requests.get(new_url)
    print(result.text)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.tit_view')[0].get_text()
    contents = doc.select('section p')
    contents.pop(-1)
    content = ''
    for info in contents:
        content += info.get_text()

    print('■■NEWS -> {} ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'.format(i+1))
    print('# URL:{}'.format(new_url))
    print('# Title:{}'.format(title))
    print('# CONTENT:{}'.format(content))