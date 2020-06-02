import pymysql as mdb

db = mdb.connect(host='47.96.224.32', port=3306, user='python_test', password='python_test', db='python_test')

cur = db.cursor()

sqlrunoob = 'select * from  runoob'
try:
    # 执行SQL语句
    cur.execute(sqlrunoob)
    # 获取所有记录列表
    results = cur.fetchall()
    for it in results:
        for i in range(len(it)):
            print(it[i])
        print('\n')
except:
    print("Error: unable to fecth data")
