from flask import Flask as flask
from flask import render_template
from flask import request

import GPIOsetting.py as statusNum

sectorStat[] = statusNum.splitedData

app = flask(__name__)

imageSec[] = str()
rboxLink = str("images/boxR.png")
bboxLink = str("images/boxB.png")

@app.route('/')
def index():
    for i in range(0,7):
        if sectorStat[i] == 1:
            imageSec[i] = bboxLink
        else:
            imageSec[i] = rboxLink
    return render_template('index.html', image_file_1 = image_link_1, image_file_2 = image_link_2 )

@app.route('/info')
def info():
    return 'Info'

if __name__ == "__main__":
    app.run(host='192.168.35.114')
