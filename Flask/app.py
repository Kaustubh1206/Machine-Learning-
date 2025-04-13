from flask import Flask
'''
It creates an instances of the flask class,
which will be your ( Web Server Gateway Interface ) application.
'''
app=Flask(__name__)


@app.route("/") # decorator 
# / act as a home 
# whenever useer go to home this / directs the user to welcome 
def welcome(): 
    return " Welcome to thisbest  Flask Zpp. This is an extended messa euse to show debug funct"


@app.route("/index")
def index():
    return " Welcome to index Page"

if __name__ == "__main__": 
    # entery point 
    # app start from here


    app.run(debug=True,port=8000) # here debug make this code run without restarting whole in terminal