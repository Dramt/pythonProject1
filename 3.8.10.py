class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.bag = []

    def add_thing(self,thing):
        if (sum(list(map(lambda x:x.weight,self.bag)))+thing.weight)<=self.max_weight:
            self.bag.append(thing)
        else:
            raise ValueError('превышен суммарный вес предметов')


    def __getitem__(self, item):
        if item <= len(self.bag):
            return self.bag[item]
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if key>len(self.bag):
            raise IndexError('неверный индекс')
        if (sum(list(map(lambda x: x.weight, self.bag))) + value.weight - self.bag[key].weight) <= self.max_weight:
            self.bag[key] = value
        else:
            raise ValueError('превышен суммарный вес предметов')
    def __delitem__(self, key):
        if key<=len(self.bag):
            del self.bag[key]
        else:
            raise IndexError('неверный индекс')

class Thing:

    def __init__(self,name, weight):
        self.name = name
        self.weight = weight


    def __setattr__(self, key, value):
        if key == "name" and type(value) == str:
            object.__setattr__(self, key, value)
        elif key == "weight" and type(value) in (int,float):
            object.__setattr__(self, key, value)


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[
    0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[
    1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"