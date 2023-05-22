import requests
from bs4 import BeautifulSoup
import pymysql

def crawl_ithome_news():
    url = "https://www.ithome.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("请求发生错误:", e)
        return []
    soup = BeautifulSoup(response.content, "html.parser")


    news_list = []
    ul_elements = soup.select("#nnews > div.t-b.sel.clearfix > ul")

    for ul in ul_elements:
        news_items = ul.select("li > a")

        for item in news_items:
            title = item.text.strip()
            link = item["href"]
            news_list.append({"title": title, "link": link})

    return news_list

def save_news_to_database(news):
    # 修改以下数据库连接信息为您的实际配置
    host = "localhost"
    user = "root"
    password = "123456"
    database = "chatgpt"
    
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()

    for item in news:
        title = item["title"]
        link = item["link"]
        sql = "INSERT INTO it_news (title, link) VALUES (%s, %s)"
        cursor.execute(sql, (title, link))

    conn.commit()
    cursor.close()
    conn.close()

news = crawl_ithome_news()
if len(news) == 0:
    print("未获取到新闻数据")
else:
    save_news_to_database(news)
