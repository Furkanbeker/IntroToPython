def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3,4,5))

def calculate(n , **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3 , multiply = 5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan" , model="GTR", colour = "Red")
print(my_car.model)



