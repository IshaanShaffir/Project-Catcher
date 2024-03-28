import mysql.connector as mycon
con = mycon.connect(host='localhost',user='root',passwd='arib')
cur = con.cursor()
cur.execute('SHOW DATABASES')
flag = False
for dbname in cur:
        if('recordB' in dbname):
            flag= True
            break
if not flag:
        cur.execute("Create Database recordB")
        print('Database created')
else:
        print('Database Already Exists')
con.commit() 
