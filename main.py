import mysql.connector as mysql
from flask import Flask, render_template

'''mysql.connect(host='localhost', 
            database='database', 
            user='root', 
            password='your password') '''



app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')
if __name__ =="__main__":
  app.run(host="0.0.0.0", debug=True)
