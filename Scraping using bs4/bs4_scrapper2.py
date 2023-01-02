from bs4 import BeautifulSoup
import requests
root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text 
soup = BeautifulSoup(content,'lxml')
# print(soup.prettify())
box = soup.find('article', class_ = 'main-article')
links = []
for link in box.find_all('a',href=True):
    links.append(link['href'])
print(links)

for link in links:
    website = f'{root}/{link}'
    result = requests.get(website)
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

    with open(f'E:\[ FreeCourseWeb.com ] Udemy - Web Scraping Course in Python - BS4, Selenium and Scrapy\~Get Your Files Here !\Python-Bots-and-Web-Scrapping-Projects\Scraping using bs4/scraped_txt/{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)