from flask import Flask,render_template

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


@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == "__main__": 
    # entery point 
    # app start from here


    app.run(debug=True) # here debug make this code run without restarting whole in terminal   