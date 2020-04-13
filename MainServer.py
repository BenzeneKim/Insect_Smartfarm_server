from flask import Flask as flask
from flask import render_template
from flask import request

import serial
from GPIOsetting import resultData
app = flask(__name__)

imageSec = [" "," "," "," "," "," "]
errorLink = str("error.png")
idleLink = str("noPro.png")
    
@app.route('/')
def index():
    for i in range(6):
        if resultData[i] == 1:
            imageSec[i] = errorLink
        else:
            imageSec[i] = idleLink
    return render_template('index.html', image_file_1 = imageSec[0], image_file_2 = imageSec[1], image_file_3 = imageSec[2], image_file_4 = imageSec[3], image_file_5 = imageSec[4], image_file_6 = imageSec[5])

@app.route('/info')
def info():
    return 'Info'

def SplitData(Input, Num):
    result = []
    for i in range(Num):
        result.append(floor(Input / 2 ^ Num) % 2)

    return result


if __name__ == "__main__":
    app.run(host='192.168.35.114')
