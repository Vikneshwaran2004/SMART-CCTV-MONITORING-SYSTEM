import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion
from identify import maincall

window = tk.Tk()
window.title("SMART CCTV")
window.iconphoto(False, tk.PhotoImage(file='g.png'))
window.geometry('1300x800')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="𝐒𝐌𝐀𝐑𝐓 𝐂𝐂𝐓𝐕 𝐌𝐎𝐍𝐈𝐓𝐎𝐑𝐈𝐍𝐆 𝐒𝐘𝐒𝐓𝐄𝐌", fg='blue')
label_font = font.Font(size=40, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('icons/jj.png')
icon = icon.resize((200,200), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/cc.png')
btn1_image = btn1_image.resize((80,80), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/re.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/ex.png')
btn5_image = btn5_image.resize((150,80), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/no.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('icons/in.png')
btn6_image = btn6_image.resize((50,50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/gg.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn7_image = Image.open('icons/id.png')
btn7_image = btn7_image.resize((50,50), Image.ANTIALIAS)
btn7_image = ImageTk.PhotoImage(btn7_image)


# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='𝚂𝚗𝚊𝚙 𝙶𝚞𝚊𝚛𝚍', height=100, width=270, fg='green',command = find_motion, bg='lavender',image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10))

btn2 = tk.Button(frame1, text='𝚉𝚘𝚗𝚎 𝙰𝚕𝚎𝚛𝚝', height=100, width=270, fg='green', bg='lavender',command=rect_noise, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))

btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, text='𝙻𝚘𝚌𝚔 𝙵𝚛𝚊𝚖𝚎', height=100, width=270, fg='green',bg='lavender', command=noise, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=5, pady=(20,10))

btn4 = tk.Button(frame1, text='𝚁𝚎𝚌𝚘𝚛𝚍', height=100, width=270, fg='green', command=record, bg='lavender',image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=3)


btn6 = tk.Button(frame1, text='𝙸𝚗 𝙾𝚞𝚝', height=100, width=270, fg='green', command=in_out,bg='lavender', image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=5, pady=(20,10), column=2)

btn5 = tk.Button(frame1, height=120, width=200, fg='red', command=window.quit, image=btn5_image,bg='lavender')
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20,10), column=2)

btn7 = tk.Button(frame1, text="𝙸𝚍𝚎𝚗𝚝𝚒𝚏𝚢", fg="green",command=maincall, compound='left', image=btn7_image, height=100, width=270,bg='lavender')
btn7['font'] = btn_font
btn7.grid(row=3, column=2, pady=(20,10))

frame1.pack()
window.mainloop()


