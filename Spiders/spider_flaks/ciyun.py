# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Handsome_Author   : Rui
# @Time     : 2020/5/21 17:50
import os
import time

import numpy as np
from flask import Flask,render_template,request

from spider_flaks import wc_tm
from spider_flaks.best_ten import get_ten

from tk_spider import main

app = Flask(__name__)

from flask_cors import CORS

CORS(app, resources=r'/*')



#启动爬虫页
@app.route('/test', methods=['GET'])
def mytest():
    main.multi_thread()
    time.sleep(10)
    return '爬取完成~'




#首页
@app.route('/')
def index2():
    return render_template('index3.html') # send_file('index.html')

#生成词云
@app.route('/aa')
def index():
    wc_tm.run()

    return render_template('index2.html')

@app.route('/news')
def news_list():
    data = get_ten()
    print(33333,data)
    data = np.array(list(set([tuple(t) for t in data])))
    return render_template('index4.html', data=data)



if __name__ == '__main__':
    app.run(debug=True,port=5000)

