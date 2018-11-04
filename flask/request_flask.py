# coding:utf-8
from flask import Flask, request, abort, jsonify
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

# request
@app.route('/login',methods=['GET','POST'])
def login():
    # http://localhost:5000/login
    # {"username":"root",	"password":"root"}
    if request.method == 'POST':
        print(request.json['username'])
        print(request.json['password'])
        return 'POST'
    # http://localhost:5000/login?username=root&password=root
    else:
        print(request.args['username'])
        print(request.args['password'])
        return 'GET'
 
users = []
@app.route('/add_user',methods=['POST'])
def add_user():
    if (not request.json or 'username' not in request.json 
    or 'password' not in request.json):
        abort(400)
    user = {'username':request.json['username'],
            'password':request.json['password']}
    users.append(user)
    return jsonify({'user_id':len(users)})

@app.route('/get_user',methods=['GET'])
def get_user():
    if not request.args or 'username' not in request.args:
        return jsonify(users)
    else:
        username = request.args['username']
        user = list(filter(lambda t: t['username'] == username,users))
        print(user)
        return jsonify(user) if user else jsonify({'result':'no found'})
# 获取form表单的数据 request.form.get('param')
# request.json 可以获取用Json body方式提交的数据, 
# request.is_json 可以用来检测body里是不是json类型的数据.

# 原始的body数据通过 request.data 访问

# 读取cookie
# request.cookies.get('name')
# cookies是一个类似字典的数据结构, 按照字典的方式访问即可. 
# 这个字典是只读的, 所以设置cookie要通过Response对象
# from flask import make_response
# response = make_response('<h1>Test</h1>')
# response.set_cookie('name', value)

# 如何获取headers?
# from flask import headers
# request.headers.get('Authorization')

# 如何实现页面转跳?
# from flask import redirect
# redirect('url')
from flask import redirect
@app.route('/gotobd')
def gotobd():
    # 页面重定向
    return redirect('https://www.baidu.com/')

if __name__ == '__main__':
    manager.run()