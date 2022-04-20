from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.lang import Builder

kv = '''
<DragLabel>:
    # Define the properties for the DragLabel
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0

FloatLayout:
    # Define the root widget
    DragLabel:
        size_hint: 0.25, 0.2
        text: 'Drag me'
'''

class Gui(App):

    def build(self):
        self.window = GridLayout()
        self.window.cols = 2
        self.window.add_widget(Image(source='hello.jpg'))
        return self.window

class DragLabel(DragBehavior, Label):
    pass


class TestApp(App):
    def build(self):
        return Builder.load_string(kv)

def main():
    Gui().run()


main()