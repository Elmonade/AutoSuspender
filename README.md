# Auto Suspender

**Batjigdrel Bataa / BB222MF**

With the help of ultrasonic distance sensor user's desktop will be suspended automatically whenever user leaves the specified range. To further
increase the accuracy of the distance detection process additional sensors are integrated to the system.

**Amount of time required to replicate the project: ~1 hour**

# Objective

Due to severa lack of time management and self control, my desktop hardly shuts down. Often it hits couple days of uptime. Which is not environment
friendly behaviour and it puts major strain on the desktop computer itself. In order to mitigate the issue however little it may, I chose this project.

Average desktop computers consume several hundred watts. High end computers could consume upwards of over 1kwatts. In order to minimise the power
consumption, suspending the computer is safest and easiest solution due to harmless behaviour towards users workflow by letting the user resume 
their work without major delay. 

By working with this project, one can attain knowledge on intricate details of how certain sensors work, how machines percieve their surrounding.
Further more, what can be done with the newly acquired data.

# Materials needed

Component | Part of | Bought at | Price* 
-| -| -| -
fipy                 |LNU - 1DT305 Applied IoT - FiPy and sensors bundle | electrokit.com | 694 SEK**
pysense              |LNU - 1DT305 Applied IoT - FiPy and sensors bundle | electrokit.com | 317 SEK**
Jumper wires         |LNU - 1DT305 Applied IoT - FiPy and sensors bundle | electrokit.com | 100 SEK**
Bread board          |LNU - 1DT305 Applied IoT - FiPy and sensors bundle | electrokit.com | 100 SEK**
HC-SR04 sensor       || amazon.se | 112 SEK
Micro USB cable***   |||

\* All prices are approximates.

\** Components were part of a kit, thus they may be cheaper when bought individually.

\*** USB cable was already in possession and free.

![FiPy](./images/fipy.png)
Figure 1: pycom fipy.
The microcontroller used in this project. Responsible for reading data from connected sensors and sending the data to given remote server.
![PySense](./images/pysense.png)
Figure 2: pycom pysense.
Additional board which gives access to SD card reader, battery connection, and 5 more built-in sensors for the connected microcontroller. However,
this board covers up all the pins on the microcontroller blocking the further connection to different sensors. Additional wiring is required to
expose the pins.
![JumperWires](./images/JumperWires.jpg)
Figure 3: Male-to-Male jumper wires.
Main connection method used in this project. It is a Male-to-Male type.
![BreadBoard](./images/BreadBoard.jpg)
Figure 4: Bread board.
Serve as a base of connection. If further information required toturials are provided from the university.
![DistanceSensor](./images/HC-SR04.jpg)
Figure 5: HC-SR04 ultrasonic distance sensor.
A sensor that uses ultrasonic sound wave to detect the distance.

# Computer setup (Windows 10 OS)

**Setting up the IDE:**

The first step in setting up the LoPy4 is to update the firmware on the expansion board, if necessary, which was not needed in this project. The procedure differs between operating systems and a thorough guide on how to do it can be found at <https://docs.pycom.io/updatefirmware/expansionboard/>.

Next, the firmware of the LoPy4 needs to be updated. This is done by using pycom's update tool. The tool and a guide on how to update the firmware can be found at <https://docs.pycom.io/updatefirmware/device/>. In the case of this prject, the Pybytes firmware was chosen.

After updating the firmware, the programme Node.js needs to be installed. For Windows OS, the installer can be downloaded here <https://nodejs.org/en/>. Next, an IDE needs to be chosen. In this case, Atom.io was used which can be downloaded and installed here <https://atom.io/>. Note that also the latest Python version must be installed. It can be found here <https://www.python.org/downloads/>.

After setting up Atom.io the pymakr plugin needs to be installed which will enable the flashing of code to the LoPy4. The plugin can be installed directly in Atom using Atom > Preferences > Install and searching for the pymakr plugin. A torough guide on this can be found here <https://docs.pycom.io/gettingstarted/software/atom/>.


**Creating a project:**

A new project can be created by either creating a new directory directly in Atom (left panel) or by creating it in the Explorer and opening it in Atom. Each project directory should include a directory called lib into which necessary libraries can be copied. Further, a file called boot.py and a file called main.py need to be created in the project directory. Note that these files must be located directly in the project directory and not in lib. The file main.py will include the functionality of the code to be run on the device while the file boot.py is always run before main.py and can include the setup of wireless connections to keep the file main.py tidy.

Another file which can be created is a file including credentials like WiFi SSIDs, passwords and tokens. It may be called credentials.py and can be referred to in main.py and boot.py (see code below for examples). By using such a file, the code can be securely shared with others.


