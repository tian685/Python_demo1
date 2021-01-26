# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Handsome_Author   : Rui
# @Time     : 2020/5/21 14:30

import requests
from lxml import etree

from pymysql import connect

conn = connect(host='localhost', port=3306, database='world', user='root', password='你自己的密码', charset='utf8')
# 获取cursor对象
cs1 = conn.cursor()
#存mysql函数
def save_sql(sqli,values):
    cs1.execute(sqli, values)
    conn.commit()


def get_s_mil():
    headers = {
        'user-agent ': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
    }

    url = 'https://mil.news.sina.com.cn/'

    try:
        res = requests.get(url=url, headers=headers)
    except:
        res = requests.get(url=url, headers=headers)

    res_text = etree.HTML(res.text)

    url_list = res_text.xpath("//div[@class='fs_right']//a/@href")
    print(url_list)
    print('一共', len(url_list))
    for x in url_list:

        try:
            res2 = requests.get(url=x, headers=headers)
        except:
            res2 = requests.get(url=x, headers=headers)
        # print(res2.encoding)
        try:
            data = res2.text
            data = data.encode('ISO-8859-1')
            data = data.decode('utf-8')
        except:
            continue
        res2_text = etree.HTML(data)

        item = {}
        item['title'] = ''.join(res2_text.xpath("//h1[@class='main-title']/text()"))
        date = res2_text.xpath("//span[@class='date']/text()")
        # print(date)
        item['date'] = ''.join(date[0].split(" ")[0])
        item['time'] = ''.join(date[0].split(" ")[1])
        item['source'] = ''.join(res2_text.xpath("//div[@class='date-source']/a/text()"))
        if item['source'] == '':
            item['source'] = ''.join(res2_text.xpath("//div[@class='date-source']/span[@class='source']/text()"))
        item['url'] = x
        item['content'] = ''.join(res2_text.xpath("//div[@class='article']/p/text()")).replace('\r', '').replace('\n',
                                                                                                                 '').replace(
            '\t', '').replace('\u3000', '').replace('  ', '')

        print(item)
        sqli = '''insert into sina(标题,日期,时间,来源,链接,内容)
                                            values(%s,%s,%s,%s,%s,%s)
                                            '''
        values = (item['title'], item['date'], item['time'], item['source'], item['url'], item['content'])
        try:
            save_sql(sqli, values)
            print('导入数据库成功')
        except:
            cs1.rollback()  # 如果发生错误则回滚
            print('失败')
    print('军事爬取完成~')

if __name__ == '__main__':
    get_s_mil()
