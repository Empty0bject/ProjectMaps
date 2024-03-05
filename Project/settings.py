class Settings():
    def __init__(self):
        pass
    def Font(self, selection):
        font_selection={
            "standard" :  "Roboto/Roboto-Regular.ttf",
            "dyslexic" : "OpenDyslexic2/OpenDyslexic-Regular.otf"
        }
        print("\n\n\n\n\n\n\n", font_selection[selection], "\n\n\n\n\n\n\n\n\n")
        return font_selection[selection]