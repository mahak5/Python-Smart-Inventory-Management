from tkinter import *
import sqlite3
import pandas as pd
v = r"C:\\Users\\GOPIKA\\Downloads\\minordata.xlsx"
df = pd.read_excel(v,sheet_name=0, header=0, index_col = False, keep_default_na=True)
# print(df)
conn=sqlite3.connect('Minor.db')
df.to_sql('data', conn, if_exists='replace', index = None)
curs=conn.cursor()
root=Tk()
root.title("On the Go")
L1=Label(root,text="Welcome to the inventory!",bd=10,relief=RAISED,font=("times new roman",25,"bold"),fg="crimson")
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
    T.delete('1.0', END)
    T.insert(END,"Product ID| Quantity\n")
    for i in r:
        if(i[0]<10):
            T.insert(END,"%s         |      %s\n"%(i[0],i[1]))
        else:
            T.insert(END,"%s        |      %s\n"%(i[0],i[1]))
    T.pack()
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
root.mainloop()



