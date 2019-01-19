import requests
from bs4 import BeautifulSoup

url = 'https://www.dataquest.io/blog/tag/python/'

site = requests.get(url)

soup = BeautifulSoup(site.content, 'html.parser')



count = 0

print("Title: ", soup.title.string)

post_feed  = soup.find('div', class_='post-feed')

posts = post_feed.find_all('article', "post-card")
for post in posts:
    title = post.find('h2', class_='post-card-title')
    print("Blog Title: ", title.string)
    date = post.find('span', class_='post-card-date')
    print("Published Date: ",date.string)
    tags = post.find('span', class_='post-card-tags')
    print("Tags: ",tags.string)
    count += 1
    print("--------------------------------------------------------------------------------------")

print("Total Blogs: ", count)
''''
Testing as a single object -
# I can scrape single data easily 
single_post = posts[0]

title = single_post.find('h2', class_='post-card-title')
print(title.string)

date = single_post.find('span', class_='post-card-date')
print(date.string)

tags = single_post.find('span', class_='post-card-tags')
print(tags.string)

'''


    






 




