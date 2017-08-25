class AgeValidator():
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __get__(self, instance, owner):
        return instance.__dict__[self.storage_name]

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('age must be > 0')

class Person():
    age = AgeValidator('age')

    def __init__(self, age):
        self.age = age


if __name__ == '__main__':
    lexa = Person(19)
    print(lexa.__dict__)
    print(lexa.age)

    sasha = Person(-32)