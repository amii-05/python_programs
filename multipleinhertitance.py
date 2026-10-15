#MULTIPLE INHERITANCE - FATHER -> MOTHER -> CHILD
class camera:
    def take_photo(self):
        print("Taking a photo")
class musicplayer:
    def playmusic(self):
        print("Playing a music")
class smartphone(camera,musicplayer):
    def call(self):
        print("Making a phone call")
mi=smartphone()
mi.playmusic()
mi.take_photo()
mi.call
print()