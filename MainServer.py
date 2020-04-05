from flask import Flask as flask
from flask import render_template
from flask import request

import serial

sectorStat = statusNum.splitedData

app = flask(__name__)

imageSec = [" "," "," "," "," "," "]
rboxLink = str("images/boxR.png")
bboxLink = str("images/boxB.png")

ser = serial.Serial('dev/ttyAMA0', 9600, timeout = 1)

inputData = int()

@app.route('/')
def index():
    for i in range(6):
        if sectorStat[i] == 1:
            imageSec[i] = bboxLink
        else:
            imageSec[i] = rboxLink
    return render_template('index.html', image_file_1 = image_link_1, image_file_2 = image_link_2 )

@app.route('/info')
def info():
    return 'Info'

def SplitData(Input, Num):
    

if __name__ == "__main__":
    app.run(host='192.168.35.114')
    global inputData
    while:
        if (ser.inWaiting() > 0):
            inputData = ser.read()
            
