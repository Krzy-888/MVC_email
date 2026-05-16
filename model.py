import regex as re
class Model:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        if re.fullmatch(pattern,value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')
    
    def save(self):
        with open('email.txt','a') as f:
            f.write(self.email+'\n')

# TEST
# klasa = Model('ABC@mail.com')
# print(klasa.email)
# klasa.save()