import tkinter as tk

def add2numbers(i):
    a = int(inputA.get())
    b = int(inputB.get())

    print(i)

    answer.config(text=f"The sum of {a} and {b} is {a+b}.")
    answer.pack()


main = tk.Tk()
main.title("Add 2 numbers")
main.resizable(width=False,height=False)

inputFrame1 = tk.Frame(master=main,padx=10, pady=5, bg= "blue")
inputFrame1.pack()
inputFrame2 = tk.Frame(master=main,padx=10, pady=5, bg="yellow")
inputFrame2.pack()

labelA = tk.Label(master=inputFrame1,text="Input A")
inputA = tk.Entry(master=inputFrame1,width=40)

labelA.pack(side="left")
inputA.pack(side="left")

labelB = tk.Label(master=inputFrame2,text="Input B")
inputB = tk.Entry(master=inputFrame2,width=40)

labelB.pack(side="left")
inputB.pack(side="left")

calcFrame = tk.Frame(master=main,padx=10, pady=5)
calcFrame.pack()

addButton = tk.Button(
    master=calcFrame,
    text="ADD THEM TOGETHER",
    command= lambda : add2numbers(5))
addButton.pack()

answer =tk.Label(master=calcFrame, text="")

main.mainloop()
