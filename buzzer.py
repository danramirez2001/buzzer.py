from bt_proximity import BluetoothRSSI
from gpiozero import LED
from time import sleep
import time
import sys

BT_ADDR = ''            # You can put your Bluetooth address here 
THRESHOLD = -15         # Threshold value under which the device will send a warning
BIN_SIZE = 10           # Number of measurements in running average
TIME_DELAY = 1          # Time between measurements in seconds
rssiList = []
led = LED(4)            # GPIO pin number corresponding to output device
led.off()





def main():
    if BT_ADDR:
        addr = BT_ADDR
    else:
        print('No Bluetooth Address Found')         # Check whether address can be found 
        return
    btrssi = BluetoothRSSI(addr=addr)
    for i in range(0,BIN_SIZE):                     # Populate initial list up to BIN_SIZE
        rssi = btrssi.get_rssi()
        rssiList.append(rssi)
    while(True):                                    # Performs continual updates at an interval of TIME_DELAY 
        led.off()                                   # Reset output device
        rssi = btrssi.get_rssi()                    # Get current RSSI
        rssiList.insert(0,rssi)                     # Add RSSI to list
        del rssiList[-1]                            # Pop last element off list
        if(getAverage(rssiList) < THRESHOLD):       # Check if running average is beneath THRESHOLD - if yes, turn on output
            led.on()
	    print('ALARM')
        time.sleep(1)

def getAverage(list):                               # Return average of current list of RSSI values
    sum = 0
    for i in range (0,len(list)):
        sum += list[i]
    average = sum / len(list)
    return average


main()



