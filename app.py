from flask import Flask,redirect,url_for

# WSGI Application - to interact with web server and web application
app=Flask(__name__)

# decorators along (Binding with) function
@app.route('/')
def welcome():
    return 'Welcome to Flask Learning, and development.....'

@app.route('/shreya')
def new():
    return '******************'


@app.route('/passfun/<int:score>')
def passfun(score):
    return "<html><body><h1>The person is Passed with marks :</h1></body></html>" + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person is failed with marks :' + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        #passed a function here
        result="fail"
    else:
        result="passfun"
    return redirect(url_for(result,score=marks))


if __name__=="__main__":
    app.run(debug=True)