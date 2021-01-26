# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Handsome_Author   : Rui
# @Time     : 2020/5/22 16:11


import re
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


def get_wy_teach():
    url = 'https://tech.163.com/special/00097UHL/tech_datalist.js?callback=data_callback'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }

    res = requests.get(url=url, headers=headers)
    # print(res.text)
    data = res.text
    data = eval(data.replace('data_callback(','').replace(data[-1],""))


    for x in data:
        if 'tech' in x['docurl']:
            try:
                res2 = requests.get(url=x['docurl'], headers=headers)

            except requests.exceptions.MissingSchema:
                continue
            except:
                res2 = requests.get(url=x['docurl'], headers=headers)

            res2_text = etree.HTML(res2.text)
            # try:
            item = {}
            item['title'] = ''.join(res2_text.xpath("//div[@id='epContentLeft']/h1/text()"))
            date = res2_text.xpath("//div[@class='post_time_source']/text()")
            date = ''.join(date).replace('\r', '').replace('\n', '').replace('\t', '').replace('  ', '').replace('\u3000', '').replace('来源: ', '')
            # print(date)
            date = date.split(' ')
            # print(date,222)
            try:
                item['date'] = ''.join(date[0])
                item['time'] = ''.join(date[1])
            except:
                pass


            item['source'] = ''.join(res2_text.xpath("//a[@id='ne_article_source']/text()"))

            item['url'] = x['docurl']
            item['content'] = ''.join(res2_text.xpath("//div[@id='endText']/p/text()")).replace('\r',
                                                                                                   '').replace(
                '\n',
                '').replace(
                '\t', '').replace('\u3000', '').replace('  ', '').replace('\xa0 ', '')


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


if __name__ == '__main__':
    get_wy_teach()