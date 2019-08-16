from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import *
from time import strftime
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

class ClockApp(App):
    sw_seconds = 0
    sw_started =False

    def update_time(self,nap):
        if self.sw_started:
            self.sw_seconds += nap
        minutes,seconds = divmod(self.sw_seconds,60)
        self.root.ids.stopwatch.text = ("%02d:%02d.[size=40]%02d[/size]"%(int(minutes),int(seconds),int(seconds*100%100)))
        # self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')
        self.root.ids.time.text = strftime('%02d:%02d:%02d' % (int(minutes // 60), int(minutes), int(seconds)))

    def on_start(self):
        Clock.schedule_interval(self.update_time,0)

    def start_stop(self):
        self.root.ids.start_stop.text =("Start" if self.sw_started else "Stop")
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text ="Start"
            self.sw_started = False

        self.sw_seconds = 0

class RobotoButton():
    pass

class ClockLayout(BoxLayout):
    time_prop = ObjectProperty(None)
    def __init__(self):
        self.root.time_prop.text = "demo"

if __name__=="__main__":
    # changing the background color
    Window.clearcolor = get_color_from_hex('#101216')
    LabelBase.register(name="Roboto",
                       fn_regular="roboto/Roboto-Regular.ttf",
                       fn_bold="roboto/Roboto-Bold.ttf")

    ClockApp().run()


