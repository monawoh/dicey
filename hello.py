# from flask import Flask, render_template, request
# app = Flask("MyApp")
#
# @app.route("/")
# def hello():
#     return "Hello World"
#
#
# @app.route ("/<name>")
# def hello_someone(name):
#         return render_template("hello.html", name=name.title())
#
#
#
# app.run(debug=True)
# FLASK_APP=hello.py flask run
#  * Serving Flask app "hello"
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    #
    # print 'hello world'





#
# import random
# # dice = random.randint(1,6)
# # dice1 = random.randint(1,6)
# # dice2 = random.randint(1,6)
# # print (dice,dice1,dice2)
# repeat = True
# while repeat:
#     dice = random.randint(1,6)
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     print "Your numbers are: ", (dice,dice1,dice2)
#     print("Do you want to roll again? Y/N")
#     repeat = ("y" or "yes") in input().lower()

import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)
    print random.randint(min, max)
    
    roll_again = raw_input("Roll the dices again?")
