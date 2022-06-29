import usocket as socket
import time
import DistanceSensor
import ujson

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendData(message, expectResponse):
    addr = socket.getaddrinfo('192.168.43.202', 1880)[0][-1]
    s.sendto(message, addr)
    print('Message sent.')

    if(expectResponse):
        response = s.recv(1024)
        print('Message received:', response)
        return response


def build_json(resultDict):
    try:
        retValue = ujson.dumps(resultDict)
        return retValue
    except:
        return None

if __name__=="__main__":
    cnt = 0
    absenceCnt = 0
    expectResponse = False
    humid = round(DistanceSensor.getHumidity())
    temp = round(DistanceSensor.getTemperature())
    while True:
        # Check humidity and temperature every 20 seconds.
        if cnt == 20:
            humid = round(DistanceSensor.getHumidity())
            temp = round(DistanceSensor.getTemperature())
            cnt = 0

        # Update distance every second.
        distance = DistanceSensor.calculateDistance(temp)
        if (distance > 70):
            absenceCnt += 1
        
        resultDict = {
            "Humidity": str(humid),
            "Temperature": str(temp),
            "Distance": str(distance),
            "Verify": str(absenceCnt)
        }
        
        message = build_json(resultDict)
        print(message)

        sendData(message, expectResponse)
        if (absenceCnt == 4):
            absenceCnt = 0

        time.sleep(1)
        cnt += 1