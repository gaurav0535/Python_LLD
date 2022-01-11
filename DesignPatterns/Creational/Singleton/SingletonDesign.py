class Singleton1:
    __instance = None
    @staticmethod
    def getInstance():
        if Singleton1.__instance is None:
            print("Test")
            Singleton1()
        return Singleton1.__instance

    def __init__(self):
        if Singleton1.__instance is not None:
            raise Exception("Singleton object already created!")
        else:
            Singleton1.__instance = self


s1 = Singleton1()
print(s1)

s2 = Singleton1.getInstance()
print(s2)

s1.x = 5
print(s2.x)


class Singleton2:
    __instance = None

    def __new__(cls):
        if (cls.__instance is None):
            cls.__instance = \
                super(Singleton2, cls).__new__(cls)

        return cls.__instance

s1 = Singleton2()
print(s1)
s2 = Singleton2()
print(s2)

s1.x = 5
print(s2.x)