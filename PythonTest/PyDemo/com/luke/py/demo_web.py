import requests
from bs4 import BeautifulSoup

url = "https://www.baidu.com"

page = requests.get(url)
# 检查http响应状态
print(page.status_code)

print(page.content)
soup = BeautifulSoup(page.content, 'lxml')

print(soup.prettify())

ta = soup.find('div', id='u1')
# print(ta)
for link in ta.find_all('a'):
    print(link.get_text())

