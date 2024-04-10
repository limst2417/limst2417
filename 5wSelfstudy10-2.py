from tkinter import*
import random


btnList = [None]*9
fnameList = ["cha-1.gif", "cha-2.gif", "cha-3.gif", "cha-4.gif", "cha-5.gif", "cha-6.gif", "cha-7.gif", "cha-8.gif", "cha-9.gif"]
random.shuffle(fnameList)
photoList = [None]*9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0


window = Tk()
window.geometry("210x210")

for i in range(0,9) :
    photoList[i] = PhotoImage(file = "C:/Users/강차원/Desktop/보민/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])

for i in range(0,3) :
    for k in range(0,3) :
        btnList[num].place(x = xPos, y = yPos)        
        num += 1 
        xPos += 70               
    xPos = 0
    yPos += 70
    

window.mainloop()    
