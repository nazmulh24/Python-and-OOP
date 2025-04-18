"""
def call():
    print("calling someone i dont know")
    return "call done"


class Phone:
    price = 12000
    color = "blue"
    brand = "samsung"
    features = ["camera", "speaker", "hammer"]

    def call(self):
        print("calling one person")

    def send_sms(self, phone, sms):
        text = f"sending SMS to: {phone} and message: {sms}"
        return text


my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(41524, "Missy, I missed to miss you")
print(result)
"""


def call():
    print("Calling someone i dont know")
    return "Call done"


class Phone:
    price = 12000
    color = "red"
    brand = "Samsung"
    feature = ["camera", "calling", "gamming"]

    def call(self):
        print("Calling someone")

    def send_sms(self, phone, sms):
        text = f"sending SMS to : {phone} and message : {sms}"
        return text


my_phone = Phone()
print(my_phone.feature)
my_phone.call()

result = my_phone.send_sms(176032, "I miss u")
print(result)
