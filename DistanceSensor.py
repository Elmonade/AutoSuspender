import utime
import pycom
from machine import Pin
from pycoproc_2 import Pycoproc 
from SI7006A20 import SI7006A20

ECHO = Pin('P10', mode=Pin.IN) 
TRIGGER = Pin('P9', mode=Pin.OUT)
py = Pycoproc()
dht = SI7006A20(py)

def getHumidity():
    return dht.humidity()

def getTemperature():
    return dht.temperature()

TRIGGER(0)
def calculateTime():
    # TRIGGER pulse LOW for 2us (just in case)
    TRIGGER(0)
    utime.sleep_us(2)
    # TRIGGER HIGH for a 10us pulse
    TRIGGER(1)
    utime.sleep_us(10)
    TRIGGER(0)

    # wait for the rising edge of the ECHO then start timer
    while ECHO() == 0:
        pass
    start = utime.ticks_us()

    # wait for end of ECHO pulse then stop timer
    while ECHO() == 1:
        pass
    finish = utime.ticks_us()

    # pause for 20ms to prevent overlapping ECHOs
    utime.sleep_ms(20)

    return (utime.ticks_diff(start, finish))

def calculateDistance():
    temp = dht.temperature()
    humid =dht.humidity()

    # SoundSpeed = 20.05 * (Tk)**0.5
    # Tk = 273.15 + Tc
    soundSpeed = 20.05 * (273.16 + temp) ** 0.5
    print("Speed of sound in current environment: ", round(soundSpeed))

    # Distance to an object = ((speed of sound in the air)*time)/2
    time = calculateTime()
    soundSpeed /= -10000
    distance = (time * soundSpeed)/2
    print("Distance from the monitor to user: ", round(distance), "cm.")
    return round(distance)