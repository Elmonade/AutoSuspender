import usocket as socket
import time
import DistanceSensor
import ujson

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendData(message):
    addr = socket.getaddrinfo('192.168.43.202', 1880)[0][-1]
    s.sendto(message, addr)
    print('Message sent.')

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
    humid = round(DistanceSensor.getHumidity())
    temp = round(DistanceSensor.getTemperature())
    while True:
        if cnt == 15:
            humid = round(DistanceSensor.getHumidity())
            temp = round(DistanceSensor.getTemperature())
            cnt = 0

        distance = DistanceSensor.calculateDistance()
        
        resultDict = {
            "Humidity": str(humid),
            "Temperature": str(temp),
            "Distance": str(distance)
        }
        
        message = build_json(resultDict)
        print(message)

        sendData(message)
        time.sleep(4)
        cnt += 1