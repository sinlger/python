import json
num = [0,9,8,7,5,4,3,3,2]



with open('pi.txt','w') as filex:
    json.dump(num,filex )