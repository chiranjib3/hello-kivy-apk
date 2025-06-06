from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HelloWorldApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50)
        button = Button(text="Click Me")

        def show_popup(instance):
            popup = Popup(title='Hello World',
                          content=Label(text='Hello, World!'),
                          size_hint=(None, None), size=(300, 200))
            popup.open()

        button.bind(on_press=show_popup)
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    HelloWorldApp().run()

