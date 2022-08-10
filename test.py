# We will write a function here and call from somewhere else. like from postman.
# Call the entire function from Postman.


# currently flask is not installed
# flask is just a library
# library gives a function or methods to perform various operations.
# pythonic library to explore your function and called be called from anywhere

from flask import Flask, request, jsonify

app = Flask(__name__)  # object of a flask

# name is a function which it is going to import
# how can we make the function available to the outside world
# currently the function is in the pycharm
# currently the function is available locally
# 1. First we have to find out at which location this function is running.
# In order to get that we create a root to get th address
# root .. like homepage of a page e.g. ineuron.ai
# So we need to get the root of this function
# 2. Create the root
# Currently we cant access it from outside.
@app.route('/xyz', methods= ['GET', 'POST'])
# route is a function available in flask
# if anyone hit this function will get the below function
# accessability and security
# GET: sends the data(query) to a server and then we get the response from the server
# Get: It tried to send the data. And we are able to see the query. Here the dataset is exposed.
# send a data through a URL
# e.g. search on a google
#
# POST: Sends the Post: It tried to send the data.
# But we are unable to see the query. We are unable to see the data.
# When we are sending a data through a body.( it will be encrypted or hidden not visible )
# e.g. sign in to the gmail.

# "/" is trying to help your to reach out to a particular root in the above example at "xyz"

def test():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return  jsonify(str(result))
@app.route('/adi/test1', methods= ['POST'])
# We bind the entire below function with the location '/adi/test1'
def test1():
    if(request.method == 'POST'):
        a = request.json['num3']
        b = request.json['num4']
        result = a + b
        return  jsonify(str(result))
@app.route('/adi/test2', methods= ['POST'])
def test2():
    if(request.method == 'POST'):
        a = request.json['num5']
        b = request.json['num6']
        result = a + b
        return  jsonify(str(result))
@app.route('/adi/test3', methods= ['POST'])
def test3():
    if(request.method == 'POST'):
        a = request.json['adviteeya']
        b = request.json['shrav']
        result = a + b
        return  jsonify(str(result))

# Now we have to execute the app or call the app
# We can call any method or function in main method
if __name__ == '__main__':
    app.run()

# we are calling the function "test" via url.