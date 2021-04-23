from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("Conversion :  PIED - METRE")
window.configure(background="light gray")
window.geometry("320x220")
window.resizable(width=False, height=False)

feet_label = Label(window, text="Pied",  bg="light gray", fg="black", width=11)
feet_label.grid(column=0, row=0, padx=25, pady=30)

feet_value = DoubleVar()
feet_entry = Entry(window, textvariable=feet_value, width=14)
feet_entry.grid(column=1, row=0)
feet_entry.delete(0, 'end')

meter_label = Label(window, text="Metre",  bg="light gray", fg="black", width=11)
meter_label.grid(column=0, row=1)

meter_value = DoubleVar()
meter_entry = Entry(window, textvariable=meter_value, width=14)
meter_entry.grid(column=1, row=1)
meter_entry.delete(0, 'end')

convert_btn = Button(window, text="Convertir", bg="gray", fg="black", width=10, command="")
convert_btn.grid(column=0, row=3, padx=30, pady=30)

reset_btn = Button(window, text="Effacer", bg="gray", fg="black", width=10, command="")
reset_btn.grid(column=1, row=3)

window.mainloop()
