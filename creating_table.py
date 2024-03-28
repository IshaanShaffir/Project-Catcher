import mysql.connector as mycon
con = mycon.connect(host='localhost',user='root',passwd='arib',database='recordb')
cur = con.cursor()
pc = 'CREATE TABLE RECORD(name varchar(30), score int,id int)'
str1 = 'insert into record values("Arib",10,1)'
str2 = 'insert into record values("Barry",15,2)'
cur.execute(pc)
cur.execute(str1)
cur.execute(str2)
con.commit()
                    
                    
