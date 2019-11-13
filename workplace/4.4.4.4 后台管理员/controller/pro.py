from flask import Blueprint, request
import pymysql
import json
import time

Pro = Blueprint('pro', __name__, url_prefix='/pro')

conn = pymysql.connect(host='123.207.27.133', user="admin", passwd="iot123456", db="shop", port=3306, charset="utf8")
cur = conn.cursor()

@Pro.route('search_pro',methods=['POST'])
def search_pro():
    json_param = request.get_json()
    sql = "select {} from pro".format(json_param['pName'])
    cur.execute(sql)
    class_list = cur.fetchall()
    print(class_list)
    t ={
        'success': True,
        'message': '',
        'data': class_list
    }
    return json.dumps(t)


@Pro.route('/add_pro',methods=['POST'])
def add_pro():
    json_param = request.get_json()
    sql = "insert into pro (pName,cId,pSn,pNum,mPrice,iPrice,pDesc, pubTime) values ({}, {}, {}, {}, {}, {}, {}, {})".format(
        json_param['pName'],
        json_param['cId'],
        json_param['pSn'],
        json_param['pNum'],
        json_param['mPrice'],
        json_param['iPrice'],
        json_param['pDesc'],
        int(time.time())
    )
    cur.execute(sql)
    conn.commit()
    t ={
        'success': True,
        'message': '',
        'data': {}
    }
    return json.dumps(t)

@Pro.route('delete_pro',methods=['POST'])
def delete_pro():
    json_param = request.get_json()
    sql = "delete from pro where pName={}".format(json_param['pName'])
    cur.execute(sql)
    conn.commit()
    t ={
        'success': True,
        'message': '',
        'data': {}
    }
    return json.dumps(t)
###################################################################################3
@Pro.route('update_pro',methods=['POST'])
def update_pro():
    json_param = request.get_json()
    sql = "update pro " \
          "set pName = {},cId = {},pSn = {},pNum = {},mPrice = {},iPrice = {},pDesc = {}, pubTime= {}" \
          "where pName = {}".formate(
          json_param['pName'],
          json_param['cId'],
          json_param['pSn'],
          json_param['pNum'],
          json_param['mPrice'],
          json_param['iPrice'],
          json_param['pDesc'],
          json_param['PName']
    )
    cur.execute(sql)
    conn.commit()
    t ={
        'success': True,
        'message': '',
        'data': {}
    }
    return json.dumps(t)

@Pro.route('pro_list',methods=['GET'])
def pro_list():
    sql = "selete * from pro"
    cur.execute(sql)
    pro_list = cur.fetchall()
    t ={
        'success': True,
        'message': '',
        'data': pro_list
    }
    return json.dumps(t)
