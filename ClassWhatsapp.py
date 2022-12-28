import os

from twilio.rest import Client
import pywhatkit


class Whatsapp():
    def __init__(self, NumbreWhatsapp, Image, Messages):
        self.NumbreWhatsapp = NumbreWhatsapp
        self.Image = Image
        self.Messages = Messages

    def Send_Message(self):
        self.Client = pywhatkit.sendwhats_image(self.NumbreWhatsapp, img_path='img/2.jpg', caption=self.Messages,
                                                wait_time=10, tab_close=False, close_time=3)
        if self.Client:
            return self.Client
if __name__ == '__main__':
    pass

