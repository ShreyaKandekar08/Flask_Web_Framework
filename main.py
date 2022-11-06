# Integrating HTML with Flask
# HTTP Verb - GET and POST

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

# Jinja2 template engine
'''
{%...%} conditional statements, if loop, for loop, etc
{{    }} expression to print output
{#...#} this is for comment

The output is {{ result }} 

    
    {% if result>=50 %}
    <h1> The Result is Pass</h1>
    {% else %}
    <h1> The Result is Fail</h1>
    {% endif %} 

'''

@app.route('/')
def welcome():
    return render_template('index.html') 

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    exp = {'score':score,'res':res}
    return render_template('result.html',result=exp)

    # return render_template('result.html',result=score)

@app.route('/passfun/<int:score>')
def passfun(score):
    return "<html><body><h1>The person is Passed with marks :</h1></body></html>" + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person is failed with marks :' + str(score)

# Result Checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        #passed a function here
        result="fail"
    else:
        result="passfun"
    return redirect(url_for(result,score=marks))

#Result checker HTML page

@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""
    return redirect(url_for('success',score=total_score))    

if __name__=="__main__":
    app.run(debug=True)