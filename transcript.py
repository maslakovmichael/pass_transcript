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

class Translater:
    def __init__(self, root):
        self.entry_int = tk.Entry(root)


        self.lab_out1 = tk.Label(root)
        self.lab_out2 = tk.Label(root)

    def clearing(self):
        self.entry_int.delete(0, 'end')
        self.lab_out1.configure(text='поле для результата')
        self.lab_out2.configure(text='поле для результата')

    def past_text(self):
        pas = tk.Tk()
        pas.withdraw()
        clip = pas.clipboard_get()
        self.entry_int.delete(0, tk.END)
        self.entry_int.insert(0, clip)
        pas.update()
        pas.destroy()

    def copy_text1(self):
        cop = tk.Tk()
        cop.withdraw()
        cop.clipboard_clear()
        cop.clipboard_append(self.lab_out1['text'])
        cop.update()
        cop.destroy()

    def copy_test2(self):
        cop = tk.Tk()
        cop.withdraw()
        cop.clipboard_clear()
        cop.clipboard_append(self.lab_out2['text'])
        cop.update()
        cop.destroy()

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