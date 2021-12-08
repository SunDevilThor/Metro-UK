# Metro - UK 
# Tutorial from John Watson Rooney YouTube channel

from requests_html import HTMLSession
import pprint

url = 'http://metro.co.uk/news/tech/'

s = HTMLSession()
r = s.get(url)

posts = r.html.find('ul.metro-mosaic', first=True).find('h3')
data = [(post.text, post.find('a', first=True).attrs['href']) for post in posts]

pprint.pprint(data)