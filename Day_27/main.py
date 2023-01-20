from tkinter import *


def miles_to_km():
    """
    calculate miles to kilometers fucntion
    """
    miles = float(miles_input.get())
    km = round(miles * 1.609)

    # Change value of kolmeter_result_label object
    kolmeter_result_label.config(text=f"{km}")


# Set up the window bject
window = Tk()
window.title("Milest to Kilometers Converter")
window.config(padx=20, pady=20)

# Set up the miles input label
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Set up the miles text label
miles_laber = Label(text="Miles")
miles_laber.grid(column=2, row=0)

# Set up the  is equal text label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Set up the  kilometer result text label
kolmeter_result_label = Label(text="0")
kolmeter_result_label.grid(column=1, row=1)

# Set up the kilometer text label
kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=2)

# Setu up the calculate button label
calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
