import asyncio
import json
import os
import threading

import webbrowser
from datetime import datetime

import geocoder
import kivy
import multitasking
import mysql
import plyer
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.image import Texture
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty, ReferenceListProperty, DictProperty

from plyer import filechooser

from kivymd.app import MDApp

from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import cv2
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton, MDRoundFlatButton, MDIconButton, MDRoundFlatIconButton
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

from kivymd.uix.snackbar import Snackbar
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.textfield import MDTextField

Window.size = 380, 580


class DEMO(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        pass
class DEMO01(MDScreen):
    velocity_x = NumericProperty(30.0)
    velocity_y = NumericProperty(7)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    pos_x = 30.0
    List_pos = [318.8928858751868, 259.6687162395127, 200.44454660383866, 141.2203769681646, 81.99620733249053]
    List_Id = []
    bilal = False

    def on_touch_move(self, touch, afther=False):

        self.Touch = touch.pos[1]
        try :
            if afther == 'box01':
                self.widget = self.ids.box01
                print('1')
            if afther == 'box02':
                self.widget = self.ids.box02
                print('2')
            if afther == 'box03':
                self.widget = self.ids.box03
                print('3')
            if afther == 'box04':
                self.widget = self.ids.box04
                print('4')
            if afther == 'box05':
                self.widget = self.ids.box05
                print('5')
            if self.widget:
                self.move(self.widget, self.List_Id)
                return
            else:
                return super(DEMO01, self).on_touch_down(touch)
        except :
            pass
    def move(self, widget, List):
        self.val = widget
        if self.val == self.ids.box01:
            self.animation = Clock.schedule_interval(self.updata, 1 / 60)
        if self.val == self.ids.box02:
            self.animation = Clock.schedule_interval(self.updata, 1 / 60)
        if self.val == self.ids.box03:
            self.animation = Clock.schedule_interval(self.updata, 1 / 60)
        if self.val == self.ids.box04:
            self.animation = Clock.schedule_interval(self.updata, 1 / 60)
        if self.val == self.ids.box05:
            self.animation = Clock.schedule_interval(self.updata, 1 / 60)

    def updata(self, arg):
        self.val.pos[1] = self.Touch

        if self.val.pos[1] > 318.8928858751868:
            self.BILAL()
            self.animation.cancel()
        if self.val.pos[1] < 81.99620733249053:
            self.val.pos[1] = self.Touch
            self.val.pos[1] = 81.99620733249053
            self.animation.cancel()

    def BILAL(self):
        if 318 < self.Touch > 371:
            self.val.pos[1] = 318.8928858751868
        if 259 < self.Touch > 305:
            self.val.pos[1] = 318.8928858751868
class MDNSearch(MDBoxLayout) :
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
        pass


class TextField(MDBoxLayout) :
    def __init__(self,*args ,id ):
        super(TextField, self).__init__()
        self.id =id


    def get_Data_Whatsapp(self, *args):
         self.User = self.ids['Text_User'].text
         self.Massege = self.ids['Text_Password'].text
         self.N_Phone = str(self.User)

         try :
            from ClassWhatsapp import Whatsapp
            self.Whatsapp =Whatsapp(self.N_Phone ,'bilal',self.Massege ).Send_Message()

         except :

             Snackbar(
                 text="verify connexion or Phone ",
                 snackbar_x="10dp",
                 snackbar_y="10dp",
                 size_hint_x=(Window.width - (dp(10) * 2)
                             ) / Window.width
             ).open()

class Textbutton(MDTextField):
    def __init__(self, *args ,id,**kawrgs ):
        super(Textbutton, self).__init__(**kawrgs)
        self.id = id
        print(self.id)


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
class MD_relativelayout05(MDRelativeLayout) :
    text = StringProperty()
    source  =StringProperty()
    comment= StringProperty()
    text01 = StringProperty()
    button = StringProperty()
    location = StringProperty()
    dataHure = StringProperty()
    commentResult = StringProperty()
    ids = DictProperty()
    result01 =StringProperty()
    result02= StringProperty()
    result03 = StringProperty()
    result04 =StringProperty()
    result05 =StringProperty()
class ButtonMD(MDRoundFlatIconButton) :
    name01 = StringProperty()
class App01(MDApp):
    def build(self):
        global screen_manager
        self.Save_Path = []
        self.Save_Path01 = []
        self.Counter = 0
        self.Counter0 = 0
        self.file = 0
        self.scrollview = 0
        self.List_Iamge = []


        self.image01 =None
        self.val_ = False
        self.A  =False
        self.ver = False
        self.data0 = 0

        self.Card = MD_relativelayout05()

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.specific_text_color ='white'
        self.theme_cls.color = 'green'

        screen_manager = ScreenManager(transition=FadeTransition())
        screen_manager.add_widget(Builder.load_file('StartScreen.kv'))
        screen_manager.add_widget(Builder.load_file('Save_Screen.kv'))
        screen_manager.add_widget(Builder.load_file('Saveresultprocessing.kv'))


        screen_manager.add_widget(Builder.load_file('View_ResultScreen.kv'))

        screen_manager.add_widget(Builder.load_file('animationscreen.kv'))
        screen_manager.add_widget(Builder.load_file('mainscreen01.kv'))
        screen_manager.add_widget(Builder.load_file('sharescreen.kv'))
        screen_manager.add_widget(Builder.load_file('ViewResultPereProcessing.kv'))
        screen_manager.add_widget(Builder.load_file('ContutScreen.kv'))
        screen_manager.add_widget(Builder.load_file('Camera_Screen.kv'))
        screen_manager.add_widget(Builder.load_file("RuseltScreen01.kv"))

        return screen_manager


    def on_start(self,*args):
        try :
            data_time = datetime.now()
            Clock.schedule_interval(self.get_time_heur , 1)
            self.data = data_time.date()
            ip = geocoder.ip('me')
            self.lacation = ip.geojson['features'][0]['properties']['address'].split(',')

        except :
            self.dialog = MDDialog(
                title= 'Worrning',
                text="Non connection !!!! ",
                type="custom",
                buttons=[
                    MDRoundFlatButton(
                        text="Ok", text_color=self.theme_cls.primary_dark, theme_text_color="Custom", pos=(0.2, 0.9),
                        on_release=self.close_dialog), ])
            self.dialog.open()
        self.get_value_Mysql()
    def get_time_heur(self ,dt):
        data_time = datetime.now()
        self.root.get_screen('mian_screen').ids['Main_Address'].text = str(
            f'{self.data}    {data_time.time().hour}:{data_time.time().minute}:{data_time.time().second} '
            f'\n {self.lacation[0]}-{self.lacation[1]}-{self.lacation[2]}')
    def get_value_Mysql(self):

        import mysql.connector
        self.mydb = mysql.connector.connect(
            host='Localhost',
            user='root',
            password='',
            database='kivy'
        )
        sql_select_Query = "select * from save_imageprocessing"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(sql_select_Query)
        records = self.mycursor.fetchall()

        for row in records:

            self.Card = MD_relativelayout05()
            self.Card.text = row[1]
            self.Card.source = row[0]
            self.Card.text01 = row[2]
            self.Card.comment = row[3]
            self.Card.button = 'View_Result_ScreenProcessing'
            self.root.get_screen('Save_screenProcessing').ids['SaveCardProcessing'].add_widget(self.Card)
            self.Card.ids = {'Image' : self.Card.text}

        sql_select_Query01 = "select * from save_image"
        self.mycursor01 = self.mydb.cursor()
        self.mycursor01.execute(sql_select_Query01)
        records01 = self.mycursor01.fetchall()

        for row01 in records01:
            self.Card = MD_relativelayout05()
            self.Card.source = row01[0]
            self.Card.text = row01[1]
            self.Card.text01 = row01[2]
            self.Card.dataHure = row01[3]
            self.Card.location = row01[4]
            self.Card.commentResult = row01[5]
            self.Card.result01 =row01[6]
            self.Card.result02 = row01[7]
            self.Card.result03 = row01[8]
            self.Card.result04 = row01[9]
            self.Card.result05 = row01[10]
            self.Card.button = 'View_Result_Screen'

            self.root.get_screen('Save_screen').ids['SaveCard'].add_widget(self.Card)
        self.mydb.commit()
        self.mydb.close()



    def change_Iamge(self, name):
        self.name02 = name
        self.dialog = MDDialog(
            title=f'Choose \t {name} ',
            text="Try to enter Image Pleases!!!! ",
            type="custom",
            buttons=[MDRoundFlatButton(
                text="Camera", text_color=self.theme_cls.primary_dark, theme_text_color="Custom", pos=(0.2, 0.9),
                on_release=self.Camera),
                MDRoundFlatButton(
                    text="Add+", text_color=self.theme_cls.primary_dark, theme_text_color="Custom", pos=(0.2, 0.9),
                    on_release=self.Add_Image), ])
        self.dialog.open()
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
        self.Stat = stat
        print(stat)


    def Exit(self):
        self.dialog = MDDialog(
            title='Warring',
            text="Are you sure to exit from App",
            type="custom",
            buttons=[MDRoundFlatButton(
                text="Conform", text_color=self.theme_cls.primary_color, theme_text_color="Custom", pos=(0.2, 0.9),
                on_release=App01().stop),
                MDRoundFlatButton(
                    text="Cancel", text_color=self.theme_cls.primary_color, theme_text_color="Custom", pos=(0.2, 0.9),
                    on_release=self.close_dialog)])
        self.dialog.open()

    def change_mode(self,instance_item):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.color = 'green'
        else:
            self.theme_cls.theme_style = 'Light'
            self.theme_cls.color = 'green'

    def change_screen(self, name):
        print(name)
        self.Counter = 0
        screen_manager.current = name
        self.Remove_Data()
    def Conform_Image(self):
        self.value = self.Counter
        if  self.root.get_screen('mian_screen').ids['Card01'].source !='Image/leaf.png':
            if self.image01 == None:
                self.image01 = self.root.get_screen('mian_screen').ids['Card01'].source
            else:
                self.image01 = self.image01
            self.LaodSpinner()
            time.sleep(0.1)
            screen_manager.current='Result_Screen'
        else:
            self.dialog = MDDialog(
                title='Error',
                text="Image Selected is less then  ",
                type="custom",
                buttons=[MDRoundFlatButton(
                    text="Cancel", text_color=self.theme_cls.primary_dark, theme_text_color="Custom", pos=(0.2, 0.9),
                    on_release=self.close_dialog), ])
            self.dialog.open()


    def Entry_Image(self):

        self.List_Iamge.append(self.image01)
        self.value =0
        self.MDspinner(True)
        from test import Calcul_Result
        self.Result_Image = Calcul_Result(self.List_Iamge)
        Function = self.Result_Image.finalresult()
        self._value1_ =self.Result_Image.result01()
        self._value2_ = self.Result_Image.result02()
        self.set_percentage(self._value1_ )
        self.get_data_location()
        self.dialog02.dismiss()
        self.List_Iamge.clear()
        self.image01 = None
    def set_percentage(self , _value_):
        self.i = 0
        for i in _value_ :
            self.get_data_json(self._value2_)
            self.i = self.i+1
            self.root.get_screen('Result_Screen').ids[f'Text_Label{self.i}'].text = str(f'{self.Name}:        {i}%')
    def get_data_json(self, _jsonId_):
        file_name01 = os.path.dirname(__file__) + '/classes/data.json'
        with open(file_name01, 'r') as f:
            self.lines = f.read()
            self.lines_jsion = json.loads(self.lines)
        f.close()
        self.Name = self.lines_jsion[f'{_jsonId_[self.i]}'][0]['Name']
    def get_data_location(self):
        self.Comment =  self.root.get_screen('mian_screen').ids['Input_Comment'].text
        data_time = datetime.now()
        self.data  =data_time.date()
        ip = geocoder.ip('me')
        self.lacation =ip.geojson['features'][0]['properties']['address'].split(',')
        self.root.get_screen('Result_Screen').ids['Text_data'].text = str(self.data)
        self.root.get_screen('Result_Screen').ids['Text_Location'].text = str(f'{self.lacation[0]}-{self.lacation[1]}-{self.lacation[2]}')
        self.root.get_screen('Result_Screen').ids['Image_Processing'].source = self.image01
        if self.Comment =='' :
            self.root.get_screen('Result_Screen').ids['Text_Comment'].text = str('No Comment')
        else :
            self.root.get_screen('Result_Screen').ids['Text_Comment'].text = str(self.Comment)

    def LaodSpinner(self):

        self.thread_ =threading.Thread(target =self.Entry_Image)
        self.thread_.start()


    def Start_screen(self, name):
        self.value= 0
        screen_manager.current = name


    def change_screen_Data(self , Adress ,Image ,Location , Data ,CommentResult ,Result01 , Result02 ,Result03 , Result04 ,Result05):
        screen_manager.current = Adress
        self.root.get_screen('View_Result_Screen').ids['Image_Processing'].source=Image
        self.root.get_screen('View_Result_Screen').ids['Text_Location'].text =Location
        self.root.get_screen('View_Result_Screen').ids['Text_data'].text = Data
        self.root.get_screen('View_Result_Screen').ids['Text_Comment'].text =CommentResult
        self.root.get_screen('View_Result_Screen').ids['Text_Label1'].text = Result01
        self.root.get_screen('View_Result_Screen').ids['Text_Label2'].text = Result02
        self.root.get_screen('View_Result_Screen').ids['Text_Label3'].text =Result03
        self.root.get_screen('View_Result_Screen').ids['Text_Label4'].text=Result04
        self.root.get_screen('View_Result_Screen').ids['Text_Label5'].text=Result05



    def Save_Image(self,name,comment , imageProcessing):
        self.data0 = int(self.data0) + 1
        self.file =self.file+1
        self.val_ = True
        import mysql.connector
        self.mydb = mysql.connector.connect(host='Localhost', user='root', password='', database='kivy')
        sql_select_Query01 = "select * from save_imageprocessing"
        self.mycursor01 = self.mydb.cursor()
        self.mycursor01.execute(sql_select_Query01)
        records01 = self.mycursor01.fetchall()
        try:
            for r in records01:
                self.id01 = r[5]
            self.id =int(self.id01) +1
        except:
            self.id = 0


        self.Card = MD_relativelayout05()
        self.Card.text = f'Image0{self.id}'
        self.Card.source =imageProcessing
        self.Card.text01 = str(datetime.now())
        self.Card.button = 'View_Result_ScreenProcessing'
        self.Card.comment = str(comment)
        self.Card.ids = {'Image': self.Card.text}
        self.root.get_screen('Save_screenProcessing').ids['SaveCardProcessing'].add_widget(self.Card)
        screen_manager.current = name
        self.Set_Value_Excel(self.Card.source , self.Card.text , self.Card.text01 ,self.Card.comment  ,str(self.Card.ids) ,str(self.id))
    def Set_Value_Excel(self,source , textCard1  ,textCard2 , comment ,ids , id):
        import mysql.connector
        self.mydb = mysql.connector.connect(
            host='Localhost',
            user='root',
            password='',
            database='kivy'
        )
        self.mycursor = self.mydb.cursor()
        self.values00 = (source ,textCard1 , textCard2 ,comment , ids ,id)
        self.mycursor.execute("insert into save_imageprocessing values(%s,%s,%s,%s,%s,%s)",self.values00)
        self.mydb.commit()
        self.mydb.close()


    def Remove_MDCard(self ,name):

        try:
            self.dialog01 = MDDialog(
                title='verification',
                text='Are you sure to delete it',
                type="custom",
                buttons=[MDRoundFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, theme_text_color="Custom", pos=(0.2, 0.9),
                    on_release=self.DeletImage),
                    MDRoundFlatButton(
                        text="NO", text_color=self.theme_cls.primary_color, theme_text_color="Custom", pos=(0.2, 0.9),
                        on_release=self.Close_dialog), ])
            self.dialog01.open()

        except:
            print('error')
    def Close_dialog(self ,*args):
        self.dialog01.dismiss()
    def DeletImage(self, *args):

        try :
            import mysql.connector
            self.mydb = mysql.connector.connect(host='Localhost', user='root', password='', database='kivy')
            sql_select_Query = "select * from save_image"
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute(sql_select_Query)
            records = self.mycursor.fetchall()

            for r in records:
                print(self.ids, 'bilal.image',r[1])
                if self.ids == r[1]:
                    print('def image')
                    self.mycursor.execute(f"DELETE FROM save_image WHERE text='{self.ids}';")
                try :
                    self.root.get_screen('Save_screen').ids['SaveCard'].remove_widget(
                        self.root.get_screen('Save_screen').ids['SaveCard'].children[0])
                except :
                    pass

            sql_select_Query01 = "select * from save_imageprocessing"
            self.mycursor01 = self.mydb.cursor()
            self.mycursor01.execute(sql_select_Query01)
            records01 = self.mycursor01.fetchall()
            for r01 in records01 :
                if self.ids ==r01[1] :
                    print('def result')
                    self.mycursor.execute(f"DELETE FROM save_imageprocessing WHERE textCard ='{self.ids}';")
                try:
                    self.root.get_screen('Save_screenProcessing').ids['SaveCardProcessing'].remove_widget(
                        self.root.get_screen('Save_screenProcessing').ids['SaveCardProcessing'].children[0])
                except:
                    pass
            self.mydb.commit()
            self.mydb.close()
            time.sleep(1)
            self.get_value_Mysql()

            self.dialog01.dismiss()



        except :
            pass
    def Remove_MDCardProcessing(self  , ids):
        self.ids = ids
        print(self.ids)
        try:
            self.dialogPro = MDDialog(
                title='verification Image',
                text='Are you sure to delete it',
                type="custom",
                buttons=[MDRoundFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, theme_text_color="Custom", pos=(0.2, 0.9),
                    on_release=self.Delete_ImageProcessing),
                    MDRoundFlatButton(
                        text="NO", text_color=self.theme_cls.primary_color, theme_text_color="Custom", pos=(0.2, 0.9),
                        on_release=self.close_dialogPro), ])
            self.dialogPro.open()

        except:
            pass
    def close_dialogPro(self ,*args):
        self.dialogPro.dismiss()
    def Delete_ImageProcessing(self,*args):
        print('fe')
        try :
            import mysql.connector
            self.mydb = mysql.connector.connect(host='Localhost', user='root', password='', database='kivy')
            sql_select_Query = "select * from save_imageprocessing"
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute(sql_select_Query)
            records = self.mycursor.fetchall()
            for r in records :
                if self.ids ==r[1] :
                    #self.mycursor.execute(f"DELETE FROM save_imageprocessing WHERE textCard ='{self.ids}';")
                    try:
                        self.root.get_screen('Save_screenProcessing').ids['SaveCardProcessing'].remove_widget(
                            self.root.get_screen('Save_screenProcessing').ids['SaveCardProcessing'].children[0])
                    except:
                        pass
            self.mydb.commit()
            self.mydb.close()

            time.sleep(1)
            self.dialogPro.dismiss()
        except :
            pass
    def Verification(self, name):
        self.value = 0
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

    def Camera(self, name02):
        self.name02 = name02
        self.capteur = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        screen_manager.current = 'Camera_Screen'
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
        self.Counter = self.Counter+1
        data_time = datetime.now().microsecond
        name_picture = f"Picture{str(data_time)}Image1.jpg"
        file_save =os.path.dirname(__file__)+f'/Image_Picture/{name_picture}'
        cv2.imwrite(file_save, self.image_frame)
        if self.name02 == 'image1':
            self.image01 = self.root.get_screen('mian_screen').ids['Card01'].source = f'.\Image_Picture\{name_picture}'
        self.Update.cancel()
        self.capteur.release()
        screen_manager.current = "mian_screen"

    def active_scroll(self,value):
        if value :
            self.root.get_screen('Result_Screen').ids[f"BoxAbout{value}"].height = dp(5)
            self.root.get_screen('Result_Screen').ids[f"BoxScroll{value}"].height = dp(70)
            self.root.get_screen('Result_Screen').ids[f"FloatLayoutScroll{value}"].size_hint = (0.7,0.25)


            self.scrollview= self.scrollview+1
            if self.scrollview % 2 ==0 :
                self.root.get_screen('Result_Screen').ids[f"BoxAbout{value}"].height = dp(70)
                self.root.get_screen('Result_Screen').ids[f"BoxScroll{value}"].height = dp(25)
                self.root.get_screen('Result_Screen').ids[f"FloatLayoutScroll{value}"].size_hint = (0.2,1)




    def MDspinner(self,*args):
        self.dialog02 = MDDialog(
            size_hint=(1, 1),
            height = '120dp',
            type="custom",
            md_bg_color = self.theme_cls.primary_dark,
            content_cls = SDsr())
        self.dialog02.open()


    def Send_MessageWattsapp(self):
        self.dialog05 = MDDialog(
            height='120dp',
            type="custom",
            md_bg_color=self.theme_cls.primary_dark,
            content_cls=TextField(id = 'bilal'))
        self.dialog05.open()
    def Save_file(self , name):
        import mysql.connector
        self.mydb = mysql.connector.connect(host='Localhost', user='root', password='', database='kivy')
        sql_select_Query = "select * from save_imageprocessing"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(sql_select_Query)
        records = self.mycursor.fetchall()

        if records !=[] :
            self.change_screen(name)
        else :
            self.dialog = MDDialog(
                title='Error',
                text='None Result',
                type="custom",
                md_bg_color=self.theme_cls.primary_dark,
                buttons=[MDRoundFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, theme_text_color="Primary", pos=(0.2, 0.9),
                    on_release=self.close_dialog), ])
            self.dialog.open()
            self.mydb.commit()
            self.mydb.close()
    def Save_file02(self , name):
        import mysql.connector
        self.mydb = mysql.connector.connect(host='Localhost', user='root', password='', database='kivy')
        sql_select_Query01 = "select * from save_image"
        self.mycursor01 = self.mydb.cursor()
        self.mycursor01.execute(sql_select_Query01)
        records01 = self.mycursor01.fetchall()

        if records01 !=[] :
            self.change_screen(name)
        else :
            self.dialog = MDDialog(
                title='Error',
                text='None Result',
                type="custom",
                md_bg_color=self.theme_cls.primary_dark,
                buttons=[MDRoundFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, theme_text_color="Primary", pos=(0.2, 0.9),
                    on_release=self.close_dialog), ])
            self.dialog.open()
            self.mydb.commit()
            self.mydb.close()

    def screenshot(self, widget):

        if self.root.get_screen('mian_screen').ids['Card01'].source !='Image/leaf.png' :
            self.path01 = os.path.dirname(__file__)+'/img'
            data_time = datetime.now().microsecond
            path = f'{self.path01}/picture{str(data_time)}.png'
            self.root.get_screen('mian_screen').ids['BoxMainSave'].export_to_png(path)
            self.Comment = self.root.get_screen('mian_screen').ids["Input_Comment"].text

            self.Save_Image("Save_screenProcessing", self.Comment , path)

        else :
            self.dialog = MDDialog(
                title='Error',
                text='No image found',
                type="custom",
                buttons=[MDRoundFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, theme_text_color="Primary", pos=(0.2, 0.9),
                    on_release=self.close_dialog), ])
            self.dialog.open()
    def Remove_Data(self) :
        self.setApresResult()
        self.root.get_screen('mian_screen').ids['Card01'].source = 'Image/leaf.png'
        self.root.get_screen('mian_screen').ids['Input_Comment'].text= ''
    def back_and_save(self ,*args):
        self.dialogHJ = MDDialog(
            title='Worrning',
            text='Do you want to save the results',
            type="custom",
            md_bg_color=self.theme_cls.primary_dark,
            buttons=[MDRoundFlatButton(
                text="OK", text_color=self.theme_cls.primary_color, theme_text_color="Primary", pos=(0.2, 0.9),
                on_release=self.screenshot_Result03),
                MDRoundFlatButton(
                    text="Cancel", text_color=self.theme_cls.primary_color, theme_text_color="Primary", pos=(0.2, 0.9),
                    on_release=self.Cdialog),
            ])
        self.dialogHJ.open()
    def Cdialog(self , *args) :
        self.dialogHJ.dismiss()
    def screenshot_Result03(self,*args):

        self.Image = self.root.get_screen('Result_Screen').ids['Image_Processing'].source
        self.Location =self.root.get_screen('Result_Screen').ids['Text_Location'].text
        self.DataHure = self.root.get_screen('Result_Screen').ids['Text_data'].text
        self.CommentResult = self.root.get_screen('Result_Screen').ids['Text_Comment'].text
        self.Result01 = self.root.get_screen('Result_Screen').ids['Text_Label1'].text
        self.Result02 = self.root.get_screen('Result_Screen').ids['Text_Label2'].text
        self.Result03 = self.root.get_screen('Result_Screen').ids['Text_Label3'].text
        self.Result04 = self.root.get_screen('Result_Screen').ids['Text_Label4'].text
        self.Result05 = self.root.get_screen('Result_Screen').ids['Text_Label5'].text
        self.Save_Image02('mian_screen',self.Image ,self.Location ,self.DataHure ,self.CommentResult ,
                          self.Result01,self.Result02,self.Result03 , self.Result04,self.Result05 )
        self.dialogHJ.dismiss()
        self.Remove_Data()
        self.setApresResult()
    def screenshot_Result02(self,*args):

        self.Image = self.root.get_screen('Result_Screen').ids['Image_Processing'].source
        self.Location =self.root.get_screen('Result_Screen').ids['Text_Location'].text
        self.DataHure = self.root.get_screen('Result_Screen').ids['Text_data'].text
        self.CommentResult = self.root.get_screen('Result_Screen').ids['Text_Comment'].text
        self.Result01 = self.root.get_screen('Result_Screen').ids['Text_Label1'].text
        self.Result02 = self.root.get_screen('Result_Screen').ids['Text_Label2'].text
        self.Result03 = self.root.get_screen('Result_Screen').ids['Text_Label3'].text
        self.Result04 = self.root.get_screen('Result_Screen').ids['Text_Label4'].text
        self.Result05 = self.root.get_screen('Result_Screen').ids['Text_Label5'].text
        self.Save_Image02('Save_screen',self.Image ,self.Location ,self.DataHure ,self.CommentResult ,
                          self.Result01,self.Result02,self.Result03 , self.Result04,self.Result05 )

        self.Remove_Data()
        self.setApresResult()
    def Save_Image02(self,name, imageProcessing , Location , dataHure , CommentResult , Result01 ,Result02,Result03,Result04,Result05):
        import mysql.connector
        self.mydb = mysql.connector.connect(host='Localhost', user='root', password='', database='kivy')
        sql_select_Query01 = "select * from save_image"
        self.mycursor01 = self.mydb.cursor()
        self.mycursor01.execute(sql_select_Query01)
        records01 = self.mycursor01.fetchall()
        try:
            for r in records01:
                self.id01 = r[12]
            self.id = int(self.id01) + 1
        except:
            self.id = 0
        self.data0 = int(self.id) + 1
        self.file =self.file+1
        self.val_ = True
        self.Card = MD_relativelayout05()
        self.Card.text = f'Result0{self.id}'
        self.Card.source =imageProcessing
        self.Card.text01 = str(datetime.now())
        self.Card.button = 'View_Result_Screen'
        self.Card.dataHure = dataHure
        self.Card.location = Location
        self.commentResult = CommentResult
        self.Card.result01 =Result01
        self.Card.result02 = Result02
        self.Card.result03 = Result03
        self.Card.result04 = Result04
        self.Card.result05 = Result05
        self.Card.ids = {'Result' :self.Card.text }
        self.root.get_screen('Save_screen').ids['SaveCard'].add_widget(self.Card)
        screen_manager.current = name
        self.Set_Value_Excel02(self.Card.source , self.Card.text , self.Card.text01   , self.Card.dataHure,
        self.Card.location , self.commentResult ,self.Card.result01 ,self.Card.result02 ,self.Card.result03 ,self.Card.result04  ,self.Card.result05 , str(self.Card.ids) , str(self.id) )



    def Set_Value_Excel02(self,source , textCard1  ,textCard2  , Data , Location , CResult , R01 ,R02 , R03 , R04 ,R05  , ids ,id ):
        self.id = 0
        import mysql.connector
        self.mydb = mysql.connector.connect(
            host='Localhost',
            user='root',
            password='',
            database='kivy'
        )
        self.mycursor = self.mydb.cursor()
        self.values0 = (source ,textCard1 , textCard2  ,Data,Location , CResult,R01,R02,R03,R04,R05 , ids ,id)
        self.mycursor.execute("insert into save_image values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",self.values0)
        self.mydb.commit()
        self.mydb.close()


    def RemoveImageView(self):
        try:
            self.dialogE = MDDialog(
                title='verification Image',
                text='Are you sure to delete it',
                type="custom",
                buttons=[MDRoundFlatButton(
                    text="OK", text_color=self.theme_cls.primary_dark, theme_text_color="Custom", pos=(0.2, 0.9),
                    on_release=self.Remove_ImageProcessing),
                    MDRoundFlatButton(
                        text="NO", text_color=self.theme_cls.primary_dark, theme_text_color="Custom", pos=(0.2, 0.9),
                        on_release=self.cancelDialog), ])
            self.dialogE.open()

        except:
            pass
    def cancelDialog(self):
        self.dialogE.dismiss()
    def Remove_ImageProcessing(self ,*args):
        self.dialogE.dismiss()
        screen_manager.current = 'Save_screen'

    def RteurnData(self,name,Image  ):

        self.Remove_Data()
        screen_manager.current = name
        self.root.get_screen('View_Result_ScreenProcessing').ids['Add_PathProcessing'].source =Image
    def RteurnProcessing(self ,name ,image):
        self.setApresResult()
        self.Stat = 'close'
        self.Remove_Data()
        screen_manager.current = name
        import mysql.connector
        self.mydb = mysql.connector.connect( host='Localhost',user='root',password='',database='kivy')
        sql_select_Query = "select * from save_imageprocessing"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(sql_select_Query)
        records = self.mycursor.fetchall()
        for row in records:
            if image == row[0] :
                self.root.get_screen('mian_screen').ids["Input_Comment"].text = row[3]
                self.root.get_screen('mian_screen').ids['Card01'].source = image
        self.mydb.commit()
        self.mydb.close()


    def set_MDCard_List(self,widget, text='' ,  search=False  ) :
        print(search)
        print(text)
        import mysql.connector
        if search ==True :
            self.mydb = mysql.connector.connect(host='Localhost', user='root', password='', database='kivy')
            sql_select_Query01 = "select * from save_imageprocessing"
            self.mycursor01 = self.mydb.cursor()
            self.mycursor01.execute(sql_select_Query01)
            records01 = self.mycursor01.fetchall()
            for r01 in records01:
                try:
                    self.root.get_screen('Save_screenProcessing').ids['SaveCardProcessing'].remove_widget(
                        self.root.get_screen('Save_screenProcessing').ids['SaveCardProcessing'].children[0])
                except:
                    pass
                if text == r01[1] :
                    self.SRow =r01[1]
                    Clock.schedule_once(self.Mysql02 , 1)



    def Mysql02(self ,Row ):
        import mysql.connector
        self.mydb = mysql.connector.connect(
            host='Localhost',
            user='root',
            password='',
            database='kivy')
        sql_select_Query01 = "select * from save_imageprocessing"
        self.mycursor01 = self.mydb.cursor()
        self.mycursor01.execute(sql_select_Query01)
        records01 = self.mycursor01.fetchall()
        print(Row)
        for row in records01:
            if row[1] == self.SRow :
                print(f'bilal{row[1]}' , f'sert{Row}')
                self.Card = MD_relativelayout05()
                self.Card.text = row[1]
                self.Card.source = row[0]
                self.Card.text01 = row[2]
                self.Card.comment = row[3]
                self.Card.button = 'View_Result_ScreenProcessing'
                self.root.get_screen('Save_screenProcessing').ids['SaveCardProcessing'].add_widget(self.Card)


        self.mydb.commit()
        self.mydb.close()
    def Save02(self):

        self.dialogF = MDDialog(
            title='Saved Image',
            text='Do you want to save',
            type="custom",
            buttons=[MDRoundFlatButton(
                text="OK", text_color=self.theme_cls.primary_dark, theme_text_color="Custom", pos=(0.2, 0.9),
                on_release=self.Save_02),])

        self.dialogF.open()

    def Save_02(self , *args):
        self.dialogF.dismiss()
        screen_manager.current = 'Save_screen'

    def setApresResult(self):
        self.root.get_screen('Result_Screen').ids['Image_Processing'].source = 'Image/leaf.png'
        self.root.get_screen('Result_Screen').ids['Text_Location'].text = 'Address-City-Country'
        self.root.get_screen('Result_Screen').ids['Text_data'].text = '2222-22-22'
        self.root.get_screen('Result_Screen').ids['Text_Comment'].text = 'No Comment'
        self.root.get_screen('Result_Screen').ids['Text_Label1'].text = 'Result 01  :                000%'
        self.root.get_screen('Result_Screen').ids['Text_Label2'].text = 'Result 02  :                000%'
        self.root.get_screen('Result_Screen').ids['Text_Label3'].text = 'Result 03  :                000%'
        self.root.get_screen('Result_Screen').ids['Text_Label4'].text = 'Result 04  :                000%'
        self.root.get_screen('Result_Screen').ids['Text_Label5'].text = 'Result 05  :                000%'
    def DeleteResultImage(self):
       ImageRuseltD=  self.root.get_screen('View_Result_Screen').ids['Image_Processing'].source
       import mysql.connector
       self.mydb = mysql.connector.connect(host='Localhost', user='root', password='', database='kivy')
       sql_select_Query = "select * from save_image"
       self.mycursor = self.mydb.cursor()
       self.mycursor.execute(sql_select_Query)
       records = self.mycursor.fetchall()

       for r in records:
           if ImageRuseltD == r[0]:
               row = r[1]
               print(ImageRuseltD ,r[0] )
               self.mycursor.execute(f"DELETE FROM save_image WHERE text='{row}';")
               print('bilal')
           try:
               self.root.get_screen('Save_screen').ids['SaveCard'].remove_widget(
                   self.root.get_screen('Save_screen').ids['SaveCard'].children[0])
           except:
               pass
       self.mydb.commit()
       self.mydb.close()
       time.sleep(1)
       self.get_value_Mysql()
       screen_manager.current = 'Save_screen'

    def set_MDCard_List02(self, widget, text='', search=False):
        print(search)
        print(text)
        import mysql.connector
        if search == True:
            self.mydb = mysql.connector.connect(host='Localhost', user='root', password='', database='kivy')
            sql_select_Query01 = "select * from save_image"
            self.mycursor01 = self.mydb.cursor()
            self.mycursor01.execute(sql_select_Query01)
            records01 = self.mycursor01.fetchall()
            for r01 in records01:
                try:
                    self.root.get_screen('Save_screen').ids['SaveCard'].remove_widget(
                        self.root.get_screen('Save_screen').ids['SaveCard'].children[0])
                except:
                    pass
                if text == r01[1] :
                    self.SSRow =r01[1]
                    Clock.schedule_once(self.Mysql03 , 1)



    def Mysql03(self, Row):
        import mysql.connector
        self.mydb = mysql.connector.connect(
            host='Localhost',
            user='root',
            password='',
            database='kivy')
        sql_select_Query01 = "select * from save_image"
        self.mycursor01 = self.mydb.cursor()
        self.mycursor01.execute(sql_select_Query01)
        records01 = self.mycursor01.fetchall()
        print(Row)
        for row01 in records01:
            if row01[1] == self.SSRow:
                print(f'bilal{row01[1]}', f'sert{Row}')
                self.Card = MD_relativelayout05()
                self.Card.source = row01[0]
                self.Card.text = row01[1]
                self.Card.text01 = row01[2]
                self.Card.dataHure = row01[3]
                self.Card.location = row01[4]
                self.Card.commentResult = row01[5]
                self.Card.result01 = row01[6]
                self.Card.result02 = row01[7]
                self.Card.result03 = row01[8]
                self.Card.result04 = row01[9]
                self.Card.result05 = row01[10]
                self.Card.button = 'View_Result_Screen'

                self.root.get_screen('Save_screen').ids['SaveCard'].add_widget(self.Card)
                self.mydb.commit()
                self.mydb.close()



if __name__ == '__main__':
    LabelBase.register(name='MPoppins', fn_regular="poppins\Poppins""-Medium.ttf")
    LabelBase.register(name='Lobster', fn_regular="Lobster\Lobster"
                                                  "-Regular.ttf")
    LabelBase.register(name='RussoOne', fn_regular="font\RussoOne"
                                                   "-Regular.ttf")
    App01().run()
