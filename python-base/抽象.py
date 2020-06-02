fibs = [0,1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])


def fibsfn(num):
    '''菲比纳妾函数'''
    fibs = [0, 1]
    for i in range(int(num)):
        fibs.append(fibs[-2] + fibs[-1])

    print(fibs)

def myname(data):
    data['first']={}
    data['middle'] = {}
    data['last'] = {}
def lookdata(data,lable,name):
    return data[lable].get(name)

def store(data,fullname):
    names = fullname.split()
    if len(names)==2:names.insert(1,'')
    lables = 'first','middle','last'
    for name,lable in zip(names,lables):
        peple = lookdata(data,lable,name)
        if peple:
            peple.append(fullname)
        else:
            data[lable][name] = [fullname]



myName1 = {}
myname(myName1)
store(myName1,'dong he')
store(myName1,'xiang li he')


s= lookdata(myName1,'first','xiang')
print(s)
