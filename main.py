from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class NXAimPro(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        layout.add_widget(Label(text='NX AIM PRO', font_size=32))
        layout.add_widget(Label(text='Welcome to your Aim Trainer'))
        btn = Button(text='START TRAINING', font_size=22)
        btn.bind(on_press=self.start_training)
        layout.add_widget(btn)
        self.status = Label(text='Ready')
        layout.add_widget(self.status)
        return layout

    def start_training(self, instance):
        self.status.text = 'Training Started!'

NXAimPro().run()
