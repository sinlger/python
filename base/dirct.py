aline_0 = {'color':'green','points':5}
aline_0['name'] = 'aline'
aline_0['x_position'] = '0'
aline_0['y_position'] = '5'
aline_0['speed']='slow'
del aline_0['speed']


for key , value in aline_0.items():
    print(key)
    print(value)
print('------------------------')

for key  in aline_0.keys():
    print(key)
print('------------------------')
for value in aline_0.values():
    print(value)
print('------------------------')

print(sorted(aline_0.keys(),reverse=True))
print(aline_0.keys())