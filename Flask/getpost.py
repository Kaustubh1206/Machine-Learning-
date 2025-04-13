from flask import Flask,render_template,request

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


@app.route("/index",methods=['GET']) # get method
def index(): 
    return render_template('index.html') 


@app.route('/form',methods=['GET','POST']) # for this we have to use both 
def form():
    if request.method =='POST': #
        name=request.form['name'] # we will retrive the message from form 
        return f'Hello {name}!' 
    return render_template('form.html')


@app.route('/submit',methods=['GET','POST']) # for this we have to use both 
def submit():
    if request.method =='POST': #
        name=request.form['name'] # we will retrive the message from form 
        return f'Hello {name}!' 
    return render_template('form.html')
if __name__ == "__main__": 
    # entery point 
    # app start from here


    app.run(debug=True) # here debug make this code run without restarting whole in terminal    