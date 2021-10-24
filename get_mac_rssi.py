# importing libraries
import time
import subprocess
import numpy
import math

# declaring an empty list to store average signal strength value at 10 different locations
Y = []
ssid = 'FasterThanSonic'  # ssid for which parameters are to be determined


# function to calculate average value of signal strength at a particular location by taking 20 readings of
# signal strength at that location
def average_rssi():
    avg = 0
    for num in range(20):
        subprocess.run(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=disabled'])
        subprocess.run(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=enabled'])
        time.sleep(4)

        # getting the result of command line command and storing it in a variable
        result = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"])

        # converting the result(datatype-bytes) first into string and then storing substrings in list y
        cmd_output_list = list((result.decode('ASCII')).split())

        i_SSID = [index for index, x in enumerate(cmd_output_list) if x == 'SSID']
        i_Network = [index for index, x in enumerate(cmd_output_list) if x == 'Network']
        i_Signal = [index for index, x in enumerate(cmd_output_list) if x == 'Signal']

        for m in range(len(i_SSID)):
            c = cmd_output_list[(i_SSID[m] + 3):i_Network[m]]
            c = tuple(c)
            s = " "
            if s.join(c) == ssid:
                a = cmd_output_list[i_Signal[m] + 2]
                a = a[0: len(a) - 1]
                dbm = ((int(a)) / 2) - 100
                avg += dbm
                break

        time.sleep(20)

    avg /= 20
    return avg


# getting the average value of signal strength at 10 different locations and storing it in the list Y
for i in range(10):
    rssi = average_rssi()
    Y.append(rssi)
    print(Y)
    time.sleep(5)

print(Y)
# converting list Y into a numpy array
