from flask import Flask, render_template, request, flash, redirect
import sqlite3
import pickle
import numpy as np
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)
chat_history = []
import pickle
modell=pickle.load(open('model/dt.pkl','rb'))

# Load Gemini AI model
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
gemini_model = genai.GenerativeModel('gemini-pro')
chat = gemini_model.start_chat(history=[])
    

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/crowd')
def crowd():
    return render_template('crowd.html')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        cursor.execute("SELECT password FROM user WHERE name = ?", (name,))
        result = cursor.fetchone()

        if result and check_password_hash(result[0], password):
            return render_template('fetal.html')
        else:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')

    return render_template('index.html')


@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email)

        command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
        cursor.execute(command)

        cursor.execute("INSERT INTO user VALUES (?, ?, ?, ?)", (name, generate_password_hash(password), mobile, email))
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/logout')
def logout():
    return render_template('index.html')


@app.route("/fetalPage", methods=['GET', 'POST'])
def fetalPage():
    return render_template('fetal.html')




@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    if request.method == 'POST':

        var1 = request.form['lat']
        var2 = request.form['lon']
        var3 = request.form['dep']

        var4 = request.form['depe']
        var5 = request.form['deps']
        var6 = request.form['mag']

        var7 = request.form['magt']
        var8 = request.form['mage']
        var9 = request.form['mags']

        var10 = request.form['gap']
        var11 = request.form['hord']
        var12 = request.form['hore']
        var13 = request.form['root']

        data = np.array([[var1, var2, var3, var4, var5, var6, var7,var8,var9,var10,var11,var12,var13]])
        result = modell.predict(data)[0]
        
        
        print(result)

        
        if result == 1 :
            res='Earth Quake Detected'
        elif result == 0: 
            res='NO Earth Quake'
        
        print(res)
        return render_template('predict.html', pred = result,status=res)

    return render_template('predict.html')

if __name__ == '__main__':
	app.run(debug = True)