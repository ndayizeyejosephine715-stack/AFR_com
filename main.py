import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import webbrowser

class AFRApp(App):
    def build(self):
        return BoxLayout()

    def search_youtube(self, instance):
        query = self.search_input.text
        if query:
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)

if __name__ == "__main__":
    AFRApp().run()
