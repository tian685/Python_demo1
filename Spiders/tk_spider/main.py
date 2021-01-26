# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Handsome_Author   : Rui
# @Time     : 2020/5/18 17:16

import datetime
import threading

from Spiders.tk_spider import sina_yule, sina_PE, sina_teach, sina_mmil, sina_money, sina_international, wy_teach, wy_guonei, \
    sina_guonei, wy_international, wy_mil, wy_money, wy_PE, wy_yule


def hua():
    sina_yule.get_s_yule()

def hy():
    sina_international.get_s_inter()

def pzn():
    sina_teach.get_tea()

def ts():
    sina_PE.get_s_sport()

def xz():
    sina_mmil.get_s_mil()

def xzg():
    print(2222)
    sina_money.get_s_money()

def chn():
    sina_guonei.get_s_guonei()

def wy_hua():
    wy_guonei.get_wy_gn()

def wy_hy():
    wy_international.get_wy_inter()

def wy_pzn():
    wy_mil.get_wy_mil()

def wy_ts():
    wy_money.get_wy_money()

def wy_xz():
    wy_PE.get_wy_sport()

def wy_xzg():
    print(333)
    wy_teach.get_wy_teach()

def wy_chn():
    wy_yule.get_wy_yule()



def multi_thread():
    t1 = threading.Thread(target=xzg)
    t2 = threading.Thread(target=xz)
    t3 = threading.Thread(target=ts)
    t4 = threading.Thread(target=pzn)
    t5 = threading.Thread(target=hy)
    t6 = threading.Thread(target=hua)
    t7 = threading.Thread(target=chn)
    t8 = threading.Thread(target=wy_xzg)
    t9 = threading.Thread(target=wy_xz)
    t10 = threading.Thread(target=wy_ts)
    t11 = threading.Thread(target=wy_pzn)
    t12 = threading.Thread(target=wy_hy)
    t13 = threading.Thread(target=wy_hua)
    t14 = threading.Thread(target=wy_chn)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()



if __name__ == '__main__':

    multi_thread()






