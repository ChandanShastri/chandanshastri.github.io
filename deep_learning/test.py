#print('Hello')
from tkinter import *
import base64
 
window = Tk()
chandanIcon="AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAABILAAASCwAAAAAAAAAAAAD/////0tLS/3l5ef+urq7/pKSk/6enp/+np6f/p6en/6ampv+oqKj/qKio/6Ojo/+vr6//bW1t/87Ozv///////////87Ozv+6urr///////n5+f/Y2Nj/2NjY/9bW1v/h4eH/39/f/87Ozv/m5ub//////6Ojo//IyMj////////////Ozs7/t7e3///////Z2dn/0tLS/8nJyf++vr7/uLi4/729vf+3t7f/wcHB//////+jo6P/yMjI////////////zs7O/7m5uf//////7e3t/7Gxsf+/v7//4uLi/+3t7v/y8vL/4+Pj/9/f3///////pKSk/8jIyP///////////87Ozv+4uLj//////+Hh4f9nZ2f/a2tr/2RkZP+AgID/zs7O///////7+/v//////6SkpP/Jycn////////////Ozs7/ubm5///////5+fn//v7+//r6+v/c3Nz/mpqa/z09Pf9fX1//6urq//////+ioqL/ycnJ////////////zs7O/7m5uf///////Pz8//39/f/8/Pz//Pz8//////+0tLT/AAAA/0JCQ///////o6Oj/8jIyP///////////87Ozv+5ubn///////n5+f/8/Pz///////39/f//////kJCQ/xwcHP8qKir//////6enp//IyMj////////////Ozs7/ubm5///////8/Pz//f39/8bGxv9qamr/Hx8f/1hYWf+Dg4P/wMDA//////+ioqL/ycnJ////////////zs7O/7e3t///////0NDQ/0BAQP8DAwP/Pz8//52dnf/h4eH///////v7+///////pKSk/8nJyf///////////83Nzf+3t7f//////0RERP8AAAD/gYGB///////8/Pz//f39//r6+v/4+Pj//////6SkpP/Jycn////////////Ozs7/t7e3//////+5ubn/JCQk/0JCQv/k5OT///////7+/v//////+/v7//////+jo6P/ycnJ////////////zs7O/7q6uv///////////+3t7f9/f3//Pj4+/11dXf+Ojo7/vb29//f39///////pKSk/8jIyP///////////87Ozv+tra3/+vr6/+rq6v/29vb//////+np6f+srKz/b29v/1hYWP/h4eH//////5iYmP/Kysr////////////R0dH/gICA/7u7u/+srKz/l5eX/5CQkP+cnJz/pKSk/62trf+mpqb/sLCw/7y8vP9zc3P/zc3N////////////0tLS/66urv/19fX/4ODg/6urq/+goKD/p6en/6CgoP+urq7/qamp/+Tk5P/39/f/nJyc/83Nzf//////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
window.iconbitmap(base64.b64decode(chandanIcon))
window.title("CS")
label_1=Label(window,text="CHANDAN SHASTRI",font=("Calibri",20))
window.geometry('500x500')

label_1.grid(column=0,row=1)

v=1

def change(event):
    global v
    if (v==1) :
        label_1.configure(text="SHASTRI")
        v=0
    else :
        label_1.configure(text="CHANDAN SHASTRI")
        but.configure(bd=1)
        v=1
    print(v)


but=Button(window,text="MDKDK",bd=5)
but.bind("<Button-1>",change)
but.grid(column=2,row=10)




window.mainloop()




#pyinstaller --name 'Chandan Shastri' --icon chandanshastri.ico  --onefile -w .\test.py
#bin64 for file icons