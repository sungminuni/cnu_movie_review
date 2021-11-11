#네이버 특정 영화 코드 입력-> 해당 영화 리뷰 수집 프로그램

import math
import requests
from bs4 import BeautifulSoup

#네이버 영화 코드
movie_code = '209496' #고장난 론
count = 0
################
# 1. Title 수집 #
################
title_url = 'http://movie.naver.com/movie/bi/mi/basic.naver?code={}'.format(movie_code)
result = requests.get(title_url)
doc = BeautifulSoup(result.text, 'html.parser')

title = doc.select('h3.h_movie > a')[0].get_text()

#############################
# 2. 리뷰 전체 수와 페이지 계산 #
#############################
#2-1.영화 total review count
all_count = doc.select('strong.total > em')[0].get_text().strip()
# 2-2. 해당 영화 전체 페이지 수 계산
pages = math.ceil(int(all_count) / 10)

######################################
# 3. 리뷰 수집(리뷰, 평점, 작성자, 날짜) #
######################################
for page in range(1, pages+1):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    result = requests.get(url, headers=headers)
    doc = BeautifulSoup(result.text, 'html.parser')

    review_list = doc.select('div.score_result > ul > li')

    for i, one in enumerate(review_list):
        count += 1
        print('## USER -> {} #######################################################################'.format(i + 1))

        # 평점 정보 수집
        score = one.select('div.star_score > em')[0].get_text()

        # 리뷰 정보 수집
        review = one.select('div.score_reple > p > span')[-1].get_text().strip()

        # 작성자(닉네임) 정보 수집
        original_writer = one.select('div.score_reple dt em')[0].get_text().strip()

        idx_end = original_writer.find('(')
        writer = original_writer[:idx_end]

        # 날짜 정보 수집
        original_date = one.select('div.score_reple dt em')[1].get_text()
        date = original_date[:10]

        # yyyy.MM.dd 전처리 코드 작성
        print(':: REVIEW -> {}'.format(review))
        print(':: WRITER -> {}'.format(writer))
        print(':: SCORE -> {}'.format(score))
        print(':: DATE -> {}'.format(date))

