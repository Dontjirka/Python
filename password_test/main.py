import random
import string

class Password:
    def __init__(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def generate(self, length, difficulty):
        chars = ""
        if difficulty == "easy":
            chars = string.ascii_lowercase
        elif difficulty == "medium":
            chars = string.ascii_letters
        elif difficulty == "hard":
            chars = string.ascii_letters + string.digits + "!@#$%^&*"
        self.password = "".join(random.choice(chars) for _ in range(length))

    def check(self, password2):
        return self.password == password2

class PasswordTest:
    def test(self):
        password1 = Password("mypassword")
        password1.generate(8, "medium")
        print("Generated password1:", password1.get_password())
        
        password2 = Password("mypassword")
        password2.generate(8, "medium")
        print("Generated password2:", password2.get_password())
        
        print("Check result:", password1.check(password2.get_password()))


test = PasswordTest()
test.test()
