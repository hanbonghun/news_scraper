from bs4 import BeautifulSoup
from konlpy.tag import Okt
import requests
import MeCab
import json
import os
import re
mecab_tagger = MeCab.Tagger()
okt = Okt()

def get_page_num(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    result = soup.find("span", {"id": "resultCntArea"}).text
    result= result.split('/')[1]
    result = result.replace(',','')
    article_num = int(re.findall(r'\d+', result)[0])

    if article_num>800:
        max_page = 80
    else :
        max_page = pages/10

    print(f"{max_page} 페이지, 약 {article_num}건의 기사가 검색되었습니다.")
    while True:
        get_page = int(input("몇 페이지까지 기사를 가져올까요?"))
        if get_page>max_page:
            print("최대 페이지를 초과하였습니다.")
            continue
        else :
            return get_page

# 페이지에 있는 뉴스들의 링크를 저장하여 반환
def get_news_daum(URL,NUM_PAGES):
    links= []   # 각 페이지에 있는 뉴스 각각의 링크
    for i in range(NUM_PAGES):
        url=f"{URL}&DA=PGD&p={i+1}"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        results = soup.find_all("div",{"class":"cont_inner"})
        for result in results:
            links.append(result.find('a')['href'])
    return links

# 뉴스 각각의 제목과 내용을 파일에 쓰고 각 파일의 내용을 반환
def get_news_contents_seoulgyeongje(f,url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    [s.extract() for s in soup('script')]           #script 태그 제거
    for div in soup.find_all("figure", {'class':'art_photo'}):  #figure 태그 제거
        div.decompose()
    for div in soup.find_all("div",{'class':'article_copy'}):
        div.decompose()
    title = soup.find("div",{"class":"art_tit"}).text.strip()
    title = title.replace("“",'"')
    title = title.replace("”",'"')
    content = soup.find("div",{"class":"article_view"}).text.strip()
    f.write(title)
    f.write('\n')
    f.write(content)
    entire_info = title+" "+content
    return entire_info

# get_news_contents_seoulgyeongje() 함수를 바탕으로 제목과 내용이 담긴 파일을 만들고, 리스트에 파일 내용을 저장
def create_news_files(links,list):
    print("기사를 가져오고 있습니다...\n")
    text_index = 0
    for i in range(len(links)):
        path = os.path.join('news',f'{text_index+1}.txt')
        with open(path,"w",encoding="utf-8") as f:
            try:
                list.append(get_news_contents_seoulgyeongje(f,links[i]))
                text_index=text_index+1
            except:
                f.close()
                os.remove(path)
                print(i+1,"번째 파일의 HTML 구조가 달라 불러오지 못했습니다.")
    print(len(links),"개 중",text_index,"개의 기사를 불러왔습니다.\n")
    print(len(list))

# mecab 라이브러리를 활용한 각 뉴스 기사 형태소 분석
def split_morph(sentence):
    return [
        node.split('\t')[0]
        for node in mecab_tagger.parse(sentence).split('\n')
    ][:-2]

# 형태소 분석 결과를 news_morph 파일에 작성
def create_morph_files(contents):
    print("형태소 분석 시작...\n")
    for i in range(len(contents)):
        path = os.path.join('news_morphs',f'{i+1}_morph.txt')
        with open(path,"w",encoding="utf-8") as f:
            words = split_morph(contents[i])
            for word in words:
                f.write(word+" ")
    print("형태소 분석이 완료되었습니다.\n")

# 기사 제목과 내용이 담긴 파일을 명사를 기준으로 분석하고 그 결과를 news_nouns폴더 안의 파일에 작성
def get_noun_files(count):
    print("명사 분석 시작...\n")
    for i in range(count):
        path = os.path.join('news',f'{i+1}.txt')
        with open(path,"r",encoding="utf-8") as f:
            text = f.read()
        text = re.sub('\?|\.|\!|\/|\;|\:|\"|\'|\‘|\’|“|\”', '', text)

        nouns = okt.nouns(text)
        dic = dict()
        for noun in nouns:
            dic[noun]= dic.get(noun,0)+1

        dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1],reverse=True)}
        path = os.path.join('news_nouns',f'{i+1}_noun.json')
        obj = json.dumps(dic,ensure_ascii=False,indent=4)
        with open(path,'w',encoding="utf8") as f:
            f.write(obj)

    print("명사 분석이 완료되었습니다.\n")

#list의 순서를 변경하지 않고 중복 제거
def OrderedSet(list):
    my_set = set()
    res = []
    for e in list:
        if e not in my_set:
            res.append(e)
            my_set.add(e)
    return res

#형태소 분석한 파일의 내용을 합친 후 dictionary를 통해 사전을 만들고 json파일로 저장
def create_dic(count):
    print("사전 파일 만들기 시작...\n")
    all_words = []
    for i in range(count):
        path = os.path.join('news_morphs',f'{i+1}_morph.txt')
        with open(path,"r",encoding="utf8") as f:
            temp = f.read()
            temp = temp.split()
            res = OrderedSet(temp)
            res.sort()
            all_words= all_words + res

    all_words.sort()
    all_words= OrderedSet(all_words)
    dic = dict()

    for i in range(len(all_words)):
        dic[i+1]= all_words[i]

    obj = json.dumps(dic,ensure_ascii=False,indent=4)
    with open('dictionary.json','w',encoding="utf8") as f:
        f.write(obj)

    print("사전 파일이 만들어졌습니다.\n")
