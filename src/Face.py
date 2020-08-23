class Face(object):
    age = None

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def print_name(self):
        print(self.__name)

    @classmethod
    def print_age(cls):
        print(cls.age)