import decimal
from flask import Blueprint, request
import pymysql
import json

Class = Blueprint('class', __name__, url_prefix='/class')

conn = pymysql.connect(host='123.207.27.133', user="admin", passwd="iot123456", db="shop", port=3306, charset="utf8")
cur = conn.cursor()


@Class.route('get_class',methods=['GET'])
def get_class():
    sql = "select cName from cate"
    cur.execute(sql)
    class_list = cur.fetchall()
    conn.commit()
    t ={
        'success': True,
        'message': '',
        'data': class_list
    }
    return json.dumps(t)

@Class.route('add_class', methods=['POST'])
def add_class():
    json_param = request.get_json()
    cur.execute("select max(id) from cate")
    id = cur.fetchall()[0][0]
    print(id)
    sql = "insert into cate(id, cName) values ({}, '{}')".format(id+1,json_param['cName'])
    cur.execute(sql)
    conn.commit()
    t = {
        'success': True,
        'message': '',
        'data': {}
    }
    return json.dumps(t)

@Class.route('delete_class', methods=['POST'])
def delete_class():
    json_param = request.get_json()
    sql = "select id from cate " \
          "where cName = '{}'".format(json_param['cName'])
    cur.execute(sql)
    id = cur.fetchall()[0][0]
    sql = "delete from cate " \
          "where cName = '{}'".format(json_param['cName'])
    cur.execute(sql)
    sql = "update cate " \
          "set id = id-1 " \
          "where id > {}".format(id)
    cur.execute(sql)
    sql = "delete from pro " \
          "where cId ={}".format(id)
    cur.execute(sql)
    sql = "update pro " \
          "set cId = cId-1 " \
          "where cId > {}".format(id)
    cur.execute(sql)
    conn.commit()
    t = {
        'success': True,
        'message': '',
        'data': {}
    }
    return json.dumps(t)

@Class.route('class_pro', methods=['POST'])
def class_pro():
    json_param = request.get_json()
    sql = "select id from cate " \
          "where cName = '{}'".format(json_param['cName'])
    cur.execute(sql)
    ID = cur.fetchall()[0][0]
    sql = "select * from pro " \
          "where cId={}".format(ID)
    cur.execute(sql)
    pro_list = cur.fetchall()
    conn.commit()
    t={
        'success': True,
        'message': '',
        'data': pro_list
    }
    return json.dumps(t, cls=DecimalEncoder)

#解决Decimal 不能被json格式化
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)
