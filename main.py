#! .venv/bin/python3
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class MainWindow(MDBoxLayout):
    def __init__(self):
        super().__init__()
        self.max_length = 10
        self.label = '0'
        self.symbols = ['/', '*', '-', '+', '.']

    def calculate(self):
        try:
            ans = eval(self.label)
            koll_round_symbols = len(str(ans)) - self.max_length
            if koll_round_symbols > 0:
                ans = round(ans, koll_round_symbols)
            if len(str(ans)) > 2:
                if str(ans)[-2] == '.' and str(ans)[-1] == '0':
                    ans = round(ans)
        except:
            ans = 'ERROR'
        self.label = str(ans)
        self.ans_label.text = self.label

    def add_number(self, instance):
        if self.label == '0' or self.label == 'ERROR':
            self.label = ''
        self.label += instance.text
        self.ans_label.text = self.label

    def add_symbol(self, instance):
        if self.label == '0' or self.label == 'ERROR':
            if instance.text != '.':
                self.label = instance.text
            else:
                self.label += instance.text
        else:
            if self.label[-1] not in self.symbols:
                self.label += instance.text
        self.ans_label.text = self.label

    def clear_label(self):
        self.label = '0'
        self.ans_label.text = self.label

    def delete_symbol(self):
        if len(self.label) == 1:
            self.label = '0'
        else:
            self.label = self.label[:-1]
        self.ans_label.text = self.label


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = '500'
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()
