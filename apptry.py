import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 


class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 2
		# self.rows = 5

		self.add_widget(Label(text= "Date: "))
		self.date = TextInput(multiline= False)
		self.add_widget(self.date)

		self.add_widget(Label(text= "Video: "))
		self.video = TextInput(multiline= False)
		self.add_widget(self.video)

		self.add_widget(Label(text= "time: "))
		self.time = TextInput(multiline= False)
		self.add_widget(self.time)

		self.add_widget(Label(text= "dress: "))
		self.dress = TextInput(multiline= False)
		self.add_widget(self.dress)

		self.add_widget(Label(text= "diary: "))
		self.diary = TextInput(multiline= True)
		self.add_widget(self.diary)

		self.submit = Button(text="Beauty and Best", font_size= 40)
		self.submit.bind(on_press=self.pressed)
		self.add_widget(self.submit)

	def pressed(self, instance):
		
		date = self.date.text
		diary = self.diary.text

		print("Date: ", date)
		print("Diary:", diary)
 
		self.date.text = " "
		self.diary.text = " "


class MyApp(App):
	def build(self):
		return MyGrid()


if __name__ == "__main__":
	MyApp().run()
