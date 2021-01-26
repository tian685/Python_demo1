# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Handsome_Author   : Rui
# @Time     : 2020/5/21 15:10
import re
import time

from lxml import etree

import requests
import json

from pymysql import connect

conn = connect(host='localhost', port=3306, database='world', user='root', password='你自己的密码', charset='utf8')
# 获取cursor对象
cs1 = conn.cursor()
#存mysql函数
def save_sql(sqli,values):
    cs1.execute(sqli, values)
    conn.commit()

sqls = "create table sina(id int(11) not null auto_increment primary key,标题 varchar(50) not null,日期 varchar(20) not null,时间 varchar(20) not null,来源 varchar(50) not null,链接 varchar(200) not null,内容 varchar(5000) not null);"
def create_sql(sqls):
    cs1.execute(sqls)
    conn.commit()





def get_tea():
    t = int(time.time())
    url = 'https://cre.mix.sina.com.cn/api/v3/get?callback=jQuery111208551231182504202_1590045085038&cateid=1z&cre=tianyi&mod=pctech&merge=3&statics=1&length=15&up=0&down=0&tm=1590045085&action=0&top_id=J9KT3%2CJNHbr%2CJMtAN%2CJMwQ9%2CJJWay%2CJMoUn%2CJMuWY%2C%2CJMetA%2C%2C%2C&offset=0&ad=%7B%22rotate_count%22%3A100%2C%22platform%22%3A%22pc%22%2C%22channel%22%3A%22tianyi_pctech%22%2C%22page_url%22%3A%22https%3A%2F%2Ftech.sina.com.cn%2F%22%2C%22timestamp%22%3A1590045085374%7D&_={}'.format(t)
    headers = {
        'user-agent ': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
    }

    try:
        res = requests.get(url=url, headers=headers)
    except:
        res = requests.get(url=url, headers=headers)
    # print(res.text)
    # res_text = etree.HTML(res.text)
    data = res.text

    data = re.findall(r'.*novels":\[],(.*?),"req_time":', data)

    data = '{' + ''.join(data) + '}'
    print(data)

    data = json.loads(data)

    for x in data['data']:
        # print(x['url'])

        try:
            res2 = requests.get(url=x['url'], headers=headers)

        except requests.exceptions.MissingSchema:
            continue
        except:
            res2 = requests.get(url=x['url'], headers=headers)
        # print(res2.encoding)
        try:
            data = res2.text
            data = data.encode('ISO-8859-1')
            data = data.decode('utf-8')
        except:
            continue
        res2_text = etree.HTML(data)
        # try:
        item = {}
        item['title'] = ''.join(res2_text.xpath("//h1[@class='main-title']/text()"))
        if item['title'] == '':
            item['title'] = ''.join(res2_text.xpath("//h1[@id='artibodyTitle']/text()"))
        date = res2_text.xpath("//span[@class='date']/text()")
        # print(date)
        try:
            item['date'] = ''.join(date[0].split(" ")[0])
            item['time'] = ''.join(date[0].split(" ")[1])
        except:
            pass
        if date == []:
            date = res2_text.xpath("//span[@id='pub_date']/text()")

            date = ''.join(date).replace('\r','').replace('\n','').replace('\t', '').replace('  ', '')
            # print(date.replace('\r','').replace('\n','').replace('\t', '').replace('  ', ''))
            date = date.split(' ')
            # print(date,222)
            item['date'] = date[1]
            item['time'] = date[2]

        item['source'] = ''.join(res2_text.xpath("//div[@class='date-source']//a/text()"))
        if item['source'] == '':
            item['source'] = ''.join(
                res2_text.xpath("//div[@class='date-source']/span[@class='source']/text()"))
        item['url'] = x['url']
        item['content'] = ''.join(res2_text.xpath("//div[@class='article']/p/text()")).replace('\r',
                                                                                               '').replace(
            '\n',
            '').replace(
            '\t', '').replace('\u3000', '').replace('  ', '').replace('\xa0 ', '')
        if item['content'] == '':
            item['content'] = ''.join(res2_text.xpath("//div[@id='artibody']//text()")).replace('\r','').replace('\n','').replace(
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
        # except:
        #     continue

    print('科技爬取完成~')

if __name__ == '__main__':
    # create_sql(sqls)
    get_tea()
    # cs1.close()