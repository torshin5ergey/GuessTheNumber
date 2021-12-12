import tkinter as tk
from PIL import Image, ImageTk
from tkinter.constants import LEFT, N, W


def new_play_window():
    level_window.destroy()
    play_window = tk.Toplevel(root)
    play_window.title('GuessTheNumber')
    play_window.geometry('500x500')
    play_window.resizable(width=False, height=False)


root = tk.Tk()
root.withdraw()

level_window = tk.Tk()
image_icon = tk.PhotoImage(file='source/gtn_icon.png')
level_window.iconphoto(False, image_icon)
level_window.title('GuessTheNumber')
level_window.geometry('500x520')
level_window.resizable(width=False, height=False)

image_file = Image.open('source/gtn_logo.png')
resized_image = image_file.resize((472, 130))
image_logo = ImageTk.PhotoImage(resized_image)

lbl_logo = tk.Label(image=image_logo)
lbl_htp = tk.Label(level_window,
                   text='How to Play',
                   font='Arial 20')
lbl_htp_text = tk.Label(level_window,
                        text='The program will pick a secret number.\n'
                             'You guess what number is it.\n'
                             '\nPick a difficulty level and press "Start"',
                        font='Arial 14',
                        justify=LEFT)
framelvl = tk.Frame(level_window)

lbl_lvleasy = tk.Label(framelvl,
                       text='Easy',
                       font='Arial 15',
                       foreground='#004d00',
                       width=15)
lbl_lvleasy_text = tk.Label(framelvl,
                            text='(1 to 10)',
                            font='Arial 10')
lbl_lvlnormal = tk.Label(framelvl,
                         text='Normal',
                         font='Arial 15',
                         foreground='#f48f00',
                         width=15)
lbl_lvlnormal_text = tk.Label(framelvl,
                              text='(1 to 100)',
                              font='Arial 10')
lbl_lvlhard = tk.Label(framelvl,
                       text='Hard',
                       font='Arial 15',
                       foreground='#7b000f',
                       width=15)
lbl_lvlhard_text = tk.Label(framelvl,
                            text='(-100 to 100)',
                            font='Arial 10')

picked_level = tk.IntVar()
picked_level.set(0)
rad_easy = tk.Radiobutton(framelvl, variable=picked_level, value=0)
rad_normal = tk.Radiobutton(framelvl, variable=picked_level, value=1)
rad_hard = tk.Radiobutton(framelvl, variable=picked_level, value=2)
btn_start = tk.Button(framelvl,
                      text='Start game',
                      font='Arial 20',
                      width=10, height=1,
                      command=new_play_window)

lbl_logo.grid(row=0, column=0, sticky=N, columnspan=3)
lbl_htp.grid(row=1, column=0, sticky=N, columnspan=3, pady=(20, 0))
lbl_htp_text.grid(row=2, column=0, sticky=N, columnspan=3, pady=(0, 30))
framelvl.grid(row=3, column=0, columnspan=3)
btn_start.grid(row=4, column=0, columnspan=3, pady=30)

lbl_lvleasy.grid(row=0, column=0)
lbl_lvlnormal.grid(row=0, column=1)
lbl_lvlhard.grid(row=0, column=2)
lbl_lvleasy_text.grid(row=1, column=0)
lbl_lvlnormal_text.grid(row=1, column=1)
lbl_lvlhard_text.grid(row=1, column=2)
rad_easy.grid(row=2, column=0)
rad_normal.grid(row=2, column=1)
rad_hard.grid(row=2, column=2)

level_window.mainloop()
