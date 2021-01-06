# -*- coding: UTF-8 -*-

import MySQLdb
import time

import json

host_value = "10.142.51.128"
user_value = "vip_incubator_x"
pass_value = "k1Kmg2gXeszwSs1NtRoIg3DeyqPjTXkY"
port_value = 6028

# create triggers for mipub_gossip

def getAppealHandlerResult():
    output = open('/home/work/sinbad/workspace/temp/vip_create_group_appeal.txt', 'w')

    db = MySQLdb.connect(user=user_value, host=host_value, passwd=pass_value, port=port_value, db="vip", charset='utf8')

    cursorSign = db.cursor()

    cursorSignDetail = db.cursor()

    # 分表采用取余数的方式#
    statementSign = """SELECT sign_id, status FROM app_sign_idx_plan_9 WHERE  plan_id = 10209 """

    statementDetailPre = """SELECT sign_id, status FROM app_sign_idx_plan_ """
    statementDetailSuf =""" WHERE  plan_id = 10209 """


    cursorSign.execute(statementSign)

    resSignResult = cursor.fetchall()
    for rowInSign in resSignResult:
        tableIndex =
        index = 0
        for signValue in rowInSign:
            tableIndex =
            temp = val
            print temp
            if index = 0:
                tableIndex = val % 100;
                cursorSignDetail.execute(statementDetailPre + tableIndex + statementDetailSuf)
                signDetail = cursorSignDetail.fetchone()

            if index > 2:
                time_local = time.localtime(temp/1000)
                temp = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
            index = index + 1
            output.write(str(temp))
        output.write("\n")
    cursor.close()
    db.close()
    output.close()
    print("Finish")
    return

getAppealHandlerResult();