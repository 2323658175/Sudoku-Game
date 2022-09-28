import tkinter as tk
import tkinter.messagebox
import pygame as py
import copy
import random
random.seed()
import operator
#判断数组列表是否相同

class Sudoku:
    '''
    数独生成器类， 调用Sudoku实例的 make_digits() 方法，尝试生成数独
    但，数独生成是随机的，那么，可能会成功，也许会失败
    因此，make_digits() 方法的返回值代表生成数独是否成功
    如果 make_digits() 返回 True，那么可以使用实例的 digits 属性，里面有生成的新数独
    '''



    def __init__(self):
        '''
        digits 属性里面保存着当前的数独矩阵
        '''
        self.digits=[]
        self.Sudoku_digits = list()
    def make_digits(self):
        '''
        尝试生成数独，返回值代表生成是否成功
        '''
        #  数独矩阵的列数组，即9个竖行
        col_lists = [[] for i in range(9)]
        #  数独矩阵的区域数组，即九宫格的几个区域
        area_lists = [[] for i in range(3)]
        #  1 - 9 的随机排列
        nine = self.random_nine()
        for i in range(9):
            col_lists[i].append(nine[i])
        area_lists[0] = nine[0:3]
        area_lists[1] = nine[3:6]
        area_lists[2] = nine[6:]

        for i in range(8):
            nine = self.random_nine()
            #  九宫格的当前格已变换，重置当前格的数字
            if i % 3 == 2:
                area_lists[0] = []
                area_lists[1] = []
                area_lists[2] = []
            for j in range(9):
                area_index = j // 3
                count = 0
                error = False
                while nine[0] in col_lists[j] or nine[0] in area_lists[area_index]:
                    count += 1
                    if count >= len(nine):
                        error = True
                        break
                    nine.append(nine.pop(0))
                if error:
                    return False
                first = nine.pop(0)
                col_lists[j].append(first)
                area_lists[area_index].append(first)
        self.digits = copy.deepcopy(col_lists)
        return True

    def random_nine(self):
        '''
        1 - 9 的随机排列
        '''
        nine = [i + 1 for i in range(9)]
        for i in range(5):
            nine.append(nine.pop(random.randint(0, 8)))
        return nine


    def Makeproblem(self):
        while not self.make_digits():
            pass
        # Sudoku_digits[0]存放原矩阵，[1]存放根据难度挖空得到的题目矩阵
        self.Sudoku_digits.append(copy.deepcopy(self.digits))
        self.Sudoku_digits.append(copy.deepcopy(self.digits))
        for row in range(9):
            for i in range(Sudoku_difficulty):
                temp = random.randint(0, 8)
                while self.Sudoku_digits[1][row][temp] == 0:
                    temp = random.randint(0, 8)
                self.Sudoku_digits[1][row][temp] = 0
        return True








#定义函数
def if_solve(digit):#判断是否有解，返回0，1
    return 1

def if_isanswer(digit1,digit2):#判断是否是正确的解，1为原解，2为待判断的解，返回0，1
    if operator.eq(digit2,digit1):
        return 1
    for row in digit2:
        for i in row:
            if i not in [1,2,3,4,5,6,7,8,9]:
                return 0
    for row in digit2:
        if len(set(row)) != len(row):
            return 0
    for c in range(9):
        column=[]
        for i in range(9):
            column.append(digit2[c][i])
        if len(set(column)) != len(column):
            return 0
    for t1 in range(3):
        for t2 in range(3):
            NineBlockBox=[]
            for i in range(3*t1,3*t1+3):
                for j in range(3*t2,3*t2+3):
                    NineBlockBox.append(digit2[i][j])
            if len(set(NineBlockBox)) != len(NineBlockBox):
                return 0
    return 1





def Goto_main():#进入主界面
    for item in Frame_digitdesk.winfo_children():
        item.destroy()
    Frame_game.forget()
    Frame_main.pack()


def initialize():#全部初始化
    tk.messagebox.showinfo(title='', message='作者太懒，此功能尚未完成')


def countine_game():#继续游戏
    tk.messagebox.showinfo(title='',message='作者太懒，此功能尚未完成')



def game_history():#查看历史记录
    tk.messagebox.showinfo(title='', message='作者太懒，此功能尚未完成')

def Help():#显示帮助
    tk.messagebox.showinfo(title='', message='作者太懒，此功能尚未完成(注：难度调整功能应未知原因失效)')


def exit_game():#退出游戏
    window.destroy()






