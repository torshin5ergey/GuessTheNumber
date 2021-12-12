import tkinter as tk
from PIL import Image, ImageTk
from tkinter.constants import LEFT, N, W, TOP, Y, X
from random import randrange


def change_to_game():
    frame_playgame.pack()
    frame_pickLvL.forget()


root = tk.Tk()
root.iconbitmap('source/gtn_icon.ico')
root.title('GuessTheNumber')
root.geometry('500x520')
root.resizable(width=False, height=False)

image_file = Image.open('source/gtn_logo.png')
resized_image = image_file.resize((472, 130))
image_logo = ImageTk.PhotoImage(resized_image)

lbl_logo = tk.Label(image=image_logo)
lbl_logo.pack(expand=1)

lbl_htp = tk.Label(root, text='The program will pick a secret number. You guess '
                              'what number is it.\n'
                              'Pick a difficulty and press "Start".',
                   font='Arial 10',
                   justify=LEFT)
lbl_htp.pack(expand=Y)

frame_pickLvL = tk.Frame(root)
frame_pickLvL.pack(expand=1, fill=Y)
frame_row1 = tk.Frame(frame_pickLvL)
frame_row1.pack(fill=Y)
frame_row2 = tk.Frame(frame_pickLvL)
frame_row2.pack(fill=Y)
frame_row3 = tk.Frame(frame_pickLvL)
frame_row3.pack(fill=Y)
diff_level = tk.IntVar()
diff_level.set(0)
rad_easy = tk.Radiobutton(frame_row1,
                          text='Easy',
                          font='Arial 15',
                          foreground='#004d00',
                          width=8,
                          variable=diff_level,
                          value=0,
                          indicator=False)
rad_easy.pack(side=LEFT, pady=5)
rad_normal = tk.Radiobutton(frame_row2,
                            text='Normal',
                            font='Arial 15',
                            foreground='#f48f00',
                            width=8,
                            variable=diff_level,
                            value=1,
                            indicator=False)
rad_normal.pack(side=LEFT, pady=5)
rad_hard = tk.Radiobutton(frame_row3,
                          text='Hard',
                          font='Arial 15',
                          foreground='#7b000f',
                          width=8,
                          variable=diff_level,
                          value=2,
                          indicator=False)
rad_hard.pack(side=LEFT, pady=5)

lbl_easy_text = tk.Label(frame_row1,
                         text='(0 to 10)',
                         font='Arial 10',
                         width=10)
lbl_easy_text.pack(pady=5, expand=1)

lbl_normal_text = tk.Label(frame_row2,
                           text='(0 to 100)',
                           font='Arial 10',
                           width=10)
lbl_normal_text.pack(pady=5, expand=1)

lbl_hard_text = tk.Label(frame_row3,
                         text='(-100 to 100)',
                         font='Arial 10',
                         width=10)
lbl_hard_text.pack(pady=5, expand=1)

btn_start = tk.Button(frame_pickLvL,
                      text='Start',
                      font='Arial 20',
                      width=10, height=1,
                      command=change_to_game)
btn_start.pack(pady=(20, 0))

frame_playgame = tk.Frame(root)

if diff_level == 0:
    low_num, high_num = 1, 10
    goal_num = randrange(low_num, high_num)
    turns_cap, turns_left = 6, 5
elif diff_level == 1:
    low_num, high_num = 1, 100
    goal_num = randrange(low_num, high_num)
    turns_cap, turns_left = 8, 7
elif diff_level == 2:
    low_num, high_num = -100, 100
    goal_num = randrange(low_num, high_num)
    turns_cap, turns_left = 11, 10

print(diff_level)

lbl_game_tips = tk.Label(frame_playgame,
                         text='Pick a number between')
lbl_game_tips.pack()

root.mainloop()
