from kivy.app import App
from kivy.uix.widget import Widget

from kivy.utils import get_color_from_hex
from kivy.config import Config
# set the size of window before calling it otherwise it wouldn't work
Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '540')
#disable the multitouch
Config.set('input', 'mouse', 'mouse,disable_multitouch')
# disable the resizing
# Config.set('graphics', 'resizable', '0')
from kivy.core.window import Window
from kivy.base import EventLoop
from kivy.graphics import Canvas,Line,Color
from kivy.lang import Builder
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton

CURSOR = (
    '       @@@@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @@@@             ',
    '                        ',
    '@@@@@@ @@@@ @@@@@@      ',
    '@----@ @--@ @----@      ',
    '@----@ @--@ @----@      ',
    '@@@@@@ @@@@ @@@@@@      ',
    '                        ',
    '       @@@@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @@@@             ',
    '                        ',
    '                        ',
    '                        ',
    '                        ',
    '                        ',
    '                        ',
)


class CanvasWidget(Widget):
    line_width = 2

    def set_line_width(self,line_Width="Normal"):
        self.line_width= {"Thin":1,"Normal":2,"Thick":4}[line_Width]

    def on_touch_down(self, touch):
        if Widget.on_touch_down(self,touch):
            return

        with self.canvas:
            # This draws an empty circle around every touch that our widget receives
            #
            touch.ud['current_line'] = Line(points=(touch.x,touch.y),width = self.line_width)
            #Line(circle=(touch.x, touch.y, 20),width =10)




    def on_touch_move(self, touch):
        if "current_line" in touch.ud:
            touch.ud['current_line'].points += (touch.x,touch.y)

    def clear_canvas(self):
        saved = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        for widget in saved:
            self.add_widget(widget)

        self.set_color(self.last_color)

    def set_color(self,new_color):
        self.last_color = new_color
        self.canvas.add(Color(*new_color))

def pygame_compile_cursor(black='@', white='-'):
    aa, bb = [], []
    a = b = 0
    i = 8
    for s in CURSOR:
        for c in s:
            a <<= 1
            b <<= 1
            i -= 1
            if c == black:
                a |= 1
                b |= 1
            elif c == white:
                b |= 1

            if not i:
                aa.append(a)
                bb.append(b)
                a = b = 0
                i = 8

    return tuple(aa), tuple(bb)

# We allow the button to toggle like it normally would only if it wasn't
# already selected (its state is 'normal', as opposed to 'down').
class RadioButton(ToggleButton):
    def _do_press(self):
        if self.state == "normal":
            ToggleButtonBehavior._do_press(self)


# EventLoop.ensure_window(): This function call blocks the execution until
# we have the application window (EventLoop.window) ready.
# • if EventLoop.window.__class__.__name__.endswith('Pygame'):
# This condition checks the window class name (not the greatest way to
# make assertions about the code, but works in this case). We want to run
# our mouse cursor customization code only for a certain window provider,
# in this case, Pygame.
# • The remaining part of the code, enclosed in a try ... except block, is a
# Pygame-specific mouse.set_cursor call.
# • Variables a and b constitute the internal representation of the cursor used
# by SDL, namely the XOR and AND mask. They are binary and should be
# considered an opaque implementation detail of the SDL.
class PaintApp(App):
    def build(self):
        # The set_color() method will be implemented shortly.
        self.canvas_widget = CanvasWidget()
        self.canvas_widget.set_color(get_color_from_hex('#000000'))
        return self.canvas_widget

        # return CanvasWidget()

if __name__ == '__main__':

    # set the color of the screen
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    PaintApp().run()