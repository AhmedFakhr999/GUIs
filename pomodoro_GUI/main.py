from tkinter import * 
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
def start_count(count):
    # global reps 
    # reps+=1
    # if reps %8 == 0: 
    #     #here is the specific condition
    #     pass 
    # elif reps %2 == 0 : 
    #     pass
    # else: 
    #     pass
    label_tiemer.config(text='Work',fg=PINK)
    count_min=math.floor(count/60)
    count_sec=count%60
    
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0: 
        window.after(1000,start_count,count-1)

def rest_count(count):
    
    label_tiemer.config(text='Break',fg=RED)
    count_min=math.floor(count/60)
    count_sec=count%60
    
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0: 
        window.after(1000,rest_count,count-1)

def count_down():
    start_button.config(state="disabled")
    rest_count(5*60)
    
    
def reset_all():
    reset_button.config(state="normal")
    start_button.config(state="normal")
def reset_count():
    reset_button.config(state="disabled")
    start_count(1500)
window= Tk() 
window.title('Pomodoro App') 
window.configure(padx=100,pady=100,bg=YELLOW )
label_tiemer=Label(text='Timer',font=(FONT_NAME,50),fg=GREEN,background=YELLOW)

label_tiemer.grid(column=1,row=0)
#image 
canvas = Canvas(width=250,height=250,bg=YELLOW,highlightthickness=0) 
tomato_png=PhotoImage(file='tomato.png') 
canvas.create_image(100,112,image=tomato_png)
timer_text=canvas.create_text(100,112,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)

start_button=Button(text='Start',highlightthickness=0,command=reset_count)
start_button.grid(row=3,column=0) 

reset_button=Button(text='reset',highlightthickness=0,command=count_down)
reset_button.grid(row=3,column=3)

check_mark=Label(text='✔️',fg=GREEN)
check_mark.grid(column=1,row=3)






window.mainloop()
