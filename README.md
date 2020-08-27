# Document Recommendation Program Using Similarity Test

## About the project
By scraping news articles related to keywords in the following news, documents that are similar to the words that appear the most in news articles are reported, and all words appearing in the articles are created as json files.

## usage
When main.py is executed, it automatically scraps the indeed and stackoverflow Python-related jobs.
![cmd화면](https://user-images.githubusercontent.com/33712528/91433426-39c65f00-e89e-11ea-8cc1-7c3ac2610091.PNG)

Information related to the imported job is divided into title, company, region, and link items, and is saved as a csv file.
![excel](https://user-images.githubusercontent.com/33712528/91433429-3af78c00-e89e-11ea-8ba6-acb17e6ffb54.PNG)

## Precautions

Retrieving specific elements of url and html in the code depends on which site and which keyword you enter. Therefore, it must be modified for each page and used.
