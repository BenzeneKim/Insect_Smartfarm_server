import serial
import math
from twilio.rest import Client

client = Client('ACd65df6789a2a7709c8cc5c674076e192', 'f9b51a5f83dff22070fd35fa75e3060e')


ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

resultData = []
getSerial = int()


preStatus = bool(0)

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
    global preStatus
    getSerial = input("get data")
    print(getSerial)
    resultData = splitData(getSerial, 6)
    print(resultData)
    confirm = bool(0)
    for i in range(6):
        if resultData[i] == 1:
            print(str(i) + " " + "pro")
            if preStatus == 0:
                sendSMS("emergency",'+821094772718')
                preStatus = 1
            confirm = 1
    if confirm == 0:
        preStatus = 0


def TestSerial():
    getSerial = ser.readline()
    resultData = splitedData(getSerial, 6)

while(1):
    TestConsole()
