from tkinter import *
import tkinter.filedialog as fd
import re
import tkinter.messagebox as mb
tk=Tk()
tk.title('Генератор вариантов')

canvas = Canvas(tk, width = 600, height = 500)
canvas.pack()
fileDad=""
def fileFam():
    global filename
    filetypes = (("Текстовый файл", "*.docx"), )
    file = fd.askopenfilename(title="Открыть файл", initialdir="/", filetype=filetypes)
    if file:
        print(file)
        filename=file
        lblFam = Label(text = filename, font=('Times', 11))
        lblFam.place(x=20, y=60, anchor = 'nw')
def fileGenDir():
    global fileDad
    file = fd.askdirectory(title="Открыть папку", initialdir="/" )
    if file:
        print(file)
        fileDad=file+'/'

#Выбор файла с фамилиями
btn1 = Button(text = "Выбрать файл с фамилиями", padx = 5,
              pady = 5,background='#B0E0E6',
              activebackground='#E6E6FA', font=('Times', 11),
              command = fileFam)
btn1.place(x=20,y=20, anchor = 'nw')
#учесть вывод ошибки если файл не выбран!!

#Выбор папки для сгенерированного файла
lblDirGenering = Label(text = "Выберите папку для хранения документа",
                        font=('Times', 12))
lblDirGenering.place(x=250,y=100,anchor = 'nw')
btn2 = Button(text='Выбрать',padx = 5,
              pady = 3,background='#B0E0E6',
              activebackground='#E6E6FA',
              font=('Times',11), command = fileGenDir)
btn2.place(x=330, y=130,anchor='nw')
#Поле ввода названия файла
name= StringVar()
lblInputName = Label(text = 'Введите название файла', font=('Times',13))
lblInputName.place(x=20,y=100,anchor='nw')
txtName=Entry(textvariable = name)
txtName.place(x=35,y=130,anchor='nw')


#Поле ввода номеров
lblTasks = Label(text = "Введите номера задач", font=('Times',12))
lblTasks.place(x=20,y=180,anchor= 'nw')
number = StringVar()
txtNumberTasks = Entry(textvariable = number)
txtNumberTasks.place(x=35,y=205,anchor='nw')

#в итоговую кнопку добавить функции преобразования строки -> вызов ошибки в случае некорректных данных    
def numTasks(s):
    pattern = r'^[0-9,\-\s]+$'
    is_valid = re.match(pattern,s)
    numberList=[]
    if is_valid:
        sTire = s.split('-')
        for i in range(len(sTire)-1):
            s1=sTire[i].split(',')
            s2=sTire[i+1].split(',')
            for j in range(len(s1)):
                numberList.append(int(s1[j]))
            for j in range(int(s1[len(s1)-1])+1,int(s2[0]),1):
                numberList.append(j)
            if i+1==len(sTire)-1:
                for j in range(len(s2)):
                    numberList.append(int(s2[j]))
        return numberList
    else:
        msg = "Ввод номеров может состоять только из записанных по возрастанию цифр, запятых и тире!"
        mb.showerror("Ошибка",msg)
        return []


#чтобы было время ввести название файла генерим чисто для проверки потом уберем
#можно потом эту функции преобразовать в итоговую
def pokaz():
    #учесть вывод ошибки, если не введено название файла
    #учесть ошибки если такой файл уже существует
    
    global fileGen
    fileGen = fileDad+name.get()+'.docx'
    lblGdePruf = Label(text=fileGen,font=('Times',11))
    lblGdePruf.place(x=20,y=190,anchor='nw')

#btnpp=Button(text = 'Показать', command=pokaz)
#btnpp.place(x=20,y=160, anchor='nw')


for i in range(len(listNumber)):
            m+=1        
            documAns.add_paragraph(str(listNumber[i])+")  "+str(answer[listNumber[i]]))

    


