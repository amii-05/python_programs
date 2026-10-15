#INHERITANCE
#SINGLE INHERITANCE - ONE PARENT -> ONE CHILD

class Device:
    def power_on(self):
        print("device switched on")
class phone(Device):
    def call(Self):
        print("making a phone call")
samsung=phone
samsung.call()
samsung.power_on()
print()