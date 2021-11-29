# 抓取PTT"電影版"網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
request=req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36" # 直接複製user-angent過來。若沒有user-angent抓不到資料(可示範)
})
# 拜訪網站
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)
print('------------------------------------')

# 解析HTML格式文件，取得每個文章標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser") # parser是解析的意思
print(root.title)
print(root.title.string)
print('------------------------------------')
print(root.find("div", class_="title"))
print('------------------------------------')
print(root.find("div", class_="title").a.string)
titles=root.find_all("div", class_="title") # 根據class='title'的特徵尋找所有<div>標籤，以列表存在titles裡
print('------------------------------------')
print(titles)
print('------------------------------------')
for title in titles:
    if title.a !=None:
         print(title.a.string) 