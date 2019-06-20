######################################
############ CHNAGE COLOR ############
######################################
import tkinter

def change_color():                          
    window.configure(background="red")        

window = tkinter.Tk()
window.geometry("800x200")
window.title("My first GUI")
window.configure(background="grey")

red = tkinter.Button(window, text="Red", bg="red", command=change_color)       
red.pack()                                                   
yellow = tkinter.Button(window, text="Yellow", bg="yellow")
yellow.pack()
green = tkinter.Button(window, text="Green", bg="green")
green.pack()
textbox = tkinter.Entry(window)              
textbox.pack()                                        
colorlabel = tkinter.Label(window, height="10", width="10")         
colorlabel.pack()             

window.mainloop()

######################################
############ COUNTDOWN ###############
######################################
import tkinter

def countdown():                                     
    countlabel.configure(background="white")         
    howlong = int(textbox.get())     
    for i in range(howlong,0,-1):  
        countlabel.configure(text=i)  
        window.update()          
        time.sleep(1)                                 
    countlabel.configure(text="DONE!")                

window = tkinter.Tk()
window.geometry("800x600")
window.title("Countdown")
window.configure(background="grey")

lbl = tkinter.Label(window, text="How many seconds to count down?")    
lbl.pack()
textbox = tkinter.Entry(window)                                  
textbox.pack()
count = tkinter.Button(window, text="Countdown!", command=countdown)   
count.pack()
countlabel = tkinter.Label(window, height="10", width="10")          
countlabel.pack()

window.mainloop()
