# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Handsome_Author   : Rui
# @Time     : 2020/4/8 11:32

import numpy as np
import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread
from openpyxl import Workbook  # 导入这个模块用来写入excel
import warnings

import pymysql


def run():

    # 连接数据库
    conn = pymysql.connect(host="localhost", user="root", passwd="200810",
                           db="world", port=3306, charset="utf8")

    cursor = conn.cursor()
    sql='select * from sina'
    cursor.execute(sql)
    row = cursor.fetchone()  # 获取一条数据

    # all=cursor.fetchall()#获取所有数据
    # print(all)
    # for each in all:
    #     print(each) #看看全部数据是否读取下了
    num = 0
    all = []

    while row is not None:

        row = cursor.fetchone()
        print(row)
        num += 1

        all.append(row)
        if num > 350:
            break
        else:
            pass

    print(tuple(all))
    cursor.close()
    conn.close()

    all = tuple(all)
    wb=Workbook()#建立一个工作簿
    sheet=wb.active#激活一张表
    sheet.title='第四题'  #给个标题
    sheet.append(['id','标题','日期','时间','来源','链接','内容'])#写入多少列数据，给个相应得标题，
    for j in all:
        print(444,j)
        print(3333,type(j))
        try:
            sheet.append(tuple(j))#循环写入
        except:
            pass
    wb.save('./今日新闻1.xlsx')#最后储存
    #
    #
    warnings.filterwarnings("ignore")

    # 读取数据
    # df = pd.read_excel(r"C:\Users\Administrator\Desktop\鸿星尔克好评.xlsx")

    df = pd.read_excel("./今日新闻.xlsx")
    df.head()
    # 利用jieba进行分析操作
    df["标题"] = df["标题"].apply(jieba.lcut)
    df.head()
    # 去除停用词操作
    with open("./stopwords.txt", "r", encoding="utf-8") as f:
        stop = f.read()  # 返回的是一个字符串

    stop = stop.split()  # 这里得到的是一个列表.split()会将空格，\n，\t进行切分，因此我们可以将这些加到停用词当中
    stop = stop + [" ", "\n", "\t"]
    df_after = df["标题"].apply(lambda x: [i for i in x if i not in stop])

    print(df_after.head())
    # 词频统计
    all_words = []
    for i in df_after:
        print(222,i)
        all_words.extend(i)

    word_count = pd.Series(all_words).value_counts()
    print(333,word_count)
    # with open('词频.txt','w') as f:
    #     f.write(str(word_count[:11]))
    word_count[:10]
    # 绘制词云图
    # 1、读取背景图片
    back_picture = imread("./static/images/timg.jpg")
    # 2、设置词云参数
    wc = WordCloud(font_path=r"C:\Windows\Fonts\simhei.ttf",
                   background_color="white",
                   max_words=2000,
                   mask=back_picture,
                   max_font_size=200,
                   random_state=42
                   )
    wc2 = wc.fit_words(word_count)
    # 3、绘制词云图
    plt.figure(figsize=(14, 8))#这是调节词云字体大小
    plt.imshow(wc2)
    plt.axis("off")
    # plt.show()
    wc.to_file("./static/images/ciyun.png")


if __name__ == '__main__':
    run()