#背景音乐
py.mixer.init()
py.mixer.music.set_volume(0.5)
py.mixer.music.load(r'.\bgm.mp3')
py.mixer.music.play(-1,0)
def open_bgm():
    py.mixer.music.unpause()
def off_bgm():
    py.mixer.music.pause()

def Confirm_answer():#确认答案
    k=0
    for i in range(9):
        for j in range(9):
            if Current_Sudoku.Sudoku_digits[1][i][j]==0:
                Current_Sudoku.Sudoku_digits[1][i][j] = Getinput[k].get()
                k+=1
    if if_isanswer(Current_Sudoku.Sudoku_digits[0],Current_Sudoku.Sudoku_digits[1]):
        tk.messagebox.showinfo(title='',message='You are right!')
    else:
        tk.messagebox.showinfo(title='',message='You are wrong!')
    Goto_main()


def changedifficultya():#修改难度
    Sudoku_difficulty = 4
def changedifficultyb():
    Sudoku_difficulty = 5
def changedifficultyc():
    Sudoku_difficulty=6
#全局变量
Sudoku_difficulty=4   #范围为[4,6]
Current_Sudoku = Sudoku()
Getinput=list()

def start_newgame():#开始游戏
    Frame_main.forget()
    Frame_game.pack()
    Current_Sudoku.__init__()
    while Current_Sudoku.Makeproblem()!= True:
        Current_Sudoku.__init__()
    Getinput.clear()
    for i in range(9):
        for j in range(9):
            if Current_Sudoku.Sudoku_digits[1][i][j]==0:
                entry=tk.Entry(Frame_digitdesk,width=2)
                entry.grid(column=i,row=j,padx=10,pady=10,ipadx=10,ipady=10)

                Getinput.append(entry)
            else:
                tk.Label(Frame_digitdesk,text=str(Current_Sudoku.Sudoku_digits[1][i][j]).center(3,' ')).grid(column=i,row=j,padx=10,pady=10,ipadx=10,ipady=10)

    Frame_digitdesk.pack(side='left')
    button_goback.pack(side='right')
    button_confirm.pack(side='right')


#建立窗口
window = tk.Tk()
window.title("数独")
window.geometry('800x600')
window.resizable(width=False,height=False)
#创建菜单栏
menubar = tk.Menu(window)
optionmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='设置', menu=optionmenu)
optionmenu_degree=tk.Menu(optionmenu,tearoff=0)
optionmenu.add_cascade(label='难度',menu=optionmenu_degree)
optionmenu_degree.add_command(label='简单',command=changedifficultya)
optionmenu_degree.add_separator()
optionmenu_degree.add_command(label='普通',command=changedifficultyb)
optionmenu_degree.add_separator()
optionmenu_degree.add_command(label='困难',command=changedifficultyc)
optionmenu.add_separator()
optionmenu_bgm = tk.Menu(optionmenu,tearoff=0)
optionmenu.add_cascade(label='背景音乐',menu=optionmenu_bgm)
optionmenu_bgm.add_command(label='打开',command=open_bgm)
optionmenu_bgm.add_command(label='关闭',command=off_bgm)
optionmenu.add_separator()
optionmenu.add_command(label='初始化', command=initialize)
menubar.add_command(label='帮助',command=Help)
window.config(menu=menubar)
Frame_main = tk.Frame(window,bg='white',width=800,height=600)
buttonstart1=tk.Button(Frame_main,text='新游戏',font=('simkai',12),bg='white',fg='red',width=70,height=8,command=start_newgame)
buttonstart2=tk.Button(Frame_main,text='继续游戏',font=('simkai',12),bg='white',fg='red',width=70,height=8,command=countine_game)
buttonstart3 = tk.Button(Frame_main, text='历史记录', font=('simkai', 12), bg='white', fg='red', width=70, height=8,command=game_history)
buttonstart4 = tk.Button(Frame_main, text='退出', font=('simkai', 12), bg='white', fg='red', width=70, height=8,command=exit_game)
Frame_main.pack()
buttonstart1.pack()
buttonstart2.pack()
buttonstart3.pack()
buttonstart4.pack()
# 游戏界面
Frame_game = tk.Frame(window, width=800, height=600)
Frame_digitdesk = tk.Frame(Frame_game, width=600, height=600, bg='black')
button_goback=tk.Button(Frame_game,text='返回',font=('simkai',12),bg='white',fg='red',width=10,height=4,command=Goto_main)
button_confirm = tk.Button(Frame_game,text='确认',font=('simkai',12),bg='white',fg='red',width=10,height=4,command=Confirm_answer)


window.mainloop()