**Troubleshooting:**
Lastly, a change in the project settings may be necessary. When trying to upload a project to the LoPy a "core panic" error can occur which will result in a failed upload of the project. If this happens, the project settings need to be opened by clicking on setings in the right lower corner of Atom. This will create a file called pymakr.conf in which the value of "safe_boot_on_upload" needs to be set to false. Then, always before uploading code to the pycom a manual safe boot needs to be executed by pressing the Reset button on the LoPy shortly while keeping the Safe Boot button on the expansion board pressed. Now the onboard LED should flash orange and the Safe Boot button can be released. After the safe boot the project can be uploaded.

Always save the files before uploading :)

Figure 2 shows an example for a project in Atom and the project settings panel is highlighted.


![](https://i.imgur.com/BFBCRLj.jpg)
Figure 2: Example for a project in Atom


# Putting everything together:

The setup of the device and the wiring is shown in a circuit diagram in Figure 3. Note that the LoPy is not shown in the diagram.

![](https://i.imgur.com/ofuqJ4y.jpg)
Figure 3: Wiring of the components

The LoPy is the heart of the setup which is mounted on the pycom expansion board for easier connectivity. The expansion board is connected via an USB cable to a power supply or a PC to transfer code.

All sensors are connected to the expansion board via a breadbord. First, the 3.3 V output pin on the expansion board is connected to the breadboard's power supply line while the GND line of the breadboard is connected to the GND pin of the expansion board. To utilise the complete breadboard and to enable a parallel setup of both LDR sensors, the power supply lines and the GND lines on both sides of the breadboard are connected accordingly. Further, jumper wires on the breadboard connect the lines on which sensors are mounted with the power supply line and the GND line of the breadboard.

The DHT11 temperature and humidity sensor was used in the three pin version. In this version, the left pin provides the measured data, the middle pin needs to be connected to the power supply and the right pin to the GND. Thus, the breadboard line with the left pin is connected to the expansion board's pin P23 while the other pins are connected to the according breadboard lines.

Two LDRs are conected to the breadboard. One of them is located at the window sill, the other on the table. Thus, they can be seperated by the shutters and, in that case, provide different outputs. The two LDRs are connected in the same way on each side of the breadboard, so the setup is only described once. In order for the LoPy to measure the change in restistance, a voltage divider needs to be set up. This is done by connecting the power supply first to one leg of a 10 kOhm resistor. Then, in the line where the second leg of the resistor is located a data wire is used to connect this line with an input pin of the expansion board. Here, pin P13 for the LDR on the table and pin P14 for the LDR at the window are used. Lastly, one leg of the LDR is connected via a Male/Female wire to the same line as the second leg of the resistor and the data wire and, again, via a Male/Female wire to a line on the breadboard which is connected to the GND line.

The voltage divider makes it possible for the LoPy to interpret the changes in resistance of the LDRs. By installing the 10 kOhm resistor, a reference point is set up from which a voltage can be measured. This voltage differs according to the the changing resistance of the LDR. A voltage divider calculator for the different values for voltages and resistances can be found at <https://ohmslawcalculator.com/voltage-divider-calculator>.

This setup is only intended as a development setup and not for production, according to the purpose of the project.


# Chosen platform

During the project, two different platforms were used. First, the device was connected to the Pybytes platform. It is a free cloud platform for data collection and visualisation run by Pycom. It was used in the beginning because it offers a simple way to connect devices via WiFi and to receive and display the data collected by the sensors. Also, it features an online pymakr plugin which allows to manipulate the code on the device from the cloud. Nevertheless, the functionality of the platform is limited. Specifically, the lack of a possibility to send e-mails triggered by some event in the measured data was the reason which led to the choice to use another platform.

Later, Ubidots was chosen as the new platform to be used. It is also a cloud service which is free to use for private and educational purposes but also offers a paid subscription with more functionality or for commercial use. For this project, the free version is sufficient since it offers the opportunity to trigger the sending of an e-mail based on the received data. Regarding the display of measured data, Ubidots offfers a neat Dashboard which can be customised in many ways. Further, the service offers the opportunity to analyse the data online in simple ways and it is possible to export the data for more sophisticated analysis. The overview page of the temperature variable as an example is shown in Figure 4.

![](https://i.imgur.com/PJ2xrwZ.jpg)
Figure 4: Overview page of the temperature variable in Ubidots

So far, there is no intent to scale the idea. However, it is possible, for instance by monitoring several working places at home or in a bureau. For these purposes Ubidots may be a good choice as well since it is possible to register several devices there.


# The code

First, shown in code snippet 1, the necessary libraries need to be imported into the file main.py. Here it is important to include the libraries DHT and urequests in the project's lib directory. Also, a file credentials.py including the WiFi credentials and the user's tokens needs to be imported here. Further, two helping variables are defined: The variable delay is the time the device sleeps after each iteration and prompt_count is a helping variable for a piece of functionality described below.

Code snippet 1: Importing libraries and defining helping variables
```python=
import pycom
import urequests as requests
import machine
from machine import Pin
import time
import binascii
from dht import DHT
import credentials


delay = 60 * 15

prompt_count = 0
```

Next, displayed in code snippet 2, the sensors need to be set up. The DHT11 sensor is set up using the DHT library. For setting it up, code provided by David M via gitlab was used. For setting up the two LDRs, first the input pin and an analog to digital converter are defined for each. Then, a function is defined which returns the digital value measured at the input pin.

Code snippet 2: Setup of the sensors (after snippet 6)
```python=
th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
time.sleep(2)

adc_w = machine.ADC()
apin_w = adc_w.channel(pin='P14')

adc_t = machine.ADC()
apin_t = adc_t.channel(pin='P13')

def light_measure(pin_input):
    light = pin_input()
    return light
```

Code snippet 3 shows the data measurements. Temperature, humidity and the light values are measured and saved as according variables and the values are printed to the console.

Code snippet 3: Measuring data (within while loop; After snippet 2)
```python=
while True:

    result = th.read()
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()

    temperature = result.temperature
    humidity = result.humidity

    print('Temp: ', temperature)
    print()
    print('RH: ', humidity)
    print()

    light_w = light_measure(apin_w)
    print('Light window: ', light_w)
    print('')

    light_t = light_measure(apin_t)
    print('Light table: ', light_t)
    print('')
```

In code snippet 4, the core functionality of the code is displayed. That is, checking whether the shutters need to be closed and if a prompt to do so needs to be sent. First, necessary helping variables are defined and set to their default values. 

Next, it is checked whether the sunlight is intense and if the shutters are open by checking the value of the window sill LDR. Then, if the difference between the measured light values at the window sill and the table is sufficiently high, closed shutters are indicated.

Following this, the consequences of the variables' values are defined. 

If both sunlight and shutters_open are True, a prompt to close the shutters needs to be sent. Thus, the variable close_shutters_prompt is set to 1. It is sent to Ubidots in the end of the iteration where it triggers an e-mail with the prompt to be sent. Further, a prompt is printed to the console and the onboard LED is turned red. Also, the helping variable prompt_count is changed within the satement. This is done to avoid the e-mail from being sent to often. By triggering the prompt only when the variable is reset, incrementing the variable four times and resetting it after the fourth iteration, the prompt is only sent once per hour.

If the shutters are closed and a prompt was sent by e-mail, indicated by prompt_count > 0, the variable thank_you_statement is set to 1. It is sent to Ubidots in the end of the iteration and triggers an e-mail with a Thank you statement. Also, the statement is printed to the console, the onboard LED is set to green and the variable prompt_count is reset. The last step avoids the statement from being sent more than once.

Lastly, in all other cases no prompt is sent, the LED is turned green and the prompt_count variable is reset in preparation for the next day.

Code snippet 4: Defining the logic for the shutter close prompt (within while loop; After snippet 3)
```python=
    sunlight = False
    shutters_open = True
    close_shutters_prompt = 0
    thank_you_statement = 0

    if light_w < 600:
        sunlight = True

    if light_t > (light_w + 1500):
        shutters_open = False

    if sunlight == True and shutters_open == True:
        if prompt_count == 4:
            prompt_count = 0
        if prompt_count == 0:
            close_shutters_prompt = 1
            print('Close the shutters, please!')
            print()
        prompt_count += 1
        pycom.rgbled(0xFF0000)

    if shutters_open == False and prompt_count > 0:
        thank_you_statement = 1
        print('Thank you for closing the shutters!')
        print()
        prompt_count = 0
        pycom.rgbled(0x007f00)

    else:
        prompt_count = 0
        pycom.rgbled(0x007f00)
```

Further code snippets used to build up a wireless connection and to transmit data are shown in the next section.


# Transmitting the data / connectivity

In this project, the data is sent every 15 minutes via WiFi as a json object using the HTTP protocol. 

15 minutes were chosen because this amount of time represents a good balance between providing a precise enough overview on how the temperature and humidity change over time while not sending data too often. Further, it is enough to control the change in sunlight intensity every 15 minutes since it does not change fast enough to justify a shorter interval. In this project, the battery lifetime is not of high importance since the device is located on a desk with a permanently available power supply.

WiFi was chosen out of two reasons. First, since the device is located on the desk it can be easily connected to the home WiFi network. Thus, it can be set up in a simple way and no subscription to a service offering other protocols is necessary. Secondly, the device is located on the island Gotland where there is poor coverage for protocols like LoRa and Sigfox, making it impossible to use them for this project. As shown, battery life is no problem here and range considerations are also not of high importance, making WiFi a feasible choice. The WiFi connection is built up in the boot.py file, as shown below. The code for the WiFi setup is based on the example code of John Lindblad available at <https://hackmd.io/@JohnLindblad/rJNKFZWAU#The-code> and displayed in code snippet 5.

Code snippet 5: The file boot.py with setup of WiFi
```python=
from network import WLAN
import machine
import time
import pycom
import credentials

pycom.heartbeat(False)

pycom.pybytes_on_boot(False)

wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.INT_ANT)
wlan.connect(credentials.wifi_ssid, auth=(WLAN.WPA2, credentials.wifi_password), timeout=5000)

while not wlan.isconnected ():
    machine.idle()
if wlan.isconnected() == True:
    print()
    print("Connected to Wifi\n")
```

The choice of sending the data via HTTP as a json object was made since this is a simple way to transfer the data to Ubidots. The follwoing code snippets of main.py are responsible for transmitting the data and the guide on how to transmit data via HTTP to Ubidots used can be found at <https://help.ubidots.com/en/articles/961994-connect-any-pycom-board-to-ubidots-using-wi-fi-over-http>. Note that it is necessary to include the library urequests.py in the lib folder of the projects which can be found in the guide above and that. The necessary code is shown in snippets 6 and 7.

Code snippet 6: Defining functions to create a json object and posting it to Ubidots via HTTP (After snippet 1)
``` python=
def build_json(variable1, value1, variable2, value2, variable3, value3, variable4, value4):
    try:
        data = {variable1: {"value": value1},
                variable2: {"value": value2},
                variable3: {"value": value3},
                variable4: {"value": value4}}
        return data
    except:
        return None

def post_var(device, value1, value2, value3, value4):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": credentials.ubidots_token, "Content-Type": "application/json"}
        data = build_json("Temperature", value1, "Humidity", value2, "Close_shutters_prompt", value3, "Thank_you_statement", value4)
        if data is not None:
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass
```

Code snippet 7: Calling the function to post data to Ubidots via HTTP (within while loop; After snippet 4)
```python=
    post_var("LTH", temperature, humidity, close_shutters_prompt, thank_you_statement)
```



# Presenting the data

**Dashboard:**

The customised Dashboard is displayed in Figures 5 and 6 which includes the variables Desk temperature, Relative humidity and Shutter close prompt. For the Desk temperature, a thermostate symbol was chosen which also displays the value in written from and the time of the last update. For the Relative humidity a water tank symbol was chosen which includes the written last measured value. Lastly, the Shutter close prompt is shown as a On/Off button which is Off by default and turns on when the shutters need to be closed.

![](https://i.imgur.com/POTBNXL.jpg)
Figure 5: Dashboard in Ubidots with active shutter close prompt

![](https://i.imgur.com/DPh1UBX.jpg)
Figure 6: Dashboard in Ubidots with inactive shutter close prompt


**Database:**

Regarding the choice of database, for this project the built-in database of Ubidots is used. Data is saved every 15 minutes and the data of up to one year can be displayed online. Further, it is possible to export the data to preserve it for longer time. However, this is not planned for this project. The built-in database was chosen because it is sufficient to fulfill the purpose of this project.


**Triggered events:**

A core functionality of the project is possible through a triggered event in Ubidots. Whenever the variable close_shutters_prompt is set to 1, an event in Ubidots is activated which sends an e-mail to the author's adress prompting to close the shutters. A second event is triggered after the shutters were closed. In that case, the thank_you_statement variable is turned to 1 and another e-mail is sent. This serves as a confirmation that the device noticed the closing of the shutters and will not send more close prompts.


# Finalizing the design

Reflecting on the project, the purpose could be fulfilled. First, the intended functionalities could be implemented. Further, thanks to the collected data the fitting temperature and humidity for a good working environment could be found. Also, the monitoring of the data can help to maintain a good working environment.

In addition, valuable insights into the topics of IOT, electronics and programming could be gained. Several problems occured along the way but all of them could be solved eventually. Some of the problems were solved with help of more experienced users while some could be solved by own research and ideas. Thus, lessons could be learned for future projects.

Considering aspects which could have been done differently, a few points are apparent. First, it is possible to use even more sensors to get more thorough data on the working environment. For example, a sensor measuring the air quality could be included, prompting to open the window when the carbon dioxide level gets to high. Also, further processing and analysis of the collected data is possible. Aside these points, the device may be used to automate the closing of the shutters by applying a electronic motor.

In sum, the project was a small but successful beginner's project in IOT which may be expanded in different ways. Concluding, two pictures of the finished project are provided. Figure 7 shows the setup with opened shutters which prompted an e-mail and turned the LED red while Figure 8 shows the setup after closing the shutters which invoked the second e-mail and turned the LED green. Between both pictures, about 20 minutes passed.

![](https://i.imgur.com/GdIwtiX.jpg)
Figure 7: Finished setup with open shutters

![](https://i.imgur.com/RAG2N3E.jpg)
Figure 8: Finished setup after closing the shutters
