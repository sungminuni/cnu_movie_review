# page 돌면서 news 목록의 제목과 본문 수집

import requests
from bs4 import BeautifulSoup

# -> ?page=숫자 는 페이지 지정
i = 0
for page_num in range(1, 3):
  url = 'https://news.daum.net/breakingnews/digital?page={}' .format(page_num)
  result = requests.get(url)
  doc = BeautifulSoup(result.text, 'html.parser')

  result = requests.get(url)
  doc = BeautifulSoup(result.text, 'html.parser')

  url_list = doc.select('ul.list_news2 a.link_txt')

  for href in url_list:
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

    i += 1 #News count
    print('■■NEWS -> {} ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'.format(i))
    print('# URL:{}'.format(new_url))
    print('# Title:{}'.format(title))
    print('# CONTENT:{}'.format(content))