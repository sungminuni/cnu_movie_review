
 #
 review

 #review score 수집
 score = one.select('div.star_score > em')[0].get_text()

 #review writer 수집
 original_writer = one.select('div.score_reple > p > span')[-1].get_text().strip()
 idx_end = original_writer.find('(')
 writeer = original_writer[0:idx_end]

 #review date 수집
 original_date = one.select('div.score_reple em')[1].get_text()
 date = original_date[0:10]
 print('SCORE => {}'.format(score))
 print('REVIEW => {}'.format(review))
 print('WRITER => {}' .format(original_writer))
 print('DATE => {}' .format(date))

