import tkinter as tk
import tkinter.filedialog
import pandas as pd
import os


# 创建文件选择对话框并将所选文件转换成csv文件
def choose_file():
    default_dir = r"文件路径"
    global file_path
    file_path = tk.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
    if len(file_path) > 0:
        print(file_path)
        text.insert('end', file_path + '\n')


def transform_to_csv():
    # 将log装换成csv格式
    global file_path, csv_path
    if len(file_path) == 0:
        return
    log_file = open(file_path, "r", encoding='UTF-8')
    file_name_start = file_path.rfind('/')
    file_name_end = file_path.rfind('.')
    csv_path = file_path[file_name_start + 1:file_name_end] + ".csv"
    csv_file = open(csv_path, 'wb')
    delimiter = ','
    csv_file.write("date,time,pid,tid,level,tag,message\n".encode("utf-8"))
    for line in log_file:
        line_txt = line.rstrip()
        # text.insert('end', line_txt + '\n')  # 将其显示到Text中
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
        message = line_txt[tag_end + 2:]
        csv_line = date + delimiter + time + delimiter + pid + delimiter + tid + delimiter + level + delimiter + \
                   tag + delimiter + message
        csv_file.write(csv_line.encode("utf-8"))
        csv_file.write('\n'.encode("utf-8"))

    log_file.close()
    csv_file.close()
    text.insert('end', "Transform End." + '\n')


def show_log():
    csv_file = open(csv_path, 'wb')


def show_button(frame):
    choose_button = tk.Button(frame, text='Choose Log File', width=15, height=2, command=choose_file)
    choose_button.grid(row=0, column=0)
    create_button = tk.Button(frame, text='Create Csv File', width=15, height=2, command=transform_to_csv)
    create_button.grid(row=0, column=1)
    show_log_button = tk.Button(frame, text='Show Log', width=15, height=2)
    show_log_button.grid(row=0, column=2)
    clear_button = tk.Button(frame, text='Clear Text', width=15, height=2)
    clear_button.grid(row=0, column=3)


def show_level_label(frame):
    level_label = tk.Label(frame, text='Level', bg='red', font=('Arial', 12), width=5)
    level_label.grid(row=0, column=0)
    var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    var5 = tk.IntVar()
    var6 = tk.IntVar()
    c1 = tk.Checkbutton(frame, text='Verbose', variable=var1, onvalue=1, offvalue=0)
    c1.grid(row=0, column=1)
    c2 = tk.Checkbutton(frame, text='Debug', variable=var2, onvalue=1, offvalue=0)
    c2.grid(row=0, column=2)
    c3 = tk.Checkbutton(frame, text='Info', variable=var3, onvalue=1, offvalue=0)
    c3.grid(row=0, column=3)
    c4 = tk.Checkbutton(frame, text='Warn', variable=var4, onvalue=1, offvalue=0)
    c4.grid(row=0, column=4)
    c5 = tk.Checkbutton(frame, text='Error', variable=var5, onvalue=1, offvalue=0)
    c5.grid(row=0, column=5)
    c6 = tk.Checkbutton(frame, text='Assert', variable=var6, onvalue=1, offvalue=0)
    c6.grid(row=0, column=6)


def show_message_tag(frame):
    type_label = tk.Label(frame, text='Message Type', bg='red', font=('Arial', 12), width=15)
    type_label.grid(row=1, column=0)
    var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    var5 = tk.IntVar()
    var6 = tk.IntVar()
    var7 = tk.IntVar()
    c1 = tk.Checkbutton(frame, text='Date', variable=var1, onvalue=1, offvalue=0)
    c1.grid(row=1, column=1)
    c2 = tk.Checkbutton(frame, text='Time', variable=var2, onvalue=1, offvalue=0)
    c2.grid(row=1, column=2)
    c3 = tk.Checkbutton(frame, text='PID', variable=var3, onvalue=1, offvalue=0)
    c3.grid(row=1, column=3)
    c4 = tk.Checkbutton(frame, text='TID', variable=var4, onvalue=1, offvalue=0)
    c4.grid(row=1, column=4)
    c5 = tk.Checkbutton(frame, text='Level', variable=var5, onvalue=1, offvalue=0)
    c5.grid(row=1, column=5)
    c6 = tk.Checkbutton(frame, text='TAG', variable=var6, onvalue=1, offvalue=0)
    c6.grid(row=1, column=6)
    c7 = tk.Checkbutton(frame, text='Message', variable=var7, onvalue=1, offvalue=0)
    c7.grid(row=1, column=7)


def show_flag_entry(frame):
    return 0


def show_log_text(frame):
    # 创建并放置一个多行文本框text用以显示
    text_widget = tk.Text(frame, height=35, width=90, font=('Arial', 16))
    text_widget.grid(row=0, column=0)
    return text_widget


def create_layout():
    frame1 = tk.Frame(root)
    frame1.pack()
    frame2 = tk.Frame(root)
    frame2.pack(side='top')
    frame3 = tk.Frame(root)
    frame3.pack(side='top')
    frame4 = tk.Frame(root)
    frame4.pack(side='top')
    return frame1, frame2, frame3, frame4


def display():
    frame1, frame2, frame3, frame4 = create_layout()
    show_button(frame1)
    show_level_label(frame2)
    show_message_tag(frame2)
    entry_widget = show_flag_entry(frame3)
    text_widget = show_log_text(frame4)
    return entry_widget, text_widget


# 实例化object，建立窗口window
root = tk.Tk()

# 给窗口的可视化起名字
root.title('My Window')

# 设定窗口的大小(长 * 宽) 乘是小x
root.geometry('1280x960')

file_path = ''
csv_path = ''
entry, text = display()

root.mainloop()
