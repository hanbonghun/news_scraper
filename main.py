import os
from main_function import *
list = os.listdir("C:\\Users\\hanbonghun\\Desktop\\newsscrapping\\news")
NUM_OF_ARTICLES = len(list)    # 전체 기사 수
articles_per_page =20 # 페이지 당 출력할 기사 수
titles, contents = get_titles_and_contents(NUM_OF_ARTICLES)
print(len(contents))
similarities = get_similarity(contents)

print_articles_list(articles_per_page,1,titles)

while True :
    option = input("페이지 이동[0], 문서 조회[1], 단어 검색[2], 종료[3] --> ")
    if option =="0":
        page = int(input("이동할 페이지 입력 : "))
        print_articles_list(articles_per_page,page,titles)

    elif option =="1":
        article_title = input("조회할 기사의 제목을 입력하세요 :").strip()
        print(article_title)
        if article_title in titles:
            index = titles.index(article_title)
            print('\n<<',titles[index],'>>\n')
            print(contents[index])
            print_similar_doc(similarities,index,titles)
            get_top_rank_words(index)
        else:
            print("기사가 존재하지 않습니다.\n")

    elif option =="2":
        word = input("검색하실 단어를 입력하세요 : ")
        get_article_by_word(word,titles)

    elif option =="3":
        print("프로그램을 종료합니다.")
        break
