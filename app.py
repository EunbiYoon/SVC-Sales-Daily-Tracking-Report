from flask import Flask, render_template
# from graph import piechart, areachart
import numpy as np
import json
import sys

dictionary = ["10","20","30","40","50","60","70","80","90","100","110","120","130"]
action="thisisworkign"


# with open('static/assets/demo/declare.js','w') as outfile:
#   outfile.write("const jsonstr={}".format(dictionary))
#   outfile.write(";\n")
#   outfile.write('const jsonstr1="{}"'.format(action))
#   outfile.write(";\n")





app = Flask(__name__)

# a=piechart()
# b=areachart()
# print("aa")
# print(a)
# print("bb")
# print(b)


@app.route("/")
def index():
    return render_template("index.html")
 
if __name__ == "__main__":
  app.run()