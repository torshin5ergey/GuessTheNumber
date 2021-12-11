import tkinter as tk
from random import randrange
from PIL import Image, ImageTk
from tkinter.constants import LEFT, N, W

root = tk.Tk()
root.title('GuessTheNumber')
root.geometry('500x490')
root.resizable(width=False, height=False)

image_file = Image.open('source/gtn_logo.PNG')
resized_image = image_file.resize((472, 130))
image_logo = ImageTk.PhotoImage(resized_image)

lbl_logo = tk.Label(image=image_logo)
lbl_htp = tk.Label(root,
                        text='How to Play',
                        font='Arial 20')
lbl_htp_text = tk.Label(root,
                        text='The program will pick a secret number.\n'
                        'You guess what number is it.',
                        font='Arial 14',
                        justify=LEFT)
framelvl = tk.Frame(root)

lbl_lvleasy = tk.Label(framelvl,
                        text='Easy',
                        font='Arial 15',
                        foreground='#004d00',
                        width=15)
lbl_lvleasy_text = tk.Label(framelvl,
                        text='(1 to 10)',
                        font='Arial 12')
lbl_lvlnormal = tk.Label(framelvl,
                        text='Normal',
                        font='Arial 15',
                        foreground='#f48f00',
                        width=15)
lbl_lvlnormal_text = tk.Label(framelvl,
                        text='(1 to 100)',
                        font='Arial 12')                        
lbl_lvlhard = tk.Label(framelvl,
                        text='Hard',
                        font='Arial 15',
                        foreground='#7b000f',
                        width=15)
lbl_lvlhard_text = tk.Label(framelvl,
                        text='(-100 to 100)',
                        font='Arial 12')

picked_level = tk.IntVar()
picked_level.set(0)
rad_easy = tk.Radiobutton(framelvl, variable=picked_level, value=0)
rad_normal = tk.Radiobutton(framelvl, variable=picked_level, value=1)
rad_hard = tk.Radiobutton(framelvl, variable=picked_level, value=2)
btn_start = tk.Button(framelvl,
                        text='Start game',
                        font='Arial 20',
                        width=10, height=1)

lbl_logo.grid(row=0, column=0, sticky=N, columnspan=3)
lbl_htp.grid(row=1, column=0, sticky=N, columnspan=3, pady=(20, 0))
lbl_htp_text.grid(row=2, column=0, sticky=N, columnspan=3, pady=(0, 30))
framelvl.grid(row=3, column=0, columnspan=3)
btn_start.grid(row=4, column=0, columnspan=3, pady=(30))

lbl_lvleasy.grid(row=0, column=0)
lbl_lvlnormal.grid(row=0, column=1)
lbl_lvlhard.grid(row=0, column=2)
lbl_lvleasy_text.grid(row=1, column=0)
lbl_lvlnormal_text.grid(row=1, column=1)
lbl_lvlhard_text.grid(row=1, column=2)
rad_easy.grid(row=2, column=0)
rad_normal.grid(row=2, column=1)
rad_hard.grid(row=2, column=2)

root.mainloop()