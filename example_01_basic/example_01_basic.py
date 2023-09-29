# %% 
# This script is an example of a simple connection to the ReWire pulse oximeter
# and reading data over serial communication.

# %% Imports

import serial
import serial.tools
import serial.tools.list_ports

# %% 

#Define some values that are the ReWire pulse oximeter's VID and PID
rewire_pulseox_vid = 0x04D8
rewire_pulseox_pid = 0xE636

#Get a list of all available serial ports
serial_ports = serial.tools.list_ports.comports()

#Find the first serial port that matches the ReWire pulse oximeter
selected_port = None
for current_port in serial_ports:
    if (current_port.vid == rewire_pulseox_vid) and (current_port.pid == rewire_pulseox_pid):
        selected_port = current_port
        break

#If we found a device...
if (selected_port is not None):

    #Connect to the serial port
    serial_port = serial.Serial(port=selected_port.name, baudrate=115200, timeout=1)

    #Loop forever
    while(True):

        if (serial_port.in_waiting > 0):

            current_line_bytes = serial_port.readline()
            if (len(current_line_bytes) > 0):
                current_line = current_line_bytes.decode("utf-8").strip()
                print(current_line)

