from tkinter import *  

window=Tk()
window.title('Miles to Km')
window.minsize(width=100,height=100)
window.columnconfigure(10,weight=1)
window.rowconfigure(10,weight=1)


entry_miles=Entry(width=10, background='gray', border=2, relief="solid")
entry_miles.grid(column=10,row=0,padx=(200,0))

label= Label(text='Miles')
label.grid(row=0,column=11,padx=(0,200))

def calculate_km(miles_string):
    miles=float(miles_string)
    value=miles* 1.60934
    value_label.config(text=value)

exit_button=Button(text='Exit',command=window.destroy)
exit_button.grid(column=300,row=300)

equal_to_label=Label(text='Is Equal to')
equal_to_label.grid(column=5,row=1)

value_label=Label(text='0')
value_label.grid(column=10,row=1,padx=(150,0))

km_label=Label(text='KM')
km_label.grid(column=10,row=1,padx=(350,0))

calculat_button=Button(text='Calulate',command=lambda:calculate_km(entry_miles.get()))
calculat_button.grid(column=10,row=10)


window.mainloop()