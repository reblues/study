#coding:utf-8
#!/user/bin/env python


from functools import partial
import Tkinter
'''
root = Tkinter.Tk()
MyButton = partial(Tkinter.Button, root, fg='white', bg='blue')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
qb = MyButton(text='QUIT', bg='red', command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('PFAs!')
root.mainloop()
'''


j, k = 1, 2

def proc1():

    j, k = 3, 4
    print "j == %d and k == %d" % (j, k)
    k = 5

def proc2():

    j = 6
    proc1()
    print "j == %d and k == %d" % (j, k)

k = 7
proc1()
print "j == %d and k == %d" % (j, k)

j = 8
proc2()
print "j == %d and k == %d" % (j, k)


34
17
34
67
87