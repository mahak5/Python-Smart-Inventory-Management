from tkinter import *
import sqlite3
import pandas as pd
from pyprefixspan import pyprefixspan
from pprint import pprint
v = r"C:\\Users\\User\\Desktop\\Minor Project.xlsx"
df = pd.read_excel(v,sheet_name=0, header=0, index_col = False, keep_default_na=True)
# print(df)
conn=sqlite3.connect('Minor.db')
df.to_sql('data', conn, if_exists='replace', index = None)
curs=conn.cursor()
l=[]
#####Creation of sequence of DATABASE######
for i in range(1,3):
    cm= "Select proid from data where custid=%s and dof=1"%(i) #Buying pattern of each cust
    curs.execute(cm)
    r=curs.fetchall()
    s='' #refresh
    for i in r:
        s=s+str(i[0])+' ' #string conversion
    l.append(s)
#print(l)

#####Generate the arragement list using data mining algorithm#####

minsup = 2
len = 1
p = pyprefixspan(l)
p.setminsup(2)
p.setlen(1)
p.run()
#print(p.out)

root=Tk()
root.title("On the Go")
L1=Label(root,text="Welcome to the inventory and arrangement window!",bd=10,relief=RAISED,font=("times new roman",25,"bold"),fg="crimson")
L1.pack()
LB= Label(root, text="Enter the two dates to know your requirements for the period",font=("times new roman",14),bg="white",fg="crimson")
LB.pack()
def listit():
    start_date=E1.get()
    end_date=E2.get()
    cmd = "Select proid,count(*) from data where dof between %s AND %s group by proid"%(start_date,end_date)
    curs.execute(cmd)
    r=curs.fetchall()
    T= Text(root, height=20, width=30)
    T.insert(END,"Product ID| Quantity\n")
    for i in r:
        if(i[0]<10):
            T.insert(END,"%s         |      %s\n"%(i[0],i[1]))
        else:
            T.insert(END,"%s        |      %s\n"%(i[0],i[1]))
    T.pack()

def arrangem():
    T1= Text(root, height=25)
    x=p.out
    T1.insert(END,"SEQUENCE | FREQUENCY\n")
    sbar=Scrollbar(root)
    T1.config(yscrollcommand=sbar.set)
    sbar.config(command=T1.yview)
    for i in x:
        T1.insert(END,"%s|%s\n"%(i,x[i]))
    sbar.pack(side='right')
    T1.pack(side='right')

SDL=Label(root,text="Enter the start date")
EDL=Label(root, text="Enter the end date")
SDL.pack()
E1=Entry(root)
E2=Entry(root)
E1.pack()
EDL.pack()
E2.pack()
B1= Button(root, text="Get the list", command=listit)
B1.pack()
B2= Button(root, text="Get Shelf Arrangement", command=arrangem)
B2.pack()
root.mainloop()



