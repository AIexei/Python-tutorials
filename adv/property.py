class Person:
    def __init__(self):
        self._name = 'Lexa'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')

        self._name = value

    #name = property(get_name, set_name)


if __name__ == '__main__':
    lexa = Person()
    print(lexa.__dict__)
    lexa.name = 10
