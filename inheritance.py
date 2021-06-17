# Inheritance

class Phone:
    def __init__(self, phone_number):
        self.number = phone_number

    def __str__(self):
        return f'Phone: {self.number}'

    def call(self, other_number):
        print("Calling {} from {}.".format(other_number, self.number))

    def text(self, other_number, msg):
        print("Sending text from {} to {}:".format(self.number, other_number))
        print(msg)

basic_phone = Phone('333-444-5566')
print(basic_phone)

class IPhone(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.fingerprint = None

    def __str__(self): # override this method
        return f'iPhone {self.number}'

    def call(self, other_number):
        print(f'iPhone is calling: {other_number}')

    def set_fingerprint(self, fingerprint):
        self.fingerprint = fingerprint

    def unlock(self, fingerprint=None):
        if (fingerprint == self.fingerprint and fingerprint == None):
            print("Phone unlocked because no fingerprint has not been set.")
        elif (fingerprint == self.fingerprint):
            print("Phone unlocked. Fingerprint matches.")
        else:
            print("Phone locked. Fingerprint doesn't match.")

# Iphone Example
print('# Iphone Example')
iphone_12 = IPhone('555-666-7789')
print(iphone_12)
iphone_12.call('234-444-5678')
iphone_12.set_fingerprint('lskdmalnkaaslfm')
print('Fingerprint', iphone_12.fingerprint)
iphone_12.unlock('lskdmalnkaaslfm')


class IPhoneXI(IPhone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number)
        self.color = color

shawn_phone = IPhoneXI('555-888-7789', 'purple')
print(shawn_phone)
shawn_phone.call('411')


class Android(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)
    self.keyboard = "Default"

  def set_keyboard(self, keyboard):
    self.keyboard = keyboard

# Exercise
# Make a specfic Android phone
# inherit the Android class
# Add 2 methods onto class
# Test class with using some of the parent methods