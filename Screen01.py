import asyncio
import json
import os
import threading

import webbrowser
from datetime import datetime

import kivy
import multitasking
import plyer
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.image import Texture
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty

from plyer import filechooser

from kivymd.app import MDApp

from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton, MDRoundFlatButton
from kivymd.uix.card import MDCard
from kivy.uix.widget import Widget
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineIconListItem

from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex
import time

from kivymd.uix.spinner import MDSpinner
from kivymd.uix.textfield import MDTextField

Window.size = 380, 580


class DEMO(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        pass


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color

                break
        instance_item.text_color = self.theme_cls.primary_color


class MD_relativelayout(MDRelativeLayout):
    def __init__(self, *arges, **kwargs):
        super(MD_relativelayout, self).__init__(**kwargs)
        self.id = StringProperty()
        pass


class Textbutton(MDTextField):
    def __init__(self, *arges, **kwargs):
        super(Textbutton, self).__init__(**kwargs)
        pass


class MDProBar(MDProgressBar):
    def __init__(self, *args, **kwargs):
        super(MDProBar, self).__init__(**kwargs)
        pass


class Content(MDBoxLayout):
    def __init__(self, *arges, **kwargs):
        super(Content, self).__init__(**kwargs)
        pass


class ItemDrawer(OneLineIconListItem):
    def __init__(self, *arges, **kwargs):
        super().__init__(**kwargs)
        pass


class SDsr(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super(SDsr, self).__init__()
        pass


class MD_relativelayout01(MDRelativeLayout):
    def __init__(self, *arges, text, source, text01, id):
        super(MD_relativelayout01, self).__init__()
        self.text = text
        self.source = source
        self.text01 = text01
        self.id = id
        self.angle= 120


class MD_relativelayout02(MDRelativeLayout):
    def __init__(self, *arges, text, source, text01, id):
        super(MD_relativelayout02, self).__init__()
        self.text = text
        self.source = source
        self.text01 = text01
        self.id = id


class App01(MDApp):
    def build(self):
        global screen_manager
        self.Counter = 0
        self.Counter2 = 0
        self.Counter0 = 0
        self.List_Iamge = []
        self.val_ = False
        self.A  =False

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"

        screen_manager = ScreenManager()

        screen_manager.add_widget(Builder.load_file('StartScreen.kv'))
        screen_manager.add_widget(Builder.load_file("ResultScreen.kv"))
        screen_manager.add_widget(Builder.load_file('mainscreen.kv'))
        screen_manager.add_widget(Builder.load_file('View_Resultscreen.kv'))
        screen_manager.add_widget(Builder.load_file('Save_Screen.kv'))
        screen_manager.add_widget(Builder.load_file('sharescreen.kv'))
        screen_manager.add_widget(Builder.load_file('animationscreen.kv'))
        screen_manager.add_widget(Builder.load_file('ContutScreen.kv'))
        screen_manager.add_widget(Builder.load_file('Camera_Screen.kv'))


        return screen_manager

    """def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }

        self.root.get_screen('mian_screen').ids['icon01'].icon = icons_item['folder']"""

    def get_image(self, name):
        if name == 'image1':
            self.root.get_screen('mian_screen').ids['Card'].source = 'image/1.jpg'
            self.root.get_screen('mian_screen').ids['Card'].text = 'image//01'
        if name == 'image2':
            self.root.get_screen('mian_screen').ids['Card2'].source = 'image/1.jpg'
            self.root.get_screen('mian_screen').ids['Card2'].text = 'image//02'
        if name == 'image3':
            self.root.get_screen('mian_screen').ids['Card3'].source = 'image/1.jpg'
            self.root.get_screen('mian_screen').ids['Card3'].text = 'image//03'
        if name == 'image4':
            self.root.get_screen('mian_screen').ids['Card4'].source = 'image/1.jpg'
            self.root.get_screen('mian_screen').ids['Card4'].text = 'image//04'
        if name == 'image5':
            self.root.get_screen('mian_screen').ids['Card5'].source = 'image/1.jpg'
            self.root.get_screen('mian_screen').ids['Card5'].text = 'image//05'

    def change_Iamge(self, name):
        self.name02 = name
        self.dialog = MDDialog(
            title=f'Choose \t {name} ',
            text="Try to enter Image Pleases!!!! ",
            radius=[20, 7, 20, 50],
            size_hint=(1, 1.4),
            type="alert",
            buttons=[MDRoundFlatButton(
                text="Camera", text_color=self.theme_cls.primary_dark, theme_text_color="Custom", pos=(0.2, 0.9),
                on_release=self.Camera),
                MDRoundFlatButton(
                    text="Add+", text_color=self.theme_cls.primary_dark, theme_text_color="Custom", pos=(0.2, 0.9),
                    on_release=self.Add_Image), ])
        self.dialog.open()

    def Add_Image(self, *args):
        self.Counter = self.Counter + 1
        self.selection01 = filechooser.open_file(o_selection=self.Selected)

        if self.name02 == 'image1':
            image01 = self.root.get_screen('mian_screen').ids['Card'].source = self.selection01[0]
            self.List_Iamge.append(image01)
        if self.name02 == 'image2':
            image02 = self.root.get_screen('mian_screen').ids['Card2'].source = self.selection01[0]
            self.Valu_Image01 =self.selection01[0]
        if self.name02 == 'image3':
            image03 = self.root.get_screen('mian_screen').ids['Card3'].source = self.selection01[0]
            self.List_Iamge.append(image03)
        if self.name02 == 'image4':
            image04 = self.root.get_screen('mian_screen').ids['Card4'].source = self.selection01[0]
            self.List_Iamge.append(image04)
        if self.name02 == 'image5':
            image05 = self.root.get_screen('mian_screen').ids['Card5'].source = self.selection01[0]
            self.List_Iamge.append(image05)
        self.dialog.dismiss()



    def Selected(self, selection):
        self.selection = selection

    def change_screenStart(self):
        self.animation_clock = Clock.schedule_interval(self.change_screen02, 2)

    def stop_clock(self, *args):
        self.animation_clock.cancel()

    def change_screen01(self, *args):
        widget = self.root.get_screen('animation_screen').ids['Image']
        widget1 = self.root.get_screen('animation_screen').ids['TEXT']
        screen_manager.current = 'animation_screen'
        self.change_screenStart()
        self.animation_widget(widget, widget1)

    def change_screen02(self, *args):
        screen_manager.current = 'mian_screen'
        Clock.schedule_once(self.stop_clock, 1)

    def animation_widget(self, widget, widget1, *args):
        animation = Animation(size_hint=(0.8, 0.8))
        animation.start(widget)
        animation = Animation(font_size=30)
        animation.start(widget1)

    def close_dialog(self, args):
        self.dialog.dismiss()

    def change_nav(self, stat):
        print(stat)

    def Exit(self):
        self.dialog = MDDialog(
            title='Warring',
            text="Are you sure to exit from App",
            radius=[50, 50, 50, 50],
            size_hint=(0.8, 1.4),
            type="alert",
            buttons=[MDRoundFlatButton(
                text="Conform", text_color=self.theme_cls.primary_color, theme_text_color="Custom", pos=(0.2, 0.9),
                on_release=App01().stop),
                MDRoundFlatButton(
                    text="Cancel", text_color=self.theme_cls.primary_color, theme_text_color="Custom", pos=(0.2, 0.9),
                    on_release=self.close_dialog)])
        self.dialog.open()

    def change_mode(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.root.get_screen('mian_screen').ids['icon01'].text_color = self.theme_cls.primary_dark
        else:
            self.theme_cls.theme_style = 'Light'

    def change_screen(self, name):
        screen_manager.current = name

    def Conform_Image(self):
        self.value = self.Counter + self.Counter2
        if self.value > 1:
            self.LaodSpinner()
            time.sleep(0.1)
            self.change_screen('Result_Screen')
            for i in self.List_Iamge :
                self.j=1
                self.root.get_screen('Result_Screen').ids[f'Image_Result0{self.j}'].source = i
                self.j=self.j+1
        else:

            self.dialog = MDDialog(
                title='Error',
                text=f"Image Selected is less then {self.value} ",
                radius=[50, 50, 50, 50],
                size_hint=(0.8, 1.4),
                type="alert",
                buttons=[MDRoundFlatButton(
                    text="Cancel", text_color=self.theme_cls.primary_dark, theme_text_color="Custom", pos=(0.2, 0.9),
                    on_release=self.close_dialog), ])
            self.dialog.open()


    def Entry_Image(self):
        self.MDspinner(True)
        from test import Calcul_Result


        self.Result_Image = Calcul_Result(self.List_Iamge)
        self._value1_ =self.Result_Image.finalresult()[0]
        self._value2_ =self.Result_Image.finalresult()[1]
        print(self.Result_Image.finalresult())
        self.Red_File(self._value1_ ,self._value2_)
        self.dialog02.dismiss()



    def Add_TextField(self):
        if self.Counter0 == 0:
            self.root.get_screen('Save_screen').ids['Card_Search'].add_widget(Textbutton(hint_text="bilal",
                                                                                         helper_text="Color is defined ", ))
            self.Counter0 = +1
            self.root.get_screen('Save_screen').ids['icon_search'].size_hint = (0, 0)

    def Start_screen(self, name):
        screen_manager.current = name

    def Save_Image(self, instance):
        self.Capteur_ecran()
        self.val_ = True
        for i in range(1):
            self.root.get_screen('Save_screen').ids['SaveCard'].add_widget(
                MD_relativelayout01(id='bilal0', text='result' + str(i), source='image/file.png',
                                    text01='2020-11-14 23:22:45'))
        time.sleep(1)
        screen_manager.current = "Save_screen"

    def Remove_MDCard(self):
        try:
            self.dialog = MDDialog(
                title='verification',
                text='Are you sure to delete it',
                radius=[50, 50, 50, 50],
                size_hint=(0.8, 1.4),
                type="alert",
                buttons=[MDRoundFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, theme_text_color="Custom", pos=(0.2, 0.9),
                    on_release=self.DeletImage),
                    MDRoundFlatButton(
                        text="NO", text_color=self.theme_cls.primary_color, theme_text_color="Custom", pos=(0.2, 0.9),
                        on_release=self.close_dialog), ])
            self.dialog.open()

        except:
            print('error')

    def DeletImage(self, *args):
        self.root.get_screen('Save_screen').ids['SaveCard'].remove_widget(
            self.root.get_screen('Save_screen').ids['SaveCard'].children[0])
        self.dialog.dismiss()

    def Delete_Image(self, *args):

        self.root.get_screen('View_Result_Screen').ids['BoxImage'].remove_widget(
            self.root.get_screen('View_Result_Screen').ids['IMAGE01'].children[0])

    def Verification(self, name):
        if self.val_ == True:
            screen_manager.current = name
        else:
            self.dialog = MDDialog(
                title='Error',
                text='There is no result recorded',
                radius=[50, 50, 50, 50],
                size_hint=(0.8, 1.4),
                type="alert",
                buttons=[MDRoundFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, theme_text_color="Primary", pos=(0.2, 0.9),
                    on_release=self.close_dialog), ])
            self.dialog.open()
        self.val_ = False

    def Camera(self, *args):
        self.capteur = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        screen_manager.current = 'Camera_Screen'
        self.dialog.dismiss()
        self.Update = Clock.schedule_interval(self.update, 1.0 / 33.0)

    def update(self, *args):

        # display image from cam in opencv window
        ret, frame = self.capteur.read()

        self.image_frame = frame
        # convert it to texture
        buf1 = cv2.flip(frame, 0).tostring()
        self.recsize = cv2.resize(frame, (350, 700))
        self.texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
        # if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer.
        self.texture1.blit_buffer(buf1, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.root.get_screen('Camera_Screen').ids['Image_Camera'].texture = self.texture1

    def take_picture(self, *args):
        self.Counter2 = self.Counter2 + 1
        data_time = datetime.now().microsecond
        name_picture = f"Picture{str(data_time)}Image1.jpg"
        file_save =os.path.dirname(__file__)+f'/Image_Picture/{name_picture}'

        cv2.imwrite(file_save, self.image_frame)
        if self.name02 == 'image1':
            image01 = self.root.get_screen('mian_screen').ids['Card'].source = f'.\Image_Picture\{name_picture}'
            self.List_Iamge.append(image01)
        if self.name02 == 'image2':
            image02 = self.root.get_screen('mian_screen').ids['Card2'].source = f'.\Image_Picture\{name_picture}'
            self.List_Iamge.append(image02)
        if self.name02 == 'image3':
            image03 = self.root.get_screen('mian_screen').ids['Card3'].source = f'.\Image_Picture\{name_picture}'
            self.List_Iamge.append(image03)
        if self.name02 == 'image4':
            image04 = self.root.get_screen('mian_screen').ids['Card4'].source = f'.\Image_Picture\{name_picture}'
            self.List_Iamge.append(image04)
        if self.name02 == 'image5':
            image05 = self.root.get_screen('mian_screen').ids['Card5'].source = f'.\Image_Picture\{name_picture}'
            self.List_Iamge.append(image05)
        self.Update.cancel()
        self.capteur.release()

        screen_manager.current = "mian_screen"

    def active_scroll(self, *args):
        self.root.get_screen('Result_Screen').ids["active_scroll"].do_scroll_y = True

    def Red_File(self, _value_, _value1_):
        file_name01 = os.path.dirname(__file__) + '/classes/data.json'
        with open(file_name01, 'r') as f:
            self.lines = f.read()
            self.lines_jsion =json.loads(self.lines)
        f.close()
        self.Name = self.lines_jsion[f'{_value_}'][0]['Name']
        self.VineImg =f"./classes/{self.lines_jsion[f'{_value_}'][0]['VineImg']}"
        self.Bottle1 = self.lines_jsion[f'{_value_}'][0]['Bottle1']
        self.Bottle2 = self.lines_jsion[f'{_value_}'][0]['Bottle2']
        self.info = f"classes/{self.lines_jsion[f'{_value_}'][0]['info']}"
        self.wiki =self.lines_jsion[f'{_value_}'][0]['wiki']
        file_name02 = os.path.dirname(__file__) +f"/{self.info}"
        with open(file_name02 ,'r') as L :
            self.info_read =L.readlines()
        L.close()
        self.Name2 = self.lines_jsion[f'{_value1_}'][0]['Name']
        self.VineImg2 = f"./classes/{self.lines_jsion[f'{_value1_}'][0]['VineImg']}"
        self.Bottle12 = self.lines_jsion[f'{_value1_}'][0]['Bottle1']
        self.Bottle22 = self.lines_jsion[f'{_value1_}'][0]['Bottle2']
        self.info2 = f"classes/{self.lines_jsion[f'{_value1_}'][0]['info']}"
        self.wiki2 = self.lines_jsion[f'{_value1_}'][0]['wiki']
        file_name022 = os.path.dirname(__file__) + f"/{self.info2}"
        with open(file_name022, 'r') as L2:
            self.info_read2 = L2.readlines()
        L2.close()
        self.Add_Tools()

    def Add_Tools(self):

        self.root.get_screen('Result_Screen').ids['Image_Result04'].source = str(self.VineImg)
        self.root.get_screen('Result_Screen').ids['Image_Result05'].source = str(self.VineImg2)
        self.root.get_screen('Result_Screen').ids['Result_text01'].text = f'{str(self.info_read[0])}'
        self.root.get_screen('Result_Screen').ids['Result_text02'].text = f'{str(self.info_read2[0])}'
        self.root.get_screen('Result_Screen').ids['Result_Name01'].text = f'{self.Name}'
        self.root.get_screen('Result_Screen').ids['Result_Name02'].text = f'{self.Name2}'

    def Open_WebSite(self, Name_Button):
        if Name_Button=='1' :
            webbrowser.open(self.wiki)
        else :
            webbrowser.open(self.wiki2)

    def LaodSpinner(self):

        self.thread_ =threading.Thread(target =self.Entry_Image)
        if self.thread_.start() :
            self.change_screen('Result_Screen')
            self.thread_.join()
    def MDspinner(self,*args):
        self.dialog02 = MDDialog(
            size_hint=(1, 1),
            height = '120dp',
            type="custom",
            md_bg_color = self.theme_cls.primary_dark,
            content_cls = SDsr())
        self.dialog02.open()

    def Capteur_ecran(self):
        import pyscreenshot
        self.PathSave = os.path.dirname(__file__)+'/Save_resukt'
        image = pyscreenshot.grab(bbox=(200, 30, 500, 500))
        data_time = datetime.now().microsecond
        image.save(f"{self.PathSave}/Result{str(data_time)}.png")


if __name__ == '__main__':
    LabelBase.register(name='MPoppins', fn_regular="poppins\Poppins""-Medium.ttf")
    LabelBase.register(name='Lobster', fn_regular="Lobster\Lobster"
                                                  "-Regular.ttf")
    LabelBase.register(name='RussoOne', fn_regular="font\RussoOne"
                                                   "-Regular.ttf")
    App01().run()
