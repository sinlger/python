cars = ['audi','bwm','toyota']

for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())


bool = 'bwm' in cars
print(bool)