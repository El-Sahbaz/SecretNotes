from tkinter import *
from tkinter import messagebox

def save_and_encrypt_notes():
    title = title_entry.get()
    message = input_text.get("1.0",END)
    master_secret = master_secret_input.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error!",message="Please enter all information.")
    else:
        #encryption
        try:
            with open("mysecret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message}")



#UI

FONT = ("Verdana",13,"italic")
window = Tk()
window.title("Secret Notes")
window.config(padx=30,pady=30)

photo = PhotoImage(file = "images.png")
photo_label = Label(image=photo)
photo_label.pack()

#canvas = Canvas(height=200,width=200)
#canvas.create_image(100,100,image=photo)
#canvas.pack()

title_info_label = Label(text="Enter your title",font=FONT)
title_info_label.pack()

title_entry = Entry(width=30)
title_entry.pack()

input_info_label = Label(text="Enter your secret",font=FONT)
input_info_label.pack()

input_text = Text(width=50,height=15)
input_text.pack()

master_secret_label = Label(text="Enter master key",font=FONT)
master_secret_label.pack()

master_secret_input = Entry(width=35)
master_secret_input.pack()

save_button = Button(text="Save & Encrypt",command=save_and_encrypt_notes)
save_button.pack()

decrypt_button = Button(text="Decrypt")
decrypt_button.pack()

window.mainloop()










