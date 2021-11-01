#WebCrawling
# Daum News의 기사와 본문을 수집하는 코드

import requests
from bs4 import BeautifulSoup

url = 'https://news.v.daum.net/v/20211026095545660'

# 1. requests 라이브러리 사용해서 url 소스코드 가져오기
result = requests.get(url)
print(result.text)

# 2. beautifulsoup 라이브러리 사용해서 원하는 정보만 추출
doc = BeautifulSoup(result.text, 'html.parser')

#select 사용하여 데이터 수집 => list 타입 []
# h3 tag 중 class가 tit.view인 tag를 가져오세요
title = doc.select('h3.tit_view')[0].get_text()
contents = doc.select('section p')
contents.pop(-1) #기자 정보 삭제

#문자열 총합구하기
content = ''
for info in contents:
    content += info.get_text()

print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('# Title:{}'. format(title))
print('# CONTENT:{}'. format(content))

#자손 선택자
