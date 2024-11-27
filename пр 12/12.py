import requests
import json
from tkinter import *
import tkinter as tk
from pprint import pprint

window = Tk()
window.geometry('400x100')
window.title('Шаганов Кирилл Александрович')

e = Entry(window,width=15)
e.pack()#anchor - определяет, как текст, виджет будет выровнен внутри контейнера
l = Label(window,text='Введите никнейм(имя) пользователя')
l.pack()

def f():
    a = e.get()
    username = a 
    url = f"https://api.github.com/users/{username}"
    data = {}
    user_data = requests.get(url).json()
    pprint(user_data)#увидеть что происходить в вычеслениях
    kkay = [ 'company' ,'created_at' ,'email' ,'id' ,'name' , 'url']
    for i in kkay:# перебор  ключей
        data[i] = user_data[i] #добавление значений в словаррь
    with open('jsondata_file.json','w') as rr:
        json.dump(data, rr ,indent = 4)# ident - кол-во отступов во время сериализации
bt=Button(window,text = "Приступим",command=f,width=45)
bt.pack()
window.mainloop()