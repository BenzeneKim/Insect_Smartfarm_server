import serial

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

inputData = int()
sectionNum = int()
splitedData = []


def splitdata(inputNum, section):
    data = []
    for i in range(section):
        data[i]=math.floor(inputNum / 2^(section-1))%2

    return data

def main()
    if ser.inWaiting():
        inputData = ser.read()
    sectionNum = 6
    
    splitedData = splitdata(inputData, sectionNum)

if __name__ == "__main__":
    main()
