from re import MULTILINE
import kivy
#kivy.require('2.0.0') # replace with your current kivy version !

from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivymd.uix.button import MDRaisedButton
from kivy.clock import Clock
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.image import Image

fontName = 'NanumGothicBold.ttf'

class LoginScreen(GridLayout):  
  def __init__(self, **kwargs):
    super(LoginScreen, self).__init__(**kwargs)
    self.cols = 1

    self.inside = GridLayout()
    self.inside.cols = 2

    self.inside.add_widget(Label(text='User Name'))
    self.username = TextInput(multiline=False)
    self.inside.add_widget(self.username)
    
    self.inside.add_widget(Label(text='password'))        
    self.password = TextInput(password=True, multiline=False)
    self.inside.add_widget(self.password)

    self.inside.add_widget(Label(text='chatbox'))
    self.chatbox = TextInput(multiline=False)
    self.chatbox.text = 'Tell me ... \n'
    self.inside.add_widget(self.chatbox)
    self.chatbox.bind(on_text_validate=self.on_enter, focus=self.on_focus)

    #self.inside.add_widget(Label(text='checkbox'))
    self.checkbox = CheckBox()
    self.checkbox.bind(active=self.on_checked)
    self.inside.add_widget(self.checkbox)

    self.img = Image(source='sample.bmp')
    self.inside.add_widget(self.img)

    self.inside.add_widget(Label(text='slider'))
    self.slider = Slider(orientation='horizontal',
                            value_track = True,
                            value_track_color=(1,0,0,1))
    self.slider.bind(value=self.on_slider_changed)
    self.inside.add_widget(self.slider)

    self.add_widget(self.inside)

    self.submit = Button(text='Submit')
    #self.submit=MDRaisedButton(text='Kivy Button')
    self.submit.bind(on_press=self.pressed)
    self.add_widget(self.submit)

  def pressed(self, instance):
    print('callback - pressed')
    print(instance)
    print(f'user name = {self.username.text}, Password: {self.password.text}')
    self.username.text = ''
    self.password.text = ''

  def on_enter(self, instance):
    print('on_enter')
    #self.chatbox.text += '\nTell me ...\n'
    print(self.chatbox.text)

  def on_focus(self, instance, value):
    print('on_focus')
    self.chatbox.focus = True
    if value:
      print(f'User focused ({value}) : {instance}')
    else:
      print(f'User defocused : {instance}')

  def on_checked(self, instance, value):
    print('on_checked')
    self.chatbox.focus = True
    if value:
      print(f'checked ({value}) : {instance}')
    else:
      print(f'unchecked : {instance}')

  def on_slider_changed(self, instance, value):
    print(f'on_slider_changed ({value})')

class MyApp(App):

  def build(self):
    #return Label(text='Hello world\n한글', font_name = fontName)
    return LoginScreen()

  def on_start(self):
    print('on_start')

  def on_stop(self):
    print('on_stop')

  def on_pause(self):
    print('on_pause')

  def on_resume(self):
    print('on_resume')



if __name__ == '__main__':
  MyApp().run()