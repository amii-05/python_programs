#POLYMORPHISM MANY FORMS
#METHOD OVERRIDING
class phone:
    def camera(self):
        print("Taking a normal photo")
    def camera(self):
        print("Taking a portrait photo")
mi=smartphone()
mi.camera()
nokia=phone()
nokia.camera()
print()