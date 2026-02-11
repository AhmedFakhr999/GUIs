from tkinter import *
from tkinter import messagebox
import random as rndm
import pandas as pd



BACKGROUND_COLOR = "#B1DDC6"





current_card={}
to_learn={} 

def start_project():
    global to_learn
    try : 
        data=pd.read_csv('data/words_to_learn.csv') 
    except (FileNotFoundError, pd.errors.EmptyDataError):
        original_data=pd.read_csv('data/french_words.csv')
        to_learn=original_data.to_dict(orient='records')
    else:
        to_learn=data.to_dict(orient='records')
    
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    try:
        
        current_card=rndm.choice(to_learn) 
    except :
        messagebox.showinfo(title='Alert',message="you have reached maximum words , the app will restart automatically")
        start_project()
    else:
        
        the_word=current_card["French"]
        canvas.itemconfig(title_canvas,text="French", fill="black")
        canvas.itemconfig(word_canvas,text=the_word, fill="black")
        canvas.itemconfig(card_background, image=card_front_image)
        flip_timer= window.after(4000,func=flip_card)
    
def flip_card():
    canvas.itemconfig(title_canvas,text='English',fill="white")
    canvas.itemconfig(word_canvas,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_image)
    
    
def is_known():
    to_learn.remove(current_card) 
    data=pd.DataFrame(to_learn) 
    data.to_csv("data/words_to_learn.csv",index=False)
    if len(data)==0:
        messagebox.showinfo(title='NOTIFY',message='you have learned all words available, Congratulations 🥳')
    next_card()




#------------UI Setup-----------------
start_project()
window=Tk()
window.title('Flash Card')
window.config(padx=50,pady=50,width=500,height=500,background=BACKGROUND_COLOR)
flip_timer=window.after(4000,func=flip_card)
card_front_image=PhotoImage(file='images/card_front.png')
card_back_image=PhotoImage(file='images/card_back.png')
canvas=Canvas(width=800,height=525)
card_background=canvas.create_image(400,263,image=card_front_image)
title_canvas= canvas.create_text(400,150,text="Title",font=('Ariel',40,'italic'))
word_canvas= canvas.create_text(400,263,text="Word",font=('Ariel',60,'bold'))

canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=1,column=1,columnspan=2)

x_image=PhotoImage(file="images/wrong.png")
r_image=PhotoImage(file="images/right.png")


x_button=Button(image=x_image,highlightthickness=0,command=next_card)
r_button=Button(image=r_image,highlightthickness=0,command=is_known)

x_button.grid(row=2,column=1)
r_button.grid(row=2,column=2)

next_card()

window.mainloop()
