from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
from kivymd.theming import ThemeManager
# from kivymd.navigationdrawer import NavigationDrawer
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.label import MDLabel
from kivymd.dialog import MDDialog
from kivymd.snackbar import Snackbar
from getPortList import getPortLIst
from kivy.uix.image import Image
from kivy.uix.camera import Camera

class Main(App):
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
        print()
        if(self.root.ids.scr_mngr.current == 'connection'):
            self.root.ids.scr_mngr.current = 'camera'
            self.root.ids.toolbar.title = 'Camera'
            self.root.ids.spinner.active = False
        elif(self.root.ids.scr_mngr.current == 'camera'):
            self.root.ids.scr_mngr.current = 'connection'
            self.root.ids.toolbar.title = 'Connection'

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
        bs = MDGridBottomSheet()
        bs.add_item("User List", lambda x: x,
                    icon_src='./assets/list.png')
        bs.add_item("Face Record", lambda x: x,
                    icon_src='./assets/record.png')
        bs.add_item("Face Detection", lambda x: x,
                    icon_src='./assets/detection.png')
        bs.open()

    def disconnect(self):
        print("disconnect")
        Snackbar(text="disconnect").show()
        self.change_screen()

    def showDialogToReset(self):
        print("reset data")
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="This is a dialog with a title and some text. "
                               "That's pretty awesome right!",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Are you sure?",
                               content=content,
                               size_hint=(.8, None),
                               auto_dismiss=False)
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.resetData())
        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def resetData(self):
        self.dialog.dismiss()
        print("reset")

Main().run()
