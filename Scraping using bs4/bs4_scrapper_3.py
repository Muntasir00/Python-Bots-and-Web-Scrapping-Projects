from bs4 import BeautifulSoup
import requests
root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
content = result.text 
soup = BeautifulSoup(content,'lxml')
# print(soup.prettify())

#pagination
pagination = soup.find('ul',class_ = 'pagination')
pages = pagination.find_all('li', class_ = 'page-item')
last_page = pages[-2].text
links = []
for page in range(1,int(last_page)+1)[:2]:
    #https://subslikescript.com/movies_letter-A?page=2
    result = requests.get(f'{website}?page={page}')
    content = result.text 
    soup = BeautifulSoup(content,'lxml')


    box = soup.find('article', class_ = 'main-article')
    
    for link in box.find_all('a',href=True):
        links.append(link['href'])
    print(links)

    for link in links:
        try:
            result = requests.get(f'{root}/{link}')
            content = result.text 
            soup = BeautifulSoup(content,'lxml')
            # print(soup.prettify())
            box = soup.find('article', class_ = 'main-article')
            title = box.find('h1').get_text()
            transcript = box.find('div', class_ = 'full-script').get_text(strip=True, separator=" ")
            # print(title,"/n")
            # print(transcript)
            # with open(f'{title}.txt', 'w') as file:
            #     file.write(transcript)

            with open(f'E:\[ FreeCourseWeb.com ] Udemy - Web Scraping Course in Python - BS4, Selenium and Scrapy\~Get Your Files Here !\Python-Bots-and-Web-Scrapping-Projects\Scraping using bs4/scraped_text_pagination/{title}.txt', 'w', encoding='utf-8') as file:
                file.write(transcript)
        except:
            print("--------------Link not working-----------")
            print(link )