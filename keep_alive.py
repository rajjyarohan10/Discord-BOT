'''
Developer: Rajjya Rohan Paudyal
File Name: keep_alive.py
Date: 5/20/2021
Description: 
    1.  This file contains code that helps keep this BOT alive 
        by constantly pinging the main source code
    2.  This way the BOT will continue to run through the help of servers
'''
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "We are alive, Go Vikings!Noikay"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()