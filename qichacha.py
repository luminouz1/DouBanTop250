import stat

import requests
from bs4 import BeautifulSoup
import re
import time
import sys
import pymysql


def getHTMLText(url, key, p):
    try:
        if (p == 0):
            kw = {}
        else:
            kw = {'key': key, 'p': p}
        r = requests.get(url, params=kw, headers={'User-Agent': 'Mozilla/4.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Failed!")


def getData(html):
    soup = BeautifulSoup(html, "html.parser")
    tableList = soup.find('table', attrs={'class': 'm_srchList'})  # 找到第一个class属性值为m_srchList的table标签
    tbodyList = tableList.find('tbody')
    companyInfo = []
    for infoTr in tbodyList.find_all('tr'):  # 找到所有tr标签
        data = []
        infoTd = infoTr.find('td')[1]

        # 得到公司名字
        companyName = infoTd.find('a', attrs={'class': 'ma_h1'}).getText()  # 找到第一个class属性值为ma_h1的a标签
        data.append(companyName)

        infoP1 = infoTd.find('p', attrs={'class', 'm-t-xs'})[0]
        # 得到法定代表人
        legalRepresentative = infoP1.find('a', attrs={'class', 'text-primary'}).getText()
        data.append(legalRepresentative)
        # 注册资本
        registeredCapital = infoP1.find('span', attrs={'class', 'm-l'})[0].getText()
        data.append(registeredCapital)
        # 成立时间
        regtime = infoP1.find('span', attrs={'class', 'm-l'})[1].getText()
        data.append(regtime)

        infoP2 = infoTd.find('p', attrs={'class', 'm-t-xs'})[1]
        # 电话
        telephone = infoP2.getText()
        data.append(telephone)
        # 邮箱
        email = infoP2.find('span').getText()
        data.append(email)

        infoP3 = infoTd.find('p', attrs={'class', 'm-t-xs'})[2]
        # 地址
        address = infoP3.getText().replace('<em>', '').replace('<//em>', '')
        data.append(address)

        print(outputMode.format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], chr(12288)))


# 将输出重定向到txt文件
output = sys.stdout
outputfile = open("companys.txt", 'w', encoding='utf-8')
sys.stdout = outputfile

outputMode = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}"
print(outputMode.format('公司名称', '法定代表人', '注册资本', '成立时间', '电话', '邮箱', '地址', chr(12288)))
basicUrl = 'http://www.qichacha.com/search'
p = 1
while p <= 10:
    key = '南京浦口区#index:10'
    html = getHTMLText(basicUrl, key, p)
    time.sleep(2)
    p += 1
    getData(html)

outputfile.close()
sys.stdout = output
