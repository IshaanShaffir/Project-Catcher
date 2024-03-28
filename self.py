import mysql.connector as mycon
con = mycon.connect(host='localhost',user='root',passwd='arib',database='recordb')
cur = con.cursor()
from tkinter import *
from tkinter import ttk

a = input('enter the user')
b = int(input('enter id'))

A = []
A.append(a)
A.append(b)
T = tuple(A)
y = 'update record set name = %s where id = %s'
cur.execute(y,T)
con.commit()