# -*- coding: UTF-8 -*-
"""
@File    ：微博热搜榜.py
@Author  ：叶庭云
@Date    ：2020/9/18 15:01
"""
import schedule
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
count = 0


def get_content():
    global count
    print('----------- 正在爬取数据 -------------')
    url = 'https://s.weibo.com/top/summary?cate=realtimehot&sudaref=s.weibo.com&display=0&retcode=6102'
    df = pd.read_html(url)[0][1:11][['序号', '关键词']]   # 获取热搜前10
    time_ = datetime.now().strftime("%Y/%m/%d %H:%M")     # 获取当前时间
    df['序号'] = df['序号'].apply(int)
    df['热度'] = df['关键词'].str.split('  ', expand=True)[1]
    df['关键词'] = df['关键词'].str.split('  ', expand=True)[0]
    df['时间'] = [time_] * len(df['序号'])
    if count == 0:
        df.to_csv('datas.csv', mode='a+', index=False)
        count += 1
    else:
        df.to_csv('datas.csv', mode='a+', index=False, header=False)


# 定时爬虫
schedule.every(1).minutes.do(get_content)

while True:
    schedule.run_pending()
