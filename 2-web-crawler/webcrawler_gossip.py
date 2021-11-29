import urllib.request as req
url="https://www.ptt.cc/bbs/Gossiping/index.html"
request=req.Request(url, headers={
    'cookie':'over18=1',
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36" 
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="title")
for title in titles:
    if title.a !=None:
         print(title.a.string)
print('------------------------------------')

# 抓取上一頁網址(超連結)
nextLink=root.find("a", string="‹ 上頁") # 找到所有特徵為 string = "<上頁"的所有<a>標籤
print(nextLink)
print('--------------')
print(nextLink['href'])
print('------------------------------------')

# 抓取一頁面標題，與上一頁連結
def get_data(url):
    request=req.Request(url, headers={
        'cookie':'over18=1',
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36" # 若沒有user-angent抓不到資料(可示範)
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    for title in titles:
        if title.a !=None:
            print(title.a.string)
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink['href']

pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
pageURL = 'http://www.ptt.cc'+get_data(pageURL)
print(pageURL)
print('------------------------------------')

# 連續抓取多個頁面標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count <3:                                      # 會抓到三頁(想抓幾頁可自己設定)
    pageURL = 'http://www.ptt.cc'+get_data(pageURL)
    count +=1