# -×- coding:utf-8 -*-


import pymongo


def judge(actions):
    util_num = len(actions)
    add_buy_count = 0
    add_count = 0
    buy_count = 0
    item_dict = {}
    for act in actions:
        if act[1] in item_dict:
            item_dict[act[1]].append(act[2])
        else:
            item_dict[act[1]] = [act[2]]
    for items_tuils in item_dict.values():
        if 4 in items_tuils:
            print items_tuils

    print util_num, '-------------------------------'


def buy_time_statics(coll):
    mong_cur = coll.find({})
    mong_num = mong_cur.count()

    buy_date = {}
    for index in xrange(mong_num):
        actions_set = mong_cur.next()
        actions = actions_set.values()[0] if isinstance(actions_set.values()[0], list) else actions_set.values()[1]
        for util in actions:
            if util[2] == 4:
                pur_date = str(util[6]) + '-' + str(util[8])
                if pur_date in buy_date:
                    buy_date[pur_date] += 1
                else:
                    buy_date[pur_date] = 1

    for date_day, counter in buy_date.items():
        print date_day, counter


if __name__ == '__main__':
    mong_conn = pymongo.MongoClient(host='localhost', port=27017)
    db = mong_conn['ali_rec']
    coll = db['user_acts']
    mong_cur = coll.find({})
    acts_num = mong_cur.count()

    # 查看产生每个用户对于购买的产品所经历的util
    # for index in xrange(acts_num):
    #     actions_set = mong_cur.next()
    #     actions = actions_set.values()[0] if isinstance(actions_set.values()[0], list) else actions_set.values()[1]
    #     judge(actions)


    #
    buy_time_statics(coll)


