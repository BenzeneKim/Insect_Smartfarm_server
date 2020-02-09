import serial

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

inputData = int()
sectionNum = int()
splitedData = []


def splitdata(inputData, sectionNum):
    data = []

    for i in range(sectionNum):
        data[i]=math.floor(inputData / 2^(sectionNum-1))%2

    return data

def main()
    inputData = ser.read()
    sectionNum = 1
    
    splitedData = splitdata(inputData, sectionNum)

if __name__ == "__main__":
    main()
