from flask import Flask as flask
from flask import render_template
from flask import request

import serial
from twilio.rest import Client

preStatus = bool()

app = flask(__name__)

imageSec = [" "," "," "," "," "," "]
errorLink = str("error.png")
idleLink = str("noPro.png")

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout = 1)

inputData = int()
splitedData = [0,0,0,0,0,0]

def sendSMS():
    confirm = 0
    TWILIO_ACCOUNT_SID = 'ACd65df6789a2a7709c8cc5c674076e192'
    TWILIO_AUTH_TOKEN = 'f9b51a5f83dff22070fd35fa75e3060e'
    client=Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for i in range(6):
        if splitedData[i] == 1:
            if preStatus == 0:
                message = client.messages \
                    .create(
                        body="emergency",
                        from_='+12064880473',
                        to='+8294772718'
                    )
            preStatus = 1
            confirm = 1
            break

    if confirm == 0:
        preStatus = 0

@app.route('/')
def index():
    for i in range(6):
        if splitedData[i] == 1:
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
    
    
    while(1):
        SerialInput = input()
        print(SerialInput)
        splitedData = {}
        #if (ser.inWaiting() > 0):
        inputData = ser.read()
        splitedData = SplitData(int(SerialInput), 6)
        print(int(splitedData))
        sendSMS()

