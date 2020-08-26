
#기사 가져오는 역할
from get_news_functions import *

KEYWORD =input("키워드를 입력하세요 : ") # 검색하려는 keyword 입력 (서울경제 기준 검색)
URL = f"https://search.daum.net/search?nil_suggest=btn&w=news&cluster=y&q={KEYWORD}&cpname=서울경제&cp=16Fbn8iLTIqdeOvaST"
contents = []

NUM_PAGES = get_page_num(URL) #읽어들일 페이지 수 (서울경제 기준 페이지당 기사 10 개 )

links = get_news_daum(URL,NUM_PAGES)

create_news_files(links,contents)

create_morph_files(contents)

get_noun_files(len(contents))

create_dic(len(contents))
