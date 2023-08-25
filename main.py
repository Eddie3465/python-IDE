from tkinter import *
import  tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title('ide python')
compiler.geometry("1280x720")
compiler.configure(bg="#2E2B2B")
compiler.resizable(False,False)
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path  = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

def save_as():
    if file_path == '':
        path  = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Pleace save you code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.delete('1.0', END)

    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

    code_output.place(x=0, y=400, width=1280, height=420)

    #boton = Button(text="¡X!")
    #boton.place(x=50, y=50)


def close():
    print('ocultar')
    code_output.place(x=0, y=800, width=1280, height=420)
    pass


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File',menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0,)
run_bar.add_command(label='Run', command=run)
run_bar.add_command(label='Close', command=close)
menu_bar.add_cascade(label='Run',menu=run_bar)

compiler.config(menu=menu_bar)

#entrada
editor = Text(bg="#2E2B2B",fg="lightgreen")
editor.place(width=1280,height=720)

####salida
code_output = Text(compiler, height=10,bg="#323846",fg="lightgreen")
#code_output.place(x=0, y=400, width=1280, height=420)


compiler.mainloop()