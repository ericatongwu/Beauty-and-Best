from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BBApp(App):
	def build(self):
		layout = GridLayout(cols=2)

		date_label = Label(text="Date:")
		video_label = Label(text="Video:")
		time_label = Label(text="Time:")
		dress_label = Label(text="Dress:")
		diary_label = Label(text="Diary:")

		date_text = TextInput(multiline= False)
		video_text = TextInput(multiline= False)
		time_text = TextInput(multiline= False)
		dress_text = TextInput(multiline= False)
		diary_text = TextInput(multiline= True)
		
		submit = Button(text= "Submit", font_size= 40)
		
		layout.add_widget(date_label)
		layout.add_widget(date_text)
		layout.add_widget(video_label)
		layout.add_widget(video_text)
		layout.add_widget(time_label)
		layout.add_widget(time_text)
		layout.add_widget(dress_label)
		layout.add_widget(dress_text)
		layout.add_widget(diary_label)
		layout.add_widget(diary_text)
		layout.add_widget(submit)
		
		return layout	


if __name__ == '__main__':
	BBApp().run()