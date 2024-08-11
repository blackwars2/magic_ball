from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random

__version__ = '0.0.1'

class EightBallApp(App):
    def build(self):
        self.title = "8 Ball"
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Я магический черный шар 8-Ball", font_size=32, size_hint_y=None, height=50)
        self.layout.add_widget(self.label)

        self.name_input = TextInput(hint_text='Введи свое имя человек', multiline=False, size_hint_y=None, height=30)
        self.layout.add_widget(self.name_input)

        self.question_input = TextInput(hint_text='Введи свой вопрос', multiline=False, size_hint_y=None, height=30)
        self.layout.add_widget(self.question_input)

        self.answer_label = Label(text="", font_size=24, size_hint_y=None, height=50)
        self.layout.add_widget(self.answer_label)

        self.ask_button = Button(text="Спросить", size_hint_y=None, height=50)
        self.ask_button.bind(on_press=self.get_answer)
        self.layout.add_widget(self.ask_button)

        self.again_button = Button(text="Попробовать снова", size_hint_y=None, height=50)
        self.again_button.bind(on_press=self.clear_input)
        self.layout.add_widget(self.again_button)

        return self.layout

    def get_answer(self, instance):
        name = self.name_input.text.capitalize()
        if name:
            answer = random.choice(["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"])
            self.answer_label.text = f"{name}, {answer}"
        else:
            self.answer_label.text = "Пожалуйста, введите ваше имя."

    def clear_input(self, instance):
        self.name_input.text = ""
        self.question_input.text = ""
        self.answer_label.text = ""

if __name__ == "__main__":
    EightBallApp().run()