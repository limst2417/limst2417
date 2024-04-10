from tkinter import*
from time import*


fnameList = ["cha-1.gif", "cha-2.gif", "cha-3.gif", "cha-4.gif", "cha-5.gif", "cha-6.gif", "cha-7.gif", "cha-8.gif", "cha-9.gif"]
num = 0


def clickNext() :
    global num
    num += 1
    if num > 8:
        num = 0
    pLabel.configure(text = fnameList[num])
            

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
    pLabel.configure(text = fnameList[num])
    

window = Tk()
window.geometry("700x200")
window.title("사진 앨범 제목 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = ">> 다음", command = clickNext)      

pLabel = Label(window, text = fnameList[num], font = ("Arial", 30), fg = "blue")

btnPrev.place(x = 150, y = 10)
btnNext.place(x = 500, y = 10)
pLabel.pack()

window.mainloop()
