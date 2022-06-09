#coding=utf-8
from flask import Flask
from flask import request
import json


#flask 是个应用程序
app = Flask(__name__)

'''
简单get
'''
# @app.route('/')
# def login():
#     data = json.dumps({
#         "username":"Jason",
#         "password":"11111",
#     })
#     return data

'''
get 请求
'''
@app.route('/passport/user/get_login',methods = ['GET'])
def get_login():
    username = request.args.get('username')
    password = request.args.get('password')

    if username and password:
        data = json.dumps({
            "username":username,
            "password":password,
            'code':'200',
            'message':'登陆成功',
            'info':'www.baidu.com',
        })
    else:
        data = json.dumps({
            'message':'请传参数',
        })
    return data

'''
post 请求
'''
@app.route('/passport/user/post_login',methods = ['POST'])
def post_login():
    request_method = request.method

    if request_method == 'POST':
        username = request.form.get("username")
        password = request.form.get('password')
        data = json.dumps({
            "username":username,
            "password":password,
            'code':'200',
            'message':'登陆成功',
            'info':'www.baidu.com',
        })
    else:
        data = json.dumps({
            'message':'请求不合法',
        })
    return data



if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=5000)