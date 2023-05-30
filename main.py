from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repo=1
time=0
# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global repo
    window.after_cancel(time)
    canvas.itemconfig(timer, text="00:00")
    label.config(text="Timer")
    repo=1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repo
    global count11
    if repo%2==1:
        label.config(text="Study time")
        count_down(25*60)


    if repo%2==0:
        if repo%8==0:
            label.config(text="Enjoy for 20 minutes!",fg=PINK)
            count_down(20*60)
        else:
            label.config(text="Short break",fg=RED)
            count_down(5*60)
    repo+=1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global count11
    min=int(count/60)
    sec=int(count%60)
    if sec<10:
        sec=f"0{sec}"
    if min<10:
        min=f"0{min}"
    canvas.itemconfig(timer,text=f"{min}:{sec}")
    if count>0:
        global time
        time=window.after(1000,count_down,count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pamadoro")
window.config(padx=150,pady=50,bg=YELLOW)


label=Label(text="Timer",bg=YELLOW,font=(FONT_NAME,45,"bold"),fg=GREEN)
label.grid(row=0,column=1)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomata_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomata_img)
timer=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


button1=Button(text="Start",highlightthickness=0,bg=YELLOW,command=start_timer)
button1.grid(row=2,column=0)

button2=Button(text="Reset",highlightthickness=0,bg=YELLOW,command=reset_time)
button2.grid(row=2,column=2)

label1=Label(text="",bg=YELLOW,fg=GREEN)
label1.grid(row=3,column=1)


window.mainloop()