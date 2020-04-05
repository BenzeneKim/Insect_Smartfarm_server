import serial

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

class serialData:
    def __init__(self, serPort, serBaud):
        self.serPort = port
        self.serBaud = buad
    
    def defineSer(self, serPort, serBaud):
        ser = serial.Serial(serPort, serBaud, timeout = 1)
        return ser

    def getData(self):
        result  = int()
        ser = defineSer('/dev/ttyAMA0', 9600)
        ser.open()
        if ser.inWaiting()>0:
              result = ser.read()
        return result
    
    def 
