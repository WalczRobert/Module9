import requests
import bs4 as bs
import urllib.request

url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=202003&Campus=1'
response = requests.get(url)
html = response.content
f = open("requestResult.txt","w+")
f.writelines(str(html))
f.close()

soup =bs.BeautifulSoup(open("requestResult.txt"), "html.parser")
print(soup.prettify())