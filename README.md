# Document Recommendation Program Using Similarity Test

## About the project
By scraping news articles related to keywords in the following news, documents that are similar to the words that appear the most in news articles are reported, and all words appearing in the articles are created as json files.

## usage
Keyword and the number of pages to be scraped are entered, and the title and content of the article are created in the news folder, and the results of morpheme analysis and noun analysis are created in the morphs and nouns folders, respectively.
![load](https://user-images.githubusercontent.com/33712528/91495623-c51f0f00-e8f5-11ea-9dd0-4a6165aa5520.PNG)


txt file in news folder
![news](https://user-images.githubusercontent.com/33712528/91495624-c51f0f00-e8f5-11ea-95df-f29a520ae3b1.PNG)

txt file in news_morphs
![morph](https://user-images.githubusercontent.com/33712528/91495613-c2bcb500-e8f5-11ea-978d-59bb5fe7d504.PNG)

json file in news_nouns
![nouns](https://user-images.githubusercontent.com/33712528/91495616-c3554b80-e8f5-11ea-9efa-fb8a109336a5.PNG)

dictionary file 
![dic](https://user-images.githubusercontent.com/33712528/91495617-c3ede200-e8f5-11ea-8224-981bfa112fc5.PNG)

Running main.py can perform a number of functions based on the loaded content.
*move page[0], Retrieving documents[1], Search for articles by word[2], exit[3]*
![실행화면 1](https://user-images.githubusercontent.com/33712528/91495618-c3ede200-e8f5-11ea-8575-fd7359408f40.PNG)


If you select option Retrieving documents[1], it recommends articles that contain the title and content of the article and similar content.
![유사기사](https://user-images.githubusercontent.com/33712528/91495619-c4867880-e8f5-11ea-8cfc-25693b934374.PNG)

If you select Search for articles by word[2], after entering a word, the article with the highest frequency of the word is recommended.
![추천기사](https://user-images.githubusercontent.com/33712528/91495621-c4867880-e8f5-11ea-85e9-5c03880ea089.PNG)


## Precautions

1. Retrieving specific elements of url and html in the code depends on which site and which keyword you enter. Therefore, it must be modified for each page and used.

2. Before main.py is executed, articles must be fetched through get_news.py execution.





