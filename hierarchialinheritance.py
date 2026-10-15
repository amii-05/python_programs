#HIERARCHICAL INHERITANCE ONE PARENT -> MULTIPLE CHILD

class Device:
    def power_on(self):
        print("Device switched on")
class phone(Device):
    def call(self):
        print("Making a phone call")
class computer(Device):
    def run_program(self):
        print("Running a python program")
iphone=phone()
iphone.power_on()
iphone.call()
hp=computer()
hp.power_on()
hp.run_program()
print()