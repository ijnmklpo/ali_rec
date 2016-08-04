# -*- coding: utf-8 -*-
# @Date    : 2016/7/14 , 23:28
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version :
# @Description: 将数据从mysql导入到mongodb的模块



import MySQLdb
import pymongo

if __name__ == '__main__':
    mysql_conn = MySQLdb.connect(host='localhost', user='ryh', passwd='123456', port=3306)
    mysql_conn.select_db('ali_rec')
    # MySQLdb.connect(host='localhost', user='ryh', passwd='123456', port=3306, db='ali_rec')
    # 上面这样的话就直接选定数据库了
    mysql_cur = mysql_conn.cursor()


    # 建立mongodb数据库链接并创建游标
    mongodb_conn = pymongo.MongoClient(host='localhost', port=27017)
    db = mongodb_conn['ali_rec']
    user_acts = db['user_acts']
    user_acts.remove({})    # 清空一下集合

    mysql_cur.execute('select * from user_tb;')
    mysql_rest = mysql_cur.fetchall()
    for user_id in mysql_rest:
        mysql_cur.execute('select * from user_act where user_id=\'' + user_id[0] + '\';')
        mysql_user_rest = mysql_cur.fetchall()
        actions = []
        for util in mysql_user_rest:
            action = []
            action.append(int(util[0]))         # 用户id           0
            action.append(int(util[1]))         # 商品id           1
            action.append(int(util[2]))         # 行为标识          2
            action.append(str(util[3]))         # 地理位置编码      3
            action.append(int(util[4]))         # 商品分类id        4
            action.append(int(util[5][0:4]))    # year             5
            action.append(int(util[5][5:7]))    # month            6
            action.append(int(util[5][8:10]))    # day             7
            action.append(int(util[5][11:13]))    # hour           8

            actions.append(action)
        user_acts.insert({user_id[0]: actions})


