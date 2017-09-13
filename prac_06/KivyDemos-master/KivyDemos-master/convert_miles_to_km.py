
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKmApp(App):

    def build(self):
        """build the Kivy app from the kv file"""
        Window.size = (1000, 500)
        self.title = "Convert mile to km"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_calculate(self, value):
        if value < 0:
            self.root.ids.output_label.text = '0.0'
        else:
            result = value / 0.62137
            self.root.ids.output_label.text = str(result)

    def handle_increment(self, value):
        try:
            result = int(self.root.ids.input_number.text) + value
        except ValueError:
            result = 0 + value
        self.root.ids.input_number.text = str(result)


MilesToKmApp().run()
