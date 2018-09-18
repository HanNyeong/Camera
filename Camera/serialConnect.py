import serial
import datetime
class Serial:

    def __init__(self,port):
        self.ser = serial.Serial(port, 115200, timeout=1)  # ttyACM1 for Arduino board
        self.readOut = 0  # chars waiting from laser range finder
        print("Starting up")
        self.connected = False

    def writing(self,command):
        print("Writing: ", command)
        self.ser.write(str(command).encode())

    def task(self):
        print("Attempt to Read")
        readOut = self.ser.readline().decode('ascii')
        print("Reading: ", readOut)
        print("Restart")
        self.ser.flush()  # flush the buffer
        if len(str(readOut)) == 0:
            return False
        return True


    def login(self):
        self.writing('V+LOGIN9876')
        self.task()


    def userList(self):
        self.writing('V+UFUSER')
        while True:
            if not self.task():
                break


    def faceRecord(self):
        self.writing('V+UFREC')
        self.task()


    def faceDetect(self):
        self.writing('V+UFFD ')
        self.task()

    def faceRegistration(self):
        self.date = datetime.datetime.now()
        faceId = str(self.date.year)+str(self.date.month)+str(self.date.day)+str(self.date.hour)+str(self.date.minute)+str(self.date.second)
        print(faceId)
        self.writing('V+UFREG'+faceId)
        while True:
            if not self.task():
                break

