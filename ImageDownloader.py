from bs4 import BeautifulSoup
import requests

name = input("Enter name of image needed: ")
base_url = 'https://unsplash.com/s/photos/'
search_url = base_url + name

# tag and class name in the web page
tag = 'img'
class_name = '_2zEKz'

r = requests.get( search_url )

soup = BeautifulSoup(r.content, 'html.parser')

# Differentiate images with different numbers
i = 0

for img in soup.find_all(tag, class_ = class_name):
    response = requests.get(img['srcset'])
    i = i + 1

    file = open("images/" + name + str(i) + ".png", "wb")
    file.write(response.content)
    file.close()