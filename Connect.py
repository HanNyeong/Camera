import sys
import glob
import serial
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemeManager
# from kivymd.navigationdrawer import NavigationDrawer
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.label import Label

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

class Connect(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    port_list = []
    for text in serial_ports():
        port_list.append({'viewclass':'MDMenuItem','text':text})

    def change_variable(self, value):
        self.root.ids.portLabel.text = value

    def build(self):
        pass

    def serialConnect(self):
        self.root.ids.spinner.active = True
        checkConnection = True
        # connection = serialConnect
        if(checkConnection):
            self.root.ids.scr_mngr.current = 'camera'
            self.root.ids.toolbar.title = 'Camera'
            self.root.ids.spinner.active = False

    def show_example_bottom_sheet(self):
        bs = MDListBottomSheet()
        bs.add_item("User LIst", lambda x: x)
        bs.add_item("Face Regist", lambda x: x)
        bs.add_item("Face Record", lambda x: x)
        bs.open()

Connect().run()
