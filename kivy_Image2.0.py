from kivy.app import App
from kivy.uix.image import Image,AsyncImage

class MinhaApp(App):
    def build(self):

        return AsyncImage(source='https://th.bing.com/th/id/R.fa306644316394b2f33744832e0505e8?rik=p4YlKLP7vPAd8A&pid=ImgRaw&r=0')
    
if __name__ == '__main__':
    MinhaApp().run()