from kivy import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import DragBehavior
from kivy.uix.image import Image
from kivy.metrics import sp
from kivy.core.window import Window

Builder.load_file("tangoRobot.kv")


#  1) Drive Option 01: Motor sent speed, time, direction from user
class drivingOneBtn(Widget):
    pass


#  2) Drive Option 02: Robot turn left right for x seconds
class drivingTwoBtn(Widget):
    pass


# Used for creating the UI
class TangoTouchUILayout(Widget):

    def __init__(self, **kwargs):
        # super function can be used to gain access
        # to inherited methods from a parent or sibling
        # class that has been overwritten in a class object.
        super(TangoTouchUILayout, self).__init__(**kwargs)

        # 4 columns in grid layout
        self.cols = 3
        #speed, time, direction
        # declaring the slider and adding some effects to it
        self.speedControl = Slider(min=4500, max=7500)

        # 1st row - one label, one slider
        self.add_widget(Label(text='Min'))
        self.add_widget(self.speedControl)

        # 2nd row - one label for caption,
        # one label for slider value
        self.add_widget(Label(text='Slider Value'))
        self.brightnessValue = Label(text='0')
        self.add_widget(self.brightnessValue)

        # On the slider object Attach a callback
        # for the attribute named value
        self.speedControl.bind(value=self.on_value)

    # Adding functionality behind the slider
    # i.e when pressed increase the value
    def on_value(self, instance, brightness):
        self.brightnessValue.text = "% d" % brightness


class TangoTouchUIApp(App):
    def build(self):
        Window.clearcolor = (240/255, 240/255, 240/255, 1)
        return TangoTouchUILayout()


if __name__ == "__main__":
    TangoTouchUIApp().run()
