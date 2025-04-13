# Building Url Dynamically
# Variable Rule
# Jinja 2 Template
'''
{{ }} - expression to print output in html

{%....%} - conditional , for loops

{#....#} - This is for comments 
'''


from flask import Flask,render_template,request,redirect,url_for

'''
It creates an instances of the flask class,
which will be your ( Web Server Gateway Interface ) application.
'''
app=Flask(__name__)


@app.route("/") # decorator 
# / act as a home 
# whenever useer go to home this / directs the user to welcome 
def welcome(): 
    return "<html><H1>Welcome to the Flask Course</H1></html>"

# Get method

@app.route("/index",methods=['GET']) 
def index(): 
    return render_template('index.html') 


#Post Method
@app.route('/submit_1',methods=['GET','POST']) # for this we have to use both 
def submit_1():
    if request.method =='POST': #
        name=request.form['name'] # we will retrive the message from form 
        return f'Hello {name}!' 
    return render_template('form.html')

# # Variable Rule
# @app.route('/success/<int:score>')
# def success(score):
#     return "The marks you got is "+ str(score) 


# Building Dynamic Variable
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',results=res) # condition res goes to result.html page 


# with expression 
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    exp={"score":score,"res":res} # instead of submiting a single value we use both

    return render_template('result1.html',results=exp) # exp goes 


# If Condition on Html
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html',results=score)


@app.route('/fail/<int>:score')
def fail(score):
    return render_template('result.html',results=score)


# Building URL dynamically 
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        math=float(request.form['math'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])

        total_score=(science+math+c+datascience)/4
    else:
        return render_template('getResult.html')
    return redirect(url_for('successres',score=total_score))





if __name__ == "__main__": 
    # entery point 
    # app start from here


    app.run(debug=True) # here debug make this code run without restarting whole in terminal    