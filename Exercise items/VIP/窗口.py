import tkinter as t
import webbrowser


result = ['http://jx.du2.cc/?url=', 'http://jx.598110.com/?url=',
          'http://jx.618ge.com/?url=', 'http://vip.jlsprh.com/?url=', 'http://jx.drgxj.com/?url=']

on = result[0]
tw = result[1]
th = result[2]
fo = result[3]
fi = result[4]

# 窗口
root = t.Tk()

# 窗口大小
root.geometry('600x300')

root.title('哒哒哒')

r0 = t.Label(root, text='选择接口:', font=12)
r0.grid(row=0, column=0)

r1 = t.Label(root, text='播放地址：', font=12)
r1.grid(row=7, column=0)

# 输入框
e1 = t.Entry(root, text='', width=60)
e1.grid(row=7, column=1)

var = t.StringVar()

l1 = t.Radiobutton(root, text='①号通用vip引擎系统【稳定通用】',
                   font=12, variable=var, value=on)
l1.grid(row=1, column=1)

l2 = t.Radiobutton(root, text='②号通用vip引擎系统【稳定通用】',
                   font=12, variable=var, value=tw)
l2.grid(row=2, column=1)

l3 = t.Radiobutton(root, text='③号通用vip引擎系统【稳定通用】',
                   font=12, variable=var, value=th)
l3.grid(row=3, column=1)

l4 = t.Radiobutton(root, text='④号通用vip引擎系统【稳定通用】',
                   font=12, variable=var, value=fo)
l4.grid(row=4, column=1)

l5 = t.Radiobutton(root, text='⑤号通用vip引擎系统【全网解析】',
                   font=12, variable=var, value=fi)
l5.grid(row=5, column=1)


# 删除
def del_t():
    e1.delete(0, 'end')

# 打开网页


def bf():
    webbrowser.open(var.get() + e1.get())


# 按钮
a1 = t.Button(root, text='开始播放', font=12, command=bf)
a1.grid(row=8, column=1)

a2 = t.Button(root, text='清除', font=12, command=del_t)
a2.grid(row=9, column=1)


root.mainloop()
