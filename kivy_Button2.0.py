from kivy.app import App
from kivy.uix.button import Button

def botao_precionado(instace):
    print("Botao precionado!")

class MinhaApp(App):
    def build(self):
        btn = Button(text='Clique Aqui')
        btn.bind(on_press=botao_precionado)
        return btn
    
if __name__ == '__main__':
    MinhaApp().run()