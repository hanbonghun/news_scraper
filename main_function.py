import os
import numpy as np
from konlpy.tag import Komoran
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import MeCab
import json
mecab_tagger = MeCab.Tagger()
komaran = Komoran()

# 저장된 웹페이지의 제목과 내용을 각각의 list에 담음
def get_titles_and_contents(NUM_OF_ARTICLES):
    titles = []
    contents = []
    os.chdir("C:/Users/hanbonghun/Desktop/newsscrapping/news")
    for i in range(NUM_OF_ARTICLES):
        with open(f'{i+1}.txt',"r",encoding="utf-8") as f:
            title = f.readline().strip()
            content = f.read().strip()
            titles.append(title)
            contents.append(content)
    return titles,contents

# 웹페이지의 제목을 출력 (20개씩)
def print_articles_list(articles_per_page,page,titles):
    print("\n========================기사 목록==========================\n")
    for i, v in enumerate(titles[articles_per_page*(page-1):articles_per_page*(page)]):
        print(i+articles_per_page*(page-1)+1,":",v)
    print(f"\n=======================<<{page}페이지>>========================\n")

# 문서의 유사도를 분석하고 nxn 배열 형태로 반환
def get_similarity(contents):
    vect = TfidfVectorizer(min_df=1, stop_words="english")
    tfidf = vect.fit_transform(contents)
    pairwise_similarity = tfidf * tfidf.T
    return pairwise_similarity.toarray()

# 유사도를 바탕으로 특정 기사의 유사 기사 목록 출력
def print_similar_doc(similarities,index,titles):
    print("\n<유사 기사 목록>")
    dic = dict()
    origin = similarities[index]
    for i in range(len(origin)):
        dic[i] = origin[i]
    dic = sorted(dic.items(), reverse=True, key=lambda item: item[1])
    for i in range(5):
        print(f"{i+1}:",titles[dic[i+1][0]])
    print('\n')

# 문서 내 최빈 단어를 찾아 출력
def get_top_rank_words(index):
    os.chdir("C:/Users/hanbonghun/Desktop/newsscrapping/news_nouns")
    with open(f"{index+1}_noun.json", encoding="utf8")as f:
        json_data = json.load(f)
    keys =[]
    for key in json_data.keys():
        keys.append(key)
    print("<최빈단어>")
    for i in range(5):
        print(f"{i+1}:",keys[i])
    print('\n')

# 특정 단어를 가장 많이 포함하는 문서를 최대 5개까지 출력
def get_article_by_word(word,titles):
    os.chdir("C:/Users/hanbonghun/Desktop/newsscrapping/news_nouns")
    a = False
    word_num = {}
    for i in range(len(titles)):
        with open(f'{i+1}_noun.json', 'r',encoding="utf8") as f:
            json_data = json.load(f)
        keys =[]
        for key in json_data.keys():
            keys.append(key)
        result = 0
        for j  in range(len(keys)):
            if word in keys[j]:
                a=True
                result = result+json_data[keys[j]]
        word_num[i]=result
    list = sorted(word_num.items(), key=lambda x: x[1], reverse=True)
    if a ==False:
        print("단어를 포함하는 문서가 존재하지 않습니다.")
        return
    print("\n<추천문서>")
    for i in range(5):
        if(list[i][1]==0):
             break
        print(f"{i+1}:",titles[list[i][0]])
    print('\n')
