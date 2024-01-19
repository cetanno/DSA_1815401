import tkinter as tk

def showLabel():
    data = textinput.get()
    print(data)

    textlabel.config(text= f"\"{data}\" has been entered!")

    textlabel.pack()

main = tk.Tk()
main.title("Python is the best")
main.resizable(width=False,height=False)

# FRAMES, AND PACKING

# frame1 = tk.Frame(master=main, width= 400, height=200, bg="red", padx=5, pady=5)
# frame2 = tk.Frame(master=main, width= 200, height=200, bg="blue", padx=5, pady=5)
# frame3 = tk.Frame(master=main, width= 200, height=200, bg="green", padx=5, pady=5)
# #
# frame1.pack(side="bottom")
# frame2.pack(side="right")
# frame3.pack()

# GRID, LABELS, AND RELIEF
#
# for i in range(5):
#     for j in range(5):
#         framegrid = tk.Frame(master=main)
#         text = tk.Label(
#             master=framegrid,
#             text=f" Row {i} and\n Column {j}",
#             width=10,
#             height=5,
#             relief="raised" # other options are groove, raised, and 3 more
#         )
#         text.pack()
#         framegrid.grid(row=i,column=j)

buttonframe= tk.Frame(master=main, width= 500, padx=10, pady=5)
buttonframe.pack()
#
textinput = tk.Entry(master=buttonframe, width= 50)
textinput.pack(side="left")
#
button1 = tk.Button(
    master=buttonframe,
    text="Click Me",
    width=10,
    command=showLabel)
button1.pack(side="left")
#
textlabel = tk.Label(
    master=buttonframe,
    text="",
    height=2)

# Frame, Entry, Button, Label


main.mainloop()