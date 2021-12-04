import tkinter
import os
import random
from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import askopenfile


pre_root = Tk()

pre_root.overrideredirect(True)
pre_root.configure(bg="#ac97d1")

app_width = 350
app_height = 165

screen_width = pre_root.winfo_screenwidth()
screen_height = pre_root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y= (screen_height / 2) - (app_height / 2)

pre_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

space1 = Label(pre_root, text="                                                                                                          ", bg="#ac97d1").grid(row=0, column=0)

exit = Button(pre_root, text="❌", bg="#ac97d1", command= lambda: pre_root.destroy())
exit.grid(row=0, column=1)

title = Label(pre_root, text="Activation code", font=('Arial', 15), bg="#ac97d1").grid(row=1, column=0)


def newone():
    pre_root.destroy()
    root = Tk()

    root.title("HIDE FILE")
    root.configure(bg="#6259c9")

    app_width = 350
    app_height = 165

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y= (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    #1e8feb



    # indroduction and steps

    en = Entry(root, width=40, font=('Arail'))
    en.pack()

    def clip():
        # past the text in the clipboard
        text = root.clipboard_get()
        en.insert(0, text)

    def openfile():
        file = askopenfile(mode ='r', filetypes =[('All files', '*')]) 
        if file is not None: 
            content = file.name 
            en.insert(0, content)


    b= Menu(root, tearoff = 0) 
    b.add_command(label ="past", command= clip)
    b.add_command(label ="choose file", command= openfile)  


    
    def do_popup(event): 
        try: 
            b.tk_popup(event.x_root, event.y_root)
        finally: 
            b.grab_release() 
    
    en.bind("<Button-3>", do_popup) 



    def hide():
        global name
        name = en.get()
        if name == "":
            messagebox.showinfo("No file", "Type a file name above to hide                                                  Tips to follow (make sure it is lower case)                                  (its should not have space)")
        else:
            os.system('cmd /c "attrib +h +s +r "'+ name)

    def show():
        global name
        name = en.get()
        if name == "":
            messagebox.showinfo("No file", "Type a file name above to hide                                                  Tips to follow (make sure it is lower case)                                  (its should not have space)")
        else:
            os.system('cmd /c "attrib -h -s -r "'+ name)

    bu = Button(root, text="HIDE", width=20, padx=20, font=(15), command=hide, bg='#1e8feb').pack()
    bu2 = Button(root, text="RETRIVE", width=20, padx=20, font=(15), command= show, bg='#1e8feb').pack(pady=20)


    def open_win():
        # CREAT A NEW WINDOW
        brand_new_win = Tk()
        brand_new_win.title('INFO')

        brand_new_win.configure(bg="#6259c9")

        info2 = Label(brand_new_win, text="Hide file real quick", bg="#6259c9", fg="white").pack()
        info3 = Label(brand_new_win, text="Follow the bellow steps", bg="#6259c9", fg="white").pack()
        info4 = Label(brand_new_win, text="1.place the file in the same", font=(20), bg="#6259c9", fg="white").pack()
        info5 = Label(brand_new_win, text="directery as the application", font=(20), bg="#6259c9", fg="white").pack()
        info6 = Label(brand_new_win, text="2.Put the file name in the white box ", font=(20), bg="#6259c9", fg="white").pack()

        info8 = Label(brand_new_win, text="Created by : Aswanth", font=(20), bg="#6259c9", fg="white").pack()

        info7 = Label(brand_new_win, text="Version - 1.7", font=('Courier', 10)).pack()



    info_button = Button(root, text="INFO", font=('Arial', 15), command=open_win, bg='blue')
    info_button.pack()

    root.mainloop()


activation_codes = ["a6d3p90g6hide456yt", "t9kl56rtx5g7file89hg7rtyup", "guxp85gh52gvhf256fvh"]

current_code = random.choice(activation_codes)
print(current_code)

box = Entry(pre_root, width=40)
box.grid(row=2, column=0)

def checkcode():
    if box.get() == current_code:
        newone()
        
    else:
        messagebox.showerror("code E", "The Activation code is incorrect")

conf = Button(pre_root, text="Enter", bg="blue", fg="white", width=10, command= checkcode)
conf.grid(row=3, column=0, pady=20)

#open_up = Button(pre_root, text="open", command= ).pack()

pre_root.mainloop()