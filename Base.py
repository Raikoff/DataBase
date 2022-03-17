# 2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# под форматами понимаем структуру файлов, например:
# - в файле на одной строке хранится одна часть записи, пустая строка - разделитель
#
# Фамилия_1
# Имя_1
# Телефон_1
# Описание_1
#
# Фамилия_2
# Имя_2
# Телефон_2
# Описание_2
#
# и т.д.
# - в файле на одной строке хранится все записи, символ разделитель - ;
# Фамилия_1,Имя_1,Телефон_1,Описание_1
# Фамилия_2,Имя_2,Телефон_2,Описание_2
#
# Использовать CSV(Если есть желание, можно попробовать возможность чтения XML)



import tkinter as tk


window = tk.Tk()                              # интерфейс
window.title('Справочник')

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

surname = tk.Label(master=frm_form,text="Фамилия: ")
en_sur = tk.Entry(master=frm_form,width=50)
surname.grid(row=0, column=0, sticky="e")
en_sur.grid(row=0, column=1)

name = tk.Label(master=frm_form,text="Имя: ")
en_name = tk.Entry(master=frm_form,width=50)
name.grid(row=1, column=0, sticky="e")
en_name.grid(row=1, column=1)

tel = tk.Label(master=frm_form,text="Телефон +: ")
en_tel = tk.Entry(master=frm_form,width=50)
tel.grid(row=2, column=0, sticky="e")
en_tel.grid(row=2, column=1)

com = tk.Label(master=frm_form,text="Описание: ")
en_com = tk.Entry(master=frm_form,width=50)
com.grid(row=3, column=0, sticky="e")
en_com.grid(row=3, column=1)

frm_enter = tk.Frame()
frm_enter.pack()

text_box = tk.Text()
text_box.pack()

frm_con = tk.Frame()
frm_con.pack()

btn_sav = tk.Button(master=frm_enter,text="Сохранить")
btn_sav.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_second = tk.Button(master=frm_con,text="Формат №2")
btn_second.pack(side=tk.RIGHT, padx=10)

btn_first = tk.Button(master=frm_con,text="Формат №1")
btn_first.pack(side=tk.RIGHT, padx=10, ipadx=10)

# if en_sur.isalpha() == False:
#     exit()
# if en_name.isalpha() == False:
#     exit()
#
# if en_tel.isnumeric() == False:
#     exit()

def inputUsers(en_sur,en_name,en_tel,en_com):
    list = [en_sur,en_name,en_tel,en_com]
    list1 = ' '.join(map(str,list))
    return list1

btn_sav.bind('<Button-1>', lambda event: inputUsers(en_sur,en_name,en_tel,en_com))

def inputUsers2(en_sur,en_name,en_tel,en_com):

    list = [en_sur,en_name,en_tel,en_com]
    list1 = '\n'.join(map(str,list))
    return list1

btn_sav.bind('<Button-1>',lambda event: inputUsers2(en_sur,en_name,en_tel,en_com))


with open('file1.txt', 'a') as data:
    data.writelines(inputUsers(en_sur,en_name,en_tel,en_com))
    data.write('\n')

with open('file2.txt', 'a') as data:
    data.writelines('\n')
    data.write(inputUsers2(en_sur,en_name,en_tel,en_com))

# def click_format():                                           # зависает программа
#     while format != btn_first or format != btn_second:
#         if format == btn_first:
#             path = 'file1.txt'
#             data = open(path, 'r')
#             for line in data:
#                 text_box.get(line)
#         elif format == btn_second:
#             path = 'file2.txt'
#             data = open(path, 'r')
#             for line in data:
#                 text_box.get(line)

# btn_second.bind('<Button-1>',lambda event: click_format())

# btn_first.bind('<Button-1>',lambda event: click_format())

window.mainloop()