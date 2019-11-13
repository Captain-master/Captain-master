from flask import Blueprint, request
import pymysql
import json

User = Blueprint('User', __name__, url_prefix='/user')

conn = pymysql.connect(host='123.207.27.133', user="admin", passwd="iot123456", db="shop", port=3306, charset="utf8")
cur = conn.cursor()

@User.route('user_list', methods = ['GET'])
def user_list():
    sql = "select * from user"
    cur.execute(sql)
    user_list = cur.fetchall()
    conn.commit()
    t = {
        'success': True,
        'message': '',
        'data': user_list
    }
    return json.dumps(t)

@User.route('chang_user', methods = ['POST'])
def chang_user():
    json_param = request.get_json()
    sql = "update user " \
          "set username = '{}', password = '{}', sex = '{}', email = '{}', face = '{}', regTime = '{}', activeFlag = {} " \
          "where username = '{}'".format(
        json_param['username'], json_param['password'], json_param['sex'], json_param['email'],
        json_param['face'], json_param['regTime'], json_param['activeFlag'], json_param['Username'])
    print(sql)
    cur.execute(sql)
    conn.commit()
    t = {
        'success': True,
        'message': '',
        'data': {}
    }
    return json.dumps(t)

@User.route('delete_user', methods = ['POST'])
def delete_user():
    json_param = request.get_json()
    sql = "select id from user where username = '{}'".format(json_param['username'])
    cur.execute(sql)
    ID = cur.fetchall()[0][0]
    sql = "delete from user where username = '{}'".format(json_param['username'])
    cur.execute(sql)
    sql = "update user " \
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

@User.route('search_user', methods = ['POST'])
def search_user():
    json_param = request.get_json()
    sql = "select * from user where username = '{}'".format(json_param['username'])
    cur.execute(sql)
    user = cur.fetchall()
    print(user)
    conn.commit()
    t = {
        'success': True,
        'message': '',
        'data': user
    }
    return json.dumps(t)

