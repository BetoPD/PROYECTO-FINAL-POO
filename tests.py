import tkinter as tk

def display_values():
    values = [var.get() for var in vars_list]
    print("Selected values:", values)

root = tk.Tk()

vars_list = []

for i in range(4):
    var = tk.StringVar()
    vars_list.append(var)

    label = tk.Label(root, text="Input " + str(i+1))
    label.pack()

    for option in ["Option A", "Option B"]:
        radio_button = tk.Radiobutton(root, text=option, variable=var, value=option)
        radio_button.pack()

button = tk.Button(root, text="Display Values", command=display_values)
button.pack()

root.mainloop()
