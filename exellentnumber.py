import tkinter as tk

def check(entry):

    try:
        x = int(entry)-1
        tab = []

        while x:
            x = x-1
            if x != 0:
                R = int(entry)%x
                if R == 0:
                    tab.append(x)

        if sum(tab) == int(entry):
            label.config(text='Number is perfect!', fg ="green")
        else:
            label.config(text='Number is not perfect!', fg = "red")

    except:
        label.config(text='Please give a number!', fg = "red")


HEIGHT = 200
WIDTH = 400

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#b3ffb3', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.3, anchor='n')

label = tk.Label(frame, font=('Modern',12), anchor = 'w', text ="Please give a number:", bg='#b3ffb3')
label.place(relwidth=1, relheight=0.3)


entry = tk.Entry(frame, font=('Tahoma',20))
entry.place(relx=0, rely=0.4, relwidth=0.65, relheight=0.7)

button = tk.Button(frame, text="Check", font=('Tahoma',10), command=lambda: check(entry.get()))
button.place(relx=0.68, rely=0.4, relheight=0.7, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#b3ffb3', bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.4, anchor='n')

label = tk.Label(lower_frame, font=('Modern',20), justify='center')
label.place(relwidth=1, relheight=1)

root.mainloop()







