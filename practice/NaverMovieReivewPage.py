#네이버 특정 영화 코드 입력-> 해당 영화 리뷰 수집 프로그램

import requests
from bs4 import BeautifulSoup

#네이버 영화 코드
movie_code = '209496' #고장난 론

################
# 1. Title 수집 #
################
title_url = 'http://movie.naver.com/movie/bi/mi/basic.naver?code={}'.format(movie_code)
result = requests.get(title_url)
doc = BeautifulSoup(result.text, 'html.parser')

title = doc.select('h3.h_movie > a')[0].get_text()
print(title)