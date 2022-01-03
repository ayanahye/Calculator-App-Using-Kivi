# Must have the kivy packages installed to run this program

import kivy
from kivy.app import App  # import main App class
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder

# root is getting the main window and expanding to that
Builder.load_file('calc.kv')
Window.size = (350, 500) # setting the dimensions of the window


class MyCalc(Widget):
    def clicked(self, num): # when a number is clicked
        old = self.ids.the_input.text
        if old == '0':
            self.ids.the_input.text = ''
            self.ids.the_input.text = f'{num}'
        elif self.ids.the_input.text == "Undefined":
          self.ids.the_input.text = ''
        else:
          self.ids.the_input.text = f"{old}{num}"

    def clear(self): # when 'AC' is clicked
        self.ids.the_input.text = ''

    def pos_neg(self): # when '+/-' is clicked
        old = self.ids.the_input.text
        if '-' in old:
            self.ids.the_input.text = f"{old.replace('-', '')}"
        else:
            self.ids.the_input.text = f"-{old}"

    def multidec(self): # to append multiple '.'s to the number
        old = self.ids.the_input.text
        operations = ['+', '-', '/', '*', '%']
        for o in operations:
          l = old.split(o)
          if o in old and '.' not in l[-1]:
            self.ids.the_input.text = f"{old}."
        if '.' in old:
            pass
        else:
            self.ids.the_input.text = f"{old}."

    def answer(self): # calculating the result
      try:
        self.ids.the_input.text = str(eval(self.ids.the_input.text))
        if len(self.ids.the_input.text) > 7:
          self.ids.the_input.text = self.ids.the_input.text[0:8]
      except:
        self.ids.the_input.text = 'Undefined'


class MyApp(App):  # inheriting from App class
    def build(self):  # calling build method from App class
        return MyCalc()


if __name__ == "__main__":
    MyApp().run()  # run method is in the App class
