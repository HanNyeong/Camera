import serial
import time


ser = serial.Serial('COM21', 115200, timeout = 1) # ttyACM1 for Arduino board
readOut = 0   #chars waiting from laser range finder
print ("Starting up")
connected = False
def task():
    print("Attempt to Read")
    readOut = ser.readline().decode('ascii')
    print("Reading: ", readOut)
    print("Restart")
    ser.flush()  # flush the buffer
    if len(str(readOut)) == 0:
        return False
    return True

def login():
    commandToSend = 'V+LOGIN9876'  # get the distance in mm
    print("Writing: ", commandToSend)
    ser.write(str(commandToSend).encode())
    task()

def user():
    commandToSend = 'V+UFUSER' # get the distance in mm
    print("Writing: ", commandToSend)
    ser.write(str(commandToSend).encode())

    while True:
        if not task():
            break







