#HYBRID INHERITANCE 

class Device:
    def power_on(self):
        print("device switched on")
class phone(Device):
    def call(Self):
        print("making a phone call")
class camera:
    def take_photo(self):
        print("Taking a photo")
class musicplayer:
    def playmusic(self):
        print("Playing a music")
class smartphone(camera,musicplayer):
    def call(self):
        print("Making a phone call")
