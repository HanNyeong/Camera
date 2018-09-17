import kivy
kivy.require('1.0.7')
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivymd.theming import ThemeManager
from kivymd.bottomsheet import MDGridBottomSheet
from kivymd.label import MDLabel
from kivymd.dialog import MDDialog
from kivymd.snackbar import Snackbar
from getPortList import getPortLIst


class Main(App):

    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    returnList = getPortLIst()
    port_list = []

    value = ""
    def build(self):
        pass
    for text in returnList.serial_ports():
        port_list.append({'viewclass':'MDMenuItem','text':text})

    def change_variable(self, value):
        self.value = value
        self.root.ids.portLabel.text = value



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
        bs.add_item("User List", lambda *x: self.userLIst(),
                    icon_src='./assets/list.png')
        bs.add_item("Face Record", lambda *x: self.faceRecord(),
                    icon_src='./assets/record.png')
        bs.add_item("Face Detection", lambda *x: self.faceDetect(),
                    icon_src='./assets/detection.png')
        bs.open()
    def userLIst(self):
        print('userLIst')

    def faceRecord(self):
        print('faceRecord')

    def faceDetect(self):
        print('faceDetect')

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
if __name__ == '__main__':
    Main().run()