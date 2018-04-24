import stat

import requests
from bs4 import BeautifulSoup
import re
import time
import sys
import pymysql


def getHTMLText(url, k):
    try:
        if (k == 0):
            kw = {}
        else:
            kw = {'start': k, 'filter': ''}
        r = requests.get(url, params=kw, headers={'User-Agent': 'Mozilla/4.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Failed!")


# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "doubantop250", use_unicode=True, charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# 使用预处理语句创建表
# sql = """CREATE TABLE FILMINFO (
#          FILM_NAME  CHAR(20) NOT NULL,
#          GRADE  FLOAT,
#          COMMENT_NUM    INT,
#          SHORT_COMMENT  CHAR(20))"""

def getData(html):
    soup = BeautifulSoup(html, "html.parser")
    movieList = soup.find('ol', attrs={'class': 'grid_view'})  # 找到第一个class属性值为grid_view的ol标签
    moveInfo = []
    for movieLi in movieList.find_all('li'):  # 找到所有li标签
        data = []
        # 得到电影名字
        movieHd = movieLi.find('div', attrs={'class': 'hd'})  # 找到第一个class属性值为hd的div标签
        movieName = movieHd.find('span', attrs={'class': 'title'}).getText()  # 找到第一个class属性值为title的span标签
        # 也可使用.string方法
        data.append(movieName)

        # 得到电影的评分
        movieScore = movieLi.find('span', attrs={'class': 'rating_num'}).getText()
        data.append(movieScore)

        # 得到电影的评价人数
        movieEval = movieLi.find('div', attrs={'class': 'star'})
        movieEvalNum = re.findall(r'\d+', str(movieEval))[-1]
        data.append(movieEvalNum)

        # 得到电影的短评
        movieQuote = movieLi.find('span', attrs={'class': 'inq'})
        if (movieQuote):
            data.append(movieQuote.getText().replace('\'', ''))
        else:
            data.append("无")

        # print(outputMode.format(data[0], data[1], data[2], data[3], chr(12288)))

        # SQL 插入语句
        sql = """INSERT INTO FILMINFO(FILM_NAME,GRADE, COMMENT_NUM, SHORT_COMMENT)
                 VALUES ('%s','%s','%s','%s')""" % (data[0], data[1], data[2], data[3])
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')

        # try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    # except:
    # 如果发生错误则回滚
    # db.rollback()


# 将输出重定向到txt文件
# output = sys.stdout
# outputfile = open("moviedata.txt", 'w', encoding='utf-8')
# sys.stdout = outputfile

# outputMode = "{0:{4}^20}\t{1:^10}\t{2:^10}\t{3:{4}<10}"
# print(outputMode.format('电影名称', '评分', '评论人数', '短评', chr(12288)))
basicUrl = 'https://movie.douban.com/top250'
k = 0
while k <= 225:
    html = getHTMLText(basicUrl, k)
    time.sleep(2)
    k += 25
    getData(html)

# outputfile.close()
# sys.stdout = output

# 关闭数据库连接
db.close()
