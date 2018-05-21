from bt_proximity import BluetoothRSSI
from gpiozero import LED
from time import sleep
import time
import sys

BT_ADDR = ''  # You can put your Bluetooth address here 
rssiList = []
led = LED(4) # Choose the correct pin number
led.off()


def print_usage():
    print "Usage: python test_address.py <bluetooth-address> [number-of-requests]"


def main():
    if BT_ADDR:
        addr = BT_ADDR
    else:
        print('No Bluetooth Address Found')
        print_usage()
        return
    btrssi = BluetoothRSSI(addr=addr)
    print('Starting count')
    for i in range(0,10):
        rssi = btrssi.get_rssi()
        rssiList.append(rssi)
    print('Done count')
    while(True):
        led.off()
	print('OFF')
        rssi = btrssi.get_rssi()
	print(rssi)
        rssiList.insert(0,rssi)
        del rssiList[-1]
	print(rssiList)
        if(getAverage(rssiList) < -15):
            led.on()
	    print('ALARM')
        time.sleep(1)

def getAverage(list):
    sum = 0
    for i in range (0,len(list)):
        sum += list[i]
    average = sum / len(list)
    return average


main()



