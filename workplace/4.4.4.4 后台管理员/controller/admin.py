from flask import Blueprint, request
import pymysql
import json

Admin = Blueprint('admin', __name__, url_prefix='/admin')

conn = pymysql.connect(host='123.207.27.133', user="admin", passwd="iot123456", db="shop", port=3306, charset="utf8")
cur = conn.cursor()


@Admin.route('get_admin', methods=['GET'])
def get_admin():
    sql = "select * from admin"
    cur.execute(sql)
    admin_list = cur.fetchall()
    conn.commit()
    t = {
        'success': True,
        'message': '',
        'data': admin_list
    }
    return json.dumps(t)

@Admin.route('add_admin',methods=['POST'])
def add_admin():
    json_param = request.get_json()
    sql = "select max(id) from admin"
    cur.execute(sql)
    ID = cur.fetchall()[0][0]
    sql = "insert into admin(id, username,password,email) values ({}, '{}', '{}', '{}')".format(
        ID+1, json_param['username'], json_param['password'], json_param['email'])
    cur.execute(sql)
    conn.commit()
    t = {
        'success': True,
        'message': '',
        'data': {}
    }
    return json.dumps(t)

@Admin.route('delete_admin', methods=['POST'])
def delete_admin():
    json_param = request.get_json()
    sql = "select id from admin where username = '{}'".format(json_param['username'])
    cur.execute(sql)
    print(sql)
    ID = cur.fetchall()[0][0]
    sql = "delete from admin where username = '{}'".format(json_param['username'])
    cur.execute(sql)
    sql = "update admin " \
          "set id = id - 1 " \
          "where id > {}".format(ID)
    cur.execute(sql)
    conn.commit()
    t = {
        'success': True,
        'message': '',
        'data': {}
    }
    return json.dumps(t)