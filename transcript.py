#!/bin/python3

import tkinter as tk

letters_dict_1 = {'а': 'f', 'б': ',', 'в': 'd', 'г': 'u', 'д': 'l', 'е': 't', 'ё': '`', 'ж': ';',
                'з': 'p', 'и': 'b', 'й': 'q', 'к': 'r', 'л': 'k', 'м': 'v', 'н': 'y',
                'о': 'j', 'п': 'g', 'р': 'h', 'с': 'c', 'т': 'n', 'у': 'e', 'ф': 'a',
                'х': '[', 'ц': 'w', 'ч': 'x', 'ш': 'i', 'щ': 'o', 'ь': 'm', 'ы': 's',
                'ъ': ']', 'э': "'", 'ю': '.', 'я': 'z', 'А': 'F', 'Б': '<', 'В': 'D',
                'Г': 'U', 'Д': 'L', 'Е': 'T', 'Ё': '~', 'Ж': ':', 'З': 'P', 'И': 'B', 'Й': 'Q',
                'К': 'R', 'Л': 'K', 'М': 'V', 'Н': 'Y', 'О': 'J', 'П': 'G', 'Р': 'H',
                'С': 'C', 'Т': 'N', 'У': 'E', 'Ф': 'A', 'Х': '{', 'Ц': 'W', 'Ч': 'X',
                'Ш': 'I', 'Щ': 'O', 'Ь': 'M', 'Ы': 'S', 'Ъ': '}', 'Э': '"', 'Ю': '>', 'Я': 'Z'}

letters_dict_2 = {'а': 'f', 'б': ',', 'в': 'd', 'г': 'u', 'д': 'l', 'е': 't', 'ё': '`', 'ж': ';',
                'з': 'p', 'и': 'b', 'й': 'q', 'к': 'r', 'л': 'k', 'м': 'v', 'н': 'y',
                'о': 'j', 'п': 'g', 'р': 'h', 'с': 'c', 'т': 'n', 'у': 'e', 'ф': 'a',
                'х': '[', 'ц': 'w', 'ч': 'x', 'ш': 'i', 'щ': 'o', 'ь': 'm', 'ы': 's',
                'ъ': ']', 'э': "'", 'ю': '.', 'я': 'z', 'А': 'F', 'Б': ',', 'В': 'D',
                'Г': 'U', 'Д': 'L', 'Е': 'T', 'Ё': '`', 'Ж': ';', 'З': 'P', 'И': 'B', 'Й': 'Q',
                'К': 'R', 'Л': 'K', 'М': 'V', 'Н': 'Y', 'О': 'J', 'П': 'G', 'Р': 'H',
                'С': 'C', 'Т': 'N', 'У': 'E', 'Ф': 'A', 'Х': '[', 'Ц': 'W', 'Ч': 'X',
                'Ш': 'I', 'Щ': 'O', 'Ь': 'M', 'Ы': 'S', 'Ъ': ']', 'Э': "'", 'Ю': '.', 'Я': 'Z'}

C = '#c7bcf3'
B = 2

'''Класс Translater - определяет компоненты визуального интерфейса, их свойства и параметры'''
class Translater:
    def __init__(self, root):
        self.lab_text_int = tk.Label(root, text='Password: ')
        self.entry_int = tk.Entry(root, width=55, font=15)
        self.btn_paste_in = tk.Button(root, text='Paste', bd=B, bg=C, command=self.past_text)
        self.lab_text_int.grid(row=0, column=0, sticky='we')
        self.entry_int.grid(row=0, column=1, sticky='we')
        self.btn_paste_in.grid(row=0, column=2, sticky='we')

        self.btn_apply = tk.Button(root, text='Apply', bd=B, bg=C, command=self.translate)
        self.btn_apply.grid(row=1, column=1, sticky='we')

        self.lab_text_out1 = tk.Label(root, text='Transcription 1: ')
        self.lab_out1 = tk.Label(root, text='поле для результата', width=55, font=15)
        self.btn_copy_out1 = tk.Button(root, text='Copy 1', bd=B, bg=C, command=self.copy_text1)
        self.lab_text_out1.grid(row=2, column=0)
        self.lab_out1.grid(row=2, column=1)
        self.btn_copy_out1.grid(row=2, column=2)

        self.lab_text_out2 = tk.Label(root, text='Transcription 2: ')
        self.lab_out2 = tk.Label(root, text='поле для результата', width=55, font=15)
        self.btn_copy_out2 = tk.Button(root, text='Copy 2', bd=B, bg=C, command=self.copy_text2)
        self.lab_text_out2.grid(row=3, column=0)
        self.lab_out2.grid(row=3, column=1)
        self.btn_copy_out2.grid(row=3, column=2)

        self.btn_clear = tk.Button(root, text='Clear', bd=B, bg=C, command=self.clearing)
        self.btn_clear.grid(row=4, column=1, sticky='we')

# Метод clearing() для очистки полей от текста
    def clearing(self):
        self.entry_int.delete(0, 'end')
        self.lab_out1.configure(text='поле для результата')
        self.lab_out2.configure(text='поле для результата')

# Метод past_text() для вставки текста в поле self.entry_int из буфера обмена
    def past_text(self):
        pas = tk.Tk()
        pas.withdraw()
        clip = pas.clipboard_get()       # получаем содержимое буфера обмена в обьект clip
        self.entry_int.delete(0, tk.END)
        self.entry_int.insert(0, clip)   # помещаем содержимое в окно
        pas.update()
        pas.destroy()

# Метод copy_text1() для копирования текста из поля self.lab_out1 в буфер обмена
    def copy_text1(self):
        cop = tk.Tk()
        cop.withdraw()
        cop.clipboard_clear()
        cop.clipboard_append(self.lab_out1['text'])
        cop.update()
        cop.destroy()

# Метод copy_text2() для копирования текста из поля self.lab_out2 в буфер обмена
    def copy_text2(self):
        cop = tk.Tk()
        cop.withdraw()
        cop.clipboard_clear()
        cop.clipboard_append(self.lab_out2['text'])
        cop.update()
        cop.destroy()

# Метод translate() для совершения транскрипирования текста по нажатию кнопки Apply
    def translate(self):
        st = self.entry_int.get()
        s1 = ''
        s2 = ''
        for i in st:
            if i in letters_dict_1:
                s1 += letters_dict_1[i]
                s2 += letters_dict_2[i]
            else:
                s1 += i
                s2 += i
        self.lab_out1['text'] = s1
        self.lab_out2['text'] = s2

if __name__=='__main__':
    root = tk.Tk()
    root.title('Транскрипция на Английскую роскладку')
    image = tk.PhotoImage(file='icon_11.png')
    root.iconphoto(True, image)
    t = Translater(root)
    root.mainloop()