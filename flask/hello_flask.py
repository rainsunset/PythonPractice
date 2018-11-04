# coding:utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hello')
def hello_fladk():
    return 'Hello Flask'

# 路径变量 
# string	默认选项，接受除了斜杠之外的字符串
# int	接受整数
# float	接受浮点数
# path	和string类似，不过可以接受带斜杠的字符串
# any	匹配任何一种转换器
# uuid	接受UUID字符串

@app.route('/hello/<username>')
def hello_user(username):
    return 'Hello %s' % username 

@app.route('/age/<int:age>')
def print_age(age):
    return 'You are %d Years old？' % age

@app.route('/chufa/<int:fenmu>')
def chufa_test(fenmu):
    print(100/fenmu)
    return 'success'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('hello'))
#     print(url_for('hello',next='/'))
#     print(url_for('hello',username='HaHa'))

if __name__ == '__main__':
    '''
    start with : 'python hello_flask.py'
    '''
    # app.run(debug=True,port='5000',host='0.0.0.0')
    '''
    start with : 'python hello_flask.py 0.0.0.0 5000 True'
    question: 难道第一个参数不应该是 “0.0.0.0” 么？
    '''
    # import sys
    # argvs = sys.argv
    # print(argvs)
    # app.run(host=argvs[1],port=argvs[2],debug=argvs[3])
    '''
    need insatll flask-script
    start with : python hello_flask.py runserver -h 0.0.0.0 -p 5000 -d
    add '-d' means:open debug 
    '''
    from flask_script import Manager
    manager = Manager(app)
    manager.run()