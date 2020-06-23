import serial
import math
from twilio.rest import Client


import sqlite3
client = Client('ACd65df6789a2a7709c8cc5c674076e192', 'd68757bd4878d8c529bbc0f7b23cb8a7')


ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

resultData = ["0","0","0","0","0","0"]
getSerial = int()

preStatus = bool(0)

db = sqlite3.connect('sensorData.db')
curs = db.cursor()

def addData(moduleNum, temperature, humidity, batPer):
    curs.execute("INSERT INTO MODULEdata values(datetime('now'), (?), (?), (?), (?))", (moduleNum, temperature, humidity, batPer))
    db.commit()

def splitData(inputData, num):
    splitedData = []
    for i in range(num):
        splitedData.append(math.floor(inputData / (2** i)) % 2)
    return splitedData

def sendSMS(content, toNum):
    message = client.messages \
        .create(
            body = content,
            from_ = '+12064880473',
            to = toNum
        )

def TestConsole():
    resultString = str()
    resultData = []
    global preStatus
    getSerial = input("get data")
    print(getSerial)
    resultData = splitData(getSerial, 6)
    print(resultData)
    confirm = bool(0)
    for i in range(6):
        resultString += str(int(resultData[i]))
        if resultData[i] == 1:
            print(str(i) + " " + "pro")
            if preStatus == 0:
                #sendSMS("emergency",'+821094772718')
                print("send sms")
                preStatus = 1
            confirm = 1
    #DatabaseSetting
    if confirm == 0:
        preStatus = 0

def TestSerial():
    resultString = str()
    global resultData
    resultData = []
    global preStatus
    getSerial = ReadSerFromArduino()
    resultData = splitData(getSerial, 6)
    confirm = bool(0)                                       # This variable is to use to indicate whether any section has error
    for i in range(6):
        resultString += str(int(resultData[i]))
        if resultData[i] == 1:                              # the problem is arrived in that section
            print(str(i+1) + " " + "has the problem")
            if preStatus == 0:                              # only when the Twilio hasn't sent the SMS to users' phone
                sendSMS("emergency", '+821094772718')       # send Message to user
                preStatus = 1
            confirm = 1                                     # to indicate whether any section has error
    print (resultString)
    #DatabaseSetting
    if confirm == 0:
        if preStatus == 1:
            sendSMS("solved",'+821094772718')
        preStatus = 0                                       # to check that the section had the error at the last loop

def DatabaseSave(data[]):
    with db:
        cur.execute("INSERT INTO FARM_data VALUES(datetime('now') 30.5, 40)")

def ReadSerFromArduino():
    while(ser.inWaiting()==0):
        None
    inputTxt = str(ser.readline())
    inputTxt = inputTxt.rstrip('\n')
    inputTxt = inputTxt.rstrip('\r')
    inputInt = int(inputTxt)
    return inputInt

if __name__ == "__main__":
    while(1):
        TestSerial()
