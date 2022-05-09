import tkinter as tk
import tkinter.filedialog as fd

filetypes = (("Текстовый файл", "*.docx"),)
filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
if filename:
    print(filename)
