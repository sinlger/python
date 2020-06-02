bicyles = ['trek','redline','sanqiang']
print(bicyles)
print(bicyles[-1])
print(bicyles[0])
bicyles[-1]='xiaodao'
print(bicyles[-1])
bicyles.append('sanqiang')
bicyles.insert(0,'kuche')
print(bicyles)
del bicyles[0]
print(bicyles)
bicyles_lasy = bicyles.pop()
print(bicyles_lasy)
print(bicyles)
trck = 'trek'
bicyles.remove(trck)
print(bicyles)

car = ['bwm','audio','toyta','sl']
car.sort()
print(car)
car.sort(reverse=True)
print(car)
print(sorted(car))
print(len(car))