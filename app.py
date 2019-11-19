from flask import Flask, redirect, url_for, request, render_template, make_response, session

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/hello/<name>")
def hello_name(name):
    return 'hello %s' % name


@app.route("/urlfor/<name>")  # 重定向练习
def hello_url(name):
    return redirect(url_for('hello_name', name=name))  # hello_name 表示hello_name函数， name 表示里面的参数


@app.route('/success1/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))  # success 表示success函数， name 表示里面的参数
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/result', methods=['POST'])
def result_student():
    return render_template('result.html', result=request.form)


@app.route('/hello_template/<user>')
def hello_template(user):
    return render_template('hello.html', name=user)


@app.route('/setcookie', methods=['POST'])
def setCookie():
    user = request.form['nm']
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)
    return resp


@app.route('/getcookie')
def getCookie():
    return request.cookies.get('userID')


#######################  session  #######################
app.secret_key = 'asdfsdfasjdfh' #任意字符串
@app.route('/session')
def sessionIndex():
    if 'username' in session:
        username = session['username']
        return render_template('helloSession.html', type='logout', username=username)
    return render_template('helloSession.html')


@app.route('/sessionlogin', methods=['GET', 'POST'])
def session_login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('sessionIndex'))
    return render_template('helloSession.html', type='login')


@app.route('/sessionlogout')
def session_logout():
    session.pop('username', None)
    return redirect(url_for('sessionIndex'))


if __name__ == '__main__':
    app.run()
