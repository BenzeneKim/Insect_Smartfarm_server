from flask import Flask as flask
from flask import render_template
from flask import request

import serial
from twilio.rest import Client

TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
client=Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

preStatus = bool()


def sendSMS():
    global preStatus
    confirm = 0
    for i in range(6):
        if splitedData[i] == 1:
            if preStatus == 0:
                client.messages.create{
                    to = "+821094772718",
                    from_ = "+미국번호",
                    body = "emergency!!"
                }
            preStatus = 1
            confirm = 1
            break

    if confirm == 0:
        preStatus = 0


app = flask(__name__)

imageSec = [" "," "," "," "," "," "]
errorLink = str("images/error.png")
idleLink = str("images/noPro.png")

ser = serial.Serial('dev/ttyAMA0', 9600, timeout = 1)

inputData = int()
splitedData = {}
@app.route('/')
def index():
    for i in range(6):
        if sectorStat[i] == 1:
            imageSec[i] = errorLink
        else:
            imageSec[i] = idleLink
    return render_template('index.html', image_file_1 = imageSec[0], image_file_2 = imageSec[1], image_file_3 = imageSec[2], image_file_4 = imageSec[3], image_file_5 = imageSec[4], image_file_6 = image[5])

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
    global inputData, splitedData
    while:
        if (ser.inWaiting() > 0):
            inputData = ser.read()
            splitedData = SplitData(inputData, 6)
        sendSMS()

