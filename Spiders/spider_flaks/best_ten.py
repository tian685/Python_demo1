# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Handsome_Author   : Rui
# @Time     : 2020/5/22 14:02
import random
import pandas as pd


def get_ten():
    df = pd.read_excel('./今日新闻.xlsx')

    df = pd.DataFrame(df, columns=['标题','链接'])

    the_sum = []

    for x in range(1,51):
        y = random.randint(2,100)
        # print(df.loc[x:x].values,3333)
        # print(y)
        print(df.loc[y:y].values)
        z = df.loc[y:y].values
        # print(5555,z)
        if z != []:
            the_sum.append(z)
        else:
            continue
    print(5555,the_sum)

    one = []
    for y in the_sum:
        # print(y[0])
        one.append(y[0])

    print(one[0])
    return one

if __name__ == '__main__':
    get_ten()