import tkinter as tk
import tkinter.filedialog
import os


# 创建文件选择对话框并将所选文件转换成csv文件
def choose_log_file():
    default_dir = r"文件路径"
    global file_path
    file_path = tk.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
    if len(file_path) > 0:
        print(file_path)
        insert_end(file_path + '\n')
        # Todo: 添加一个判断 防止选取多次产生多个按钮
        b2 = tk.Button(top_right_frame, text='Transform To CSV', width=15,
                       height=2, command=transform_to_csv)
        b2.pack(side='right')


def transform_to_csv():
    # TODO: 将其划分成几个部分 一个是显示部分 用于筛选所需要的信息 另一个部分用于生成csv格式文件
    # 将log装换成csv格式
    log_file = open(file_path, "r", encoding='UTF-8')
    file_name_start = file_path.rfind('/')
    file_name_end = file_path.rfind('.')
    csv_name = file_path[file_name_start + 1:file_name_end] + ".csv"
    csv_file = open(csv_name, 'wb')
    delimiter = ','
    csv_file.write("date,time,pid,tid,level,tag,message\n".encode("utf-8"))
    for line in log_file:
        line_txt = line.rstrip()
        insert_end(line_txt + '\n')     # 将其显示到Text中
        date_end = line_txt.find(' ')
        date = line_txt[:date_end]
        line_txt = line_txt[date_end:].lstrip()
        time_end = line_txt.find(' ')
        time = line_txt[:time_end]
        line_txt = line_txt[time_end:].lstrip()
        pid_end = line_txt.find(' ')
        pid = line_txt[:pid_end]
        line_txt = line_txt[pid_end:].lstrip()
        tid_end = line_txt.find(' ')
        tid = line_txt[:tid_end]
        line_txt = line_txt[tid_end:].lstrip()
        level_end = line_txt.find(' ')
        level = line_txt[:level_end]
        line_txt = line_txt[level_end:].lstrip()
        tag_end = line_txt.find(':')
        tag = line_txt[:tag_end].strip()
        message = line_txt[tag_end + 2:].replace('\t', "        ")
        csv_line = date + delimiter + time + delimiter + pid + delimiter + tid + delimiter + level + delimiter + tag + delimiter + message
        csv_file.write(csv_line.encode("utf-8"))
        csv_file.write('\n'.encode("utf-8"))

    log_file.close()
    csv_file.close()
    insert_end("Transform End." + '\n')
    lb = tk.Label(bottom_top_frame, text='Level', bg='blue', font=('Arial', 12), width=5)
    lb.grid(column=0, row=0)  # Label内容content区域放置位置，自动调节尺寸
    var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    var5 = tk.IntVar()
    var6 = tk.IntVar()
    c1 = tk.Checkbutton(bottom_top_frame, text='Verbose', variable=var1, onvalue=1, offvalue=0)
    c1.grid(column=1, row=0)
    c2 = tk.Checkbutton(bottom_top_frame, text='Debug', variable=var2, onvalue=1, offvalue=0)
    c2.grid(column=2, row=0)
    c3 = tk.Checkbutton(bottom_top_frame, text='Info', variable=var3, onvalue=1, offvalue=0)
    c3.grid(column=3, row=0)
    c4 = tk.Checkbutton(bottom_top_frame, text='Warn', variable=var4, onvalue=1, offvalue=0)
    c4.grid(column=4, row=0)
    c5 = tk.Checkbutton(bottom_top_frame, text='Error', variable=var5, onvalue=1, offvalue=0)
    c5.grid(column=5, row=0)
    c6 = tk.Checkbutton(bottom_top_frame, text='Assert', variable=var6, onvalue=1, offvalue=0)
    c6.grid(column=6, row=0)


# 实例化object，建立窗口window
window = tk.Tk()

# 给窗口的可视化起名字
window.title('My Window')

# 设定窗口的大小(长 * 宽)
window.geometry('1280x960')  # 这里的乘是小x


# 定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def insert_point(text):  # 在鼠标焦点处插入输入内容
    t.insert('insert', text)


def insert_end(text):  # 在文本框内容最后接着插入输入内容
    t.insert('end', text)


file_path = " "
frame = tk.Frame(window).pack()
top_frame = tk.Frame(frame)
top_frame.pack(side='top')
top_left_frame = tk.Frame(top_frame)
top_left_frame.pack(side='left')
top_right_frame = tk.Frame(top_frame)
top_right_frame.pack(side='right')
bottom_frame = tk.Frame(frame)
bottom_frame.pack(side='bottom')
bottom_top_frame = tk.Frame(bottom_frame)
bottom_top_frame.pack(side='top')
bottom_bottom_frame = tk.Frame(bottom_frame)
bottom_bottom_frame.pack(side='bottom')
# 创建并放置两个按钮分别触发两种情况
b1 = tk.Button(top_left_frame, text='Choose Log File', width=15,
               height=2, command=choose_log_file)
b1.pack(side='left')

# 创建并放置一个多行文本框text用以显示
t = tk.Text(bottom_bottom_frame, height=35, width=90, font=('Arial', 16))
t.grid(row=0, column=0)
y_scrollbar = tk.Scrollbar(bottom_bottom_frame)
y_scrollbar.grid(row=0, column=1, sticky=tkinter.N + tkinter.S)
t.config(yscrollcommand=y_scrollbar.set)
y_scrollbar.config(command=t.yview)

# # 并不需要水平方向上的滚动条
# x_scrollbar = tk.Scrollbar(bottom_bottom_frame, orient='horizontal')
# x_scrollbar.grid(row=1, column=0, sticky=tk.E + tk.W)
# t.config(xscrollcommand=x_scrollbar.set)
# x_scrollbar.config(command=t.xview)
# 主窗口循环显示
window.mainloop()
