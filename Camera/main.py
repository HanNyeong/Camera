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
from kivy.core.window import Window
main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem

<MDMenuItem>:
    on_release: app.change_variable(self.text)
BoxLayout:
    orientation: 'vertical'
    Toolbar:
        id: toolbar
        title: 'Connect'
        md_bg_color: app.theme_cls.primary_color
        background_palette: 'Primary'
        background_hue: '500'
    ScreenManager:
        id: scr_mngr
        Screen:
            name: 'connection'
            MDLabel:
                font_style: 'Subhead'
                theme_text_color: 'Primary'
                text: "Port : "
                size_hint_x:None
                pos_hint: {'center_x': 0.4, 'center_y': 0.7}
                height: self.texture_size[1] + dp(4)
            MDLabel:
                id:portLabel
                font_style: 'Subhead'
                theme_text_color: 'Primary'
                text: ""
                size_hint_x:None
                pos_hint: {'center_x': 0.63, 'center_y': 0.7}
                height: self.texture_size[1] + dp(4)
            MDIconButton:
                icon:'arrow-down-drop-circle'
                size_hint: None, None
                pos_hint: {'center_x': 0.67, 'center_y': 0.7}
                on_release: MDDropdownMenu(items=app.port_list, width_mult=4).open(self)
            MDLabel:
                font_style: 'Subhead'
                theme_text_color: 'Primary'
                text: "Baud : "
                size_hint_x:None
                pos_hint: {'center_x': 0.4, 'center_y': 0.6}
            MDLabel:
                id:baudLabel
                font_style: 'Subhead'
                theme_text_color: 'Primary'
                text: "115200 "
                size_hint_x:None
                pos_hint: {'center_x': 0.63, 'center_y': 0.6}
            MDLabel:
                font_style: 'Subhead'
                theme_text_color: 'Primary'
                text: "Password : "
                size_hint_x:None
                pos_hint: {'center_x': 0.4, 'center_y': 0.5}
            MDLabel:
                font_style: 'Subhead'
                theme_text_color: 'Primary'
                text: "9876"
                size_hint_x:None
                pos_hint: {'center_x': 0.63, 'center_y': 0.5}
            #M#D#L#a#b#e#l#:#
    # # # # # # # # # # # # #f#o#n#t#_#s#t#y#l#e#:# #'#S#u#b#h#e#a#d#'#
    # # # # # # # # # # # # #t#h#e#m#e#_#t#e#x#t#_#c#o#l#o#r#:# #'#P#r#i#m#a#r#y#'#
    # # # # # # # # # # # # #t#e#x#t#:# #"#s#e#c#y#K#e#y# #:# #"#
    # # # # # # # # # # # # #s#i#z#e#_#h#i#n#t#_#x#:#N#o#n#e#
    # # # # # # # # # # # # #p#o#s#_#h#i#n#t#:# #{#'#c#e#n#t#e#r#_#x#'#:# #0#.#4#,# #'#c#e#n#t#e#r#_#y#'#:# #0#.#5#}#
    # # # # # # # # #M#D#L#a#b#e#l#:#
    # # # # # # # # # # # # #f#o#n#t#_#s#t#y#l#e#:# #'#S#u#b#h#e#a#d#'#
    # # # # # # # # # # # # #t#h#e#m#e#_#t#e#x#t#_#c#o#l#o#r#:# #'#P#r#i#m#a#r#y#'#
    # # # # # # # # # # # # #t#e#x#t#:# #"#1#2#3#4#5#6#7#8#9#0#1#2#3#4#5#6#7#8#9#0#1#2#3#4#5#6#7#8#9#0#1#2#"#
    # # # # # # # # # # # # #s#i#z#e#_#h#i#n#t#_#x#:#N#o#n#e#
    # # # # # # # # # # # # #p#o#s#_#h#i#n#t#:# #{#'#c#e#n#t#e#r#_#x#'#:# #0#.#6#3#,# #'#c#e#n#t#e#r#_#y#'#:# #0#.#5#}#
    # # # # # # # # # # # # #s#i#z#e#:# #(#3#0#0#,# #5#0#)
            MDRaisedButton:
                text: "Connect"
                opposite_colors: True
                size_hint: None, None
                size: dp(70), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                on_release: app.serialConnect()
            MDSpinner:
                id: spinner
                size_hint: None, None
                size: dp(46), dp(46)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                active: False
        Screen:
			name: 'camera'
			MDBottomNavigation:
                id: bottom_navigation_demo
                valign: 'center'
                MDBottomNavigationItem:
                    name: 'cameraDetail'
                    text: "Camera"
                    icon: "camera"
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        padding: dp(48)
                        spacing: 10
                        spacing: 10
                        MDRaisedButton:
                            text: "Option"
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.bottom_camera_list()
                MDBottomNavigationItem:
                    name: 'setting'
                    text: "Setting"
                    icon: 'file'
                    BoxLayout:
                        orientation: 'vertical'
                        padding: dp(48)
                        spacing: 10
                        MDList:
                            id: ml
                            pos_hint: {'center_x': 0.5, 'center_y': 0.9}
                            OneLineListItem:
                                text: "Disconnect"
                                on_release:app.disconnect()
                            TwoLineListItem:
                                text: "Reset Database"
                                on_release:app.showDialogToReset()
'''

Window.size = (600, 400)
class Main(App):

    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    returnList = getPortLIst()
    port_list = []

    value = ""
    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        # self.theme_cls.theme_style = 'Dark'
        return main_widget
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