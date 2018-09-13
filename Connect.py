from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemeManager
# from kivymd.navigationdrawer import NavigationDrawer
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.label import Label
from kivymd.snackbar import Snackbar
from kivy.clock import Clock
from getPortList import getPortLIst

class Connect(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    returnList = getPortLIst()
    port_list = []

    value = ""

    for text in returnList.serial_ports():
        port_list.append({'viewclass':'MDMenuItem','text':text})

    def change_variable(self, value):
        self.value = value
        self.root.ids.portLabel.text = value

    def build(self):
        pass

    def change_screen(self):
        self.root.ids.scr_mngr.current = 'camera'
        self.root.ids.toolbar.title = 'Camera'
        self.root.ids.spinner.active = False

    def serialConnect(self):
        self.root.ids.spinner.active = True
        Snackbar(text="connecting...").show()
        checkConnection = True
        # connection = serialConnect
        if(checkConnection):
            Snackbar(text="connect success").show()
            Clock.schedule_once(lambda dt: self.change_screen(), 3)
        else:
            Snackbar(text="connect fail").show()
            self.root.ids.spinner.active = False

    def bottom_camera_list(self):
        bs = MDListBottomSheet()
        bs.add_item("User LIst", lambda x: x)
        bs.add_item("Face Regist", lambda x: x)
        bs.add_item("Face Record", lambda x: x)
        bs.open()

Connect().run()
