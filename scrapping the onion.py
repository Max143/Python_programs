import requests
from bs4 import BeautifulSoup

def scrape():
   session = requests.session()

   url = "https://www.theonion.com/"

   content = session.get(url, verify=False).content

   # Bs4 Object
   soup = BeautifulSoup(content,'lxml')

   columns =  soup.find_all('div', {'class':'curation-module__zone'})

   print(len(columns))

    #for col in columns:
     # print(col)

   # posts
   posts = soup.find_all('div', {'class':'curation-module__item'})

   for post in posts:
      link = post.find_all('a', {'class':'js_curation-click'})[1]
      image_source = post.find('img', {'class':'featured-image'})
      print(link.text)
      print(image_source)
scrape()
